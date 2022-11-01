package main

import (
	aws_client "encoder/infra/aws"
	"fmt"
	"log"
	"os"

	"github.com/joho/godotenv"
)

// Uploads a file to S3 given a bucket and object key. Also takes a duration
// value to terminate the update if it doesn't complete within that time.
//
// The AWS Region needs to be provided in the AWS shared config or on the
// environment variable as `AWS_REGION`. Credentials also must be provided
// Will default to shared config file, but can load from environment if provided.
//
// Usage:
//
//	# Upload myfile.txt to myBucket/myKey. Must complete within 10 minutes or will fail
//	go run withContext.go -b mybucket -k myKey -d 10m < myfile.txt
func loadEnv() {
	err := godotenv.Load()
	if err != nil {
		log.Fatalf("Error loading .env file")
	}
}

// func main() {
// 	loadEnv()
// 	timeout, _ := time.ParseDuration(os.Getenv("AWS_UPLOAD_TIMEOUT"))

// 	// All clients require a Session. The Session provides the client with
// 	// shared configuration such as region, endpoint, and credentials. A
// 	// Session should be shared where possible to take advantage of
// 	// configuration and credential caching. See the session package for
// 	// more information.
// 	client := session.Must(session.NewSessionWithOptions(session.Options{
// 		SharedConfigState: session.SharedConfigEnable,
// 	}))

// 	// Create a new instance of the service's client with a Session.
// 	// Optional aws.Config values can also be provided as variadic arguments
// 	// to the New function. This option allows you to provide service
// 	// specific configuration.
// 	// svc := s3.New(client)

// 	svc := s3.New(client, &aws.Config{
// 		// Region:                        aws.String("us-east-1"),
// 		CredentialsChainVerboseErrors: aws.Bool(true),
// 	})

// 	// Create a context with a timeout that will abort the upload if it takes
// 	// more than the passed in timeout.
// 	ctx := context.Background()
// 	var cancelFn func()
// 	if timeout > 0 {
// 		ctx, cancelFn = context.WithTimeout(ctx, timeout)
// 	}
// 	// Ensure the context is canceled to prevent leaking.
// 	// See context package for more information, https://golang.org/pkg/context/
// 	if cancelFn != nil {
// 		defer cancelFn()
// 	}

// 	// Uploads the object to S3. The Context will interrupt the request if the
// 	// timeout expires.
// 	_, err := svc.PutObjectWithContext(ctx, &s3.PutObjectInput{
// 		Bucket: aws.String(os.Getenv("AWS_BUCKET_NAME")),
// 		Key:    aws.String("Sample"),
// 		Body:   os.Stdin,
// 	})

// 	fmt.Println(err)
// 	if err != nil {
// 		if aerr, ok := err.(awserr.Error); ok && aerr.Code() == request.CanceledErrorCode {
// 			fmt.Fprintf(os.Stderr, "upload canceled due to timeout, %v\n", err)
// 		} else {
// 			fmt.Fprintf(os.Stderr, "failed to upload object, %v\n", err)
// 		}
// 		os.Exit(1)
// 	}

// 	fmt.Printf("successfully uploaded file to %s/%s\n", os.Getenv("AWS_BUCKET_NAME"), os.Getenv("AWS_OBJECT_KEY"))
// }

func main() {
	loadEnv()
	awsClient := aws_client.NewAwsClient()
	awsClient.Upload(os.Stdin, "mais um verde")
	fmt.Println(awsClient)
}
