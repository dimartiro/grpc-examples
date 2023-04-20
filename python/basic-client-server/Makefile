gen-stubs:
	@echo "Generating stubs..."
	@python3 -m grpc_tools.protoc -Iprotos --python_out=. --pyi_out=. --grpc_python_out=. protos/demo.proto
	@echo "Stubs created..."
