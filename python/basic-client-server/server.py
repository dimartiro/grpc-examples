from concurrent import futures

import grpc
import demo_pb2
import demo_pb2_grpc

class Greeter(demo_pb2_grpc.DemoServicer):
    valuesList = []

    def Hello(self, request, context):
        print("Message received %s" % request)
        
        reply = demo_pb2.HelloReply(message='Hello %s' % request.name)
        return reply
    
    def Append(self, request, context):
        print("Message received %s" % request)

        self.valuesList.append(request.value)
        reply = demo_pb2.AppendReply(values=self.valuesList)
        return reply
    
def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_DemoServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()