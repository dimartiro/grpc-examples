package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"net"

	pb "github.com/dimartiro/grpc-examples/protos"
	"google.golang.org/grpc"
)

var (
	port       = flag.Int("port", 50051, "The server port")
	valuesList = make([]string, 0)
)

type server struct {
	pb.UnimplementedDemoServer
}

func (s *server) Hello(ctx context.Context, in *pb.HelloRequest) (*pb.HelloReply, error) {
	log.Printf("Message received {%v}\n", in)

	reply := &pb.HelloReply{Message: "Hello " + in.GetName()}
	return reply, nil
}

func (s *server) Append(ctx context.Context, in *pb.AppendRequest) (*pb.AppendReply, error) {
	log.Printf("Message received {%v}\n", in)

	//Add new value in values list
	valuesList = append(valuesList, in.GetValue())

	reply := pb.AppendReply{Values: valuesList}
	return &reply, nil
}

func main() {
	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterDemoServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
