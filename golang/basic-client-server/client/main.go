package main

import (
	"context"
	"fmt"
	"log"

	pb "github.com/dimartiro/grpc-examples/protos"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

const (
	serverHost  = "localhost:50051"
	defaultName = "World!"
)

var (
	serverConnection *grpc.ClientConn
	ctx              = context.Background()
)

func main() {
	//Get client connection
	client := createClient()
	//Execute hello call
	executeHelloCall(client)
	//Execute append call adding 10 elements
	executeAppendCall(client)
	//Close server connection when finished
	closeConnection()
}

func executeHelloCall(client pb.DemoClient) {
	helloReply, err := client.Hello(ctx, &pb.HelloRequest{Name: defaultName})
	if err != nil {
		log.Fatalf("Error executing server call: %v", err)
	}
	log.Printf("Response: %s", helloReply.GetMessage())
}

func executeAppendCall(client pb.DemoClient) {
	for i := 1; i <= 10; i++ {
		log.Printf("Adding element: %d", i)
		appendReply, err := client.Append(ctx, &pb.AppendRequest{Value: fmt.Sprint(i)})
		if err != nil {
			log.Fatalf("Error executing append call: %v", err)
		}
		log.Printf("Response: %s", appendReply.GetValues())
	}
}

func createClient() pb.DemoClient {
	//Configure connection with server
	var err error
	serverConnection, err = grpc.Dial(serverHost, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}

	//Create server connection
	return pb.NewDemoClient(serverConnection)
}

func closeConnection() error {
	return serverConnection.Close()
}
