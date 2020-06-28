It is the fork of https://github.com/chaserhkj/PyMajSoul/ package with different improvements.

`example.py` is working only with **Python3.7+**.

## Requirements

1. Install python packages from `requerements.txt`
1. Install protobuf compiler `sudo apt install protobuf-compiler`

## How to update protocol files to the new version

It was tested on Ubuntu.

1. Download the new `liqi.json` file (find it in the network tab of your browser) and put it to `ms/liqi.json`
1. `python generate_proto_file.py`
1. `protoc --python_out=plugins=grpc:. protocol.proto`
1. `chmod +x ms-plugin.py`
1. `sudo cp ms-plugin.py /usr/bin/ms-plugin.py`
1. `protoc --custom_out=. --plugin=protoc-gen-custom=ms-plugin.py ./protocol.proto`