import asyncio
import hashlib
import hmac
import logging
import random
import uuid
from optparse import OptionParser

import aiohttp

from ms.base import MSRPCChannel
from ms.rpc import Lobby
import ms.protocol_pb2 as pb

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

MS_HOST = 'https://game.maj-soul.com'


async def main():
    """
    Login to the CN server with username and password and get latest 30 game logs.
    """
    parser = OptionParser()
    parser.add_option('-u', '--username',
                      type='string',
                      help='Your account name.')
    parser.add_option('-p', '--password',
                      type='string',
                      help='Your account password.')

    opts, _ = parser.parse_args()
    username = opts.username
    password = opts.password
    if not username or not password:
        parser.error('Username or password cant be empty')

    lobby, channel = await connect()
    await login(lobby, username, password)
    game_logs = await load_game_logs(lobby)
    logging.info('Found {} records'.format(len(game_logs)))

    await channel.close()


async def connect():
    async with aiohttp.ClientSession() as session:
        async with session.get('{}/1/version.json'.format(MS_HOST)) as res:
            version = await res.json()
            print(version)
            version = version['version']

        async with session.get('{}/1/v{}/config.json'.format(MS_HOST, version)) as res:
            config = await res.json()
            print(config)
            url = config['ip'][0]['region_urls'][1]

        async with session.get(url + '?service=ws-gateway&protocol=ws&ssl=true') as res:
            servers = await res.json()
            print(servers)
            servers = servers['servers']
            server = random.choice(servers)
            endpoint = 'wss://{}/'.format(server)

    logging.info('Chosen endpoint: {}'.format(endpoint))
    channel = MSRPCChannel(endpoint)

    lobby = Lobby(channel)
    lobby.version = version

    await channel.connect(MS_HOST)
    logging.info('Connection was established')

    return lobby, channel


async def login(lobby, username, password):
    logging.info('Login with username and password')

    uuid_key = str(uuid.uuid1())

    req = pb.ReqLogin()
    req.account = username
    req.password = hmac.new(b'lailai', password.encode(), hashlib.sha256).hexdigest()
    req.device.device_type = 'pc'
    req.device.browser = 'safari'
    req.random_key = uuid_key
    req.client_version = lobby.version
    req.gen_access_token = True
    req.currency_platforms.append(2)

    res = await lobby.login(req)
    token = res.access_token
    if not token:
        logging.error('Login Error:')
        logging.error(res)
        return False

    return True


async def load_game_logs(lobby):
    logging.info('Loading game logs')

    records = []
    current = 1
    step = 30
    req = pb.ReqGameRecordList()
    req.start = current
    req.count = step
    res = await lobby.fetch_game_record_list(req)
    records.extend([r.uuid for r in res.record_list])

    return records


if __name__ == '__main__':
    asyncio.run(main())
