# How to use

## Requisites

### Install golang

You can download golang from the [official site](https://go.dev/dl/)

### Install protoc

More info [here](https://grpc.io/docs/protoc-installation/)

On linux with apt
```
apt install -y protobuf-compiler
```

On mac
```
brew install protobuf
```

On windows
```
You should not use windows if you want to be a software engineer :D
```

## Generate proto stubs
```
make gen-go
```
or execute
```
protoc --go_out=. --go_opt=paths=source_relative --go-grpc_out=. --go-grpc_opt=paths=source_relative protos/demo.proto
```

## Execute server
```
go run server/main.go
```

## Execute client
```
go run client/main.go
```