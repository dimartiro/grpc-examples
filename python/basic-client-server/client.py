from __future__ import print_function

import logging

import grpc
import demo_pb2_grpc
import demo_pb2

SERVER_HOST  = "localhost:50051"
DEFAULT_NAME = "World!"

def run():
	#Create client connection with auto close
	with grpc.insecure_channel(SERVER_HOST) as channel:
		#Get client connection
		stub = demo_pb2_grpc.DemoStub(channel)

		#Execute hello call
		executeHelloCall(stub)
	
		#Execute append call adding 10 elements
		#executeAppendCall(stub)

	print("Connection closed")


def executeHelloCall(stub):
	helloReply = stub.Hello(demo_pb2.HelloRequest(name=DEFAULT_NAME))
	print("Response: %s" % helloReply.message)

def executeAppendCall(stub):
	for i in range(1, 11):
		print("Adding element: %d" % i)
		appendReply = stub.Append(demo_pb2.AppendRequest(value = str(i)))
		print("Response: %s" %appendReply.values)


if __name__ == '__main__':
	logging.basicConfig()
	run()