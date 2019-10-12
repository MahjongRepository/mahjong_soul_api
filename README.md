It is the fork of https://github.com/chaserhkj/PyMajSoul/ package with different improvements.

`example.py` is working only with **Python3.7+**.

# How to update protocol files to the newest version

1. Download the new liqi.json file (find it in the network tab of your browser) and put it to data/liqi.json. For example https://mahjongsoul.game.yo-star.com/v0.6.58.w/res/proto/liqi.json
2. `cd ms`
3. `python generate_proto_file.py`

# Hot to update RPC wrapper

1. Install protobuf compiler first `sudo apt install protobuf-compiler`
2. `cd ms`
3. `chmod +x ms-plugin.py`
4. `sudo cp ms-plugin.py /usr/bin/ms-plugin.py`
5. `protoc --custom_out=. --plugin=protoc-gen-custom=ms-plugin.py ./data/protocol.proto`