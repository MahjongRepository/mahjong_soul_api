import setuptools

from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='ms_api',
    packages=[
        'ms',
    ],
    version='0.8.188',
    description='Python wrapper for the Mahjong Soul (Majsoul) Protobuf objects. It allows to use their API.',
    long_description='',
    author='Nihisil',
    author_email='alexey@nihisil.com',
    url='https://github.com/MahjongRepository/mahjong_soul_api',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
