The idea of repository based on https://github.com/chaserhkj/PyMajSoul/

Python wrappers for Majsoul allow you to interact with their servers from Python scripts.

## For User

### Installation

1. Install Python 3.9 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Login with username and password (CN server)

```bash
python example.py -u <username> -p <password>
```

#### Login with email verification code (EN/JP server)

See `example.py` for reference on how to use email login.

#### Fetch game records

```bash
python example.py -u <username> -p <password> -l <game_uuid>
```

### API Example

```python
import asyncio
from ms.base import MSRPCChannel
from ms.rpc import Lobby
import ms.protocol_pb2 as pb

async def main():
    # Connect to server
    channel = MSRPCChannel("wss://route-2.maj-soul.com/gateway")
    await channel.connect("https://game.maj-soul.com")

    lobby = Lobby(channel)

    # Login
    req = pb.ReqLogin()
    req.account = "your_username"
    req.password = "your_password_hash"
    req.device.is_browser = True
    req.gen_access_token = True

    res = await lobby.login(req)
    print(f"Account ID: {res.account_id}")
    print(f"Nickname: {res.account.nickname}")

    # Fetch account info
    req_info = pb.ReqAccountInfo()
    res_info = await lobby.fetch_account_info(req_info)
    print(f"Level: {res_info.account.level}")

    await channel.close()

asyncio.run(main())
```

### Server Support

| Server | Login Method | Notes |
|--------|-------------|-------|
| CN (中国) | Username + Password | Primary method |
| EN (International) | Email verification | Requires email code |
| JP (日本) | Email verification | Requires email code |

**Note:** Only CN server accounts can use username/password login. EN/JP server accounts require email verification or OAuth2 login.

## For Developer

### Requirements

1. Install Python packages from `requirements.txt`
2. Install protobuf compiler: `sudo apt install protobuf-compiler`

### How to update protocol files to the new version

Tested on Ubuntu:

1. Download the new `liqi.json` file from MS (find it in the network tab of your browser) and put it to `ms/liqi.json`
2. `python generate_proto_file.py`
3. `protoc --python_out=. protocol.proto`
4. `chmod +x ms-plugin.py`
5. `sudo cp ms-plugin.py /usr/bin/ms-plugin.py`
6. `protoc --custom_out=. --plugin=protoc-gen-custom=ms-plugin.py ./protocol.proto`

### How to release new version

1. `pip install twine`
2. `python setup.py sdist`
3. `twine upload dist/*`
