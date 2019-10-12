import setuptools

from distutils.core import setup

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='mahjong',
    packages=[
        'ms',
    ],
    version='0.0.1',
    description='',
    long_description=readme,
    author='Alexey Lisikhin',
    author_email='lisikhin@gmail.com',
    url='https://github.com/MahjongRepository/mahjong_soul_api',
    data_files=[('', ['README.rst'])],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)
