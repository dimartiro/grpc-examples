# How to use

## Requisites

### Install Python protoc

```
python3 -m pip install --user grpcio-tools
```

## Generate proto stubs
```
make gen-stubs
```
or execute
```
python3 -m grpc_tools.protoc -Iprotos --python_out=. --pyi_out=. --grpc_python_out=. protos/demo.proto
```

## Execute server
```
python server.py
```

## Execute client
```
python client.py
```