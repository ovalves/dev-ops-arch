package aws_client

import (
	"context"
	"fmt"
	"os"
	"time"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/awserr"
	"github.com/aws/aws-sdk-go/aws/request"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
)

type AwsClient struct {
	svc      s3.S3
	ctx      context.Context
	cancelFn func()
}

func NewAwsClient() *AwsClient {
	aws_client := &AwsClient{}
	aws_client.service()
	aws_client.requestContext()
	return aws_client
}

func (client *AwsClient) service() {
	_client := session.Must(session.NewSessionWithOptions(session.Options{
		SharedConfigState: session.SharedConfigEnable,
	}))

	_svc := s3.New(_client, &aws.Config{
		CredentialsChainVerboseErrors: aws.Bool(true),
	})

	client.svc = *_svc
}

func (client *AwsClient) requestContext() {
	timeout, _ := time.ParseDuration(os.Getenv("AWS_UPLOAD_TIMEOUT"))

	ctx := context.Background()
	var cancelFn func()
	if timeout > 0 {
		ctx, cancelFn = context.WithTimeout(ctx, timeout)
	}

	client.cancelFn = cancelFn
	client.ctx = ctx
}

func (client *AwsClient) Upload(file *os.File, filename string) {
	if client.cancelFn != nil {
		defer client.cancelFn()
	}

	_, err := client.svc.PutObjectWithContext(client.ctx, &s3.PutObjectInput{
		Bucket: aws.String(os.Getenv("AWS_BUCKET_NAME")),
		Key:    aws.String(filename),
		Body:   file,
	})

	if err != nil {
		if aerr, ok := err.(awserr.Error); ok && aerr.Code() == request.CanceledErrorCode {
			fmt.Fprintf(os.Stderr, "upload canceled due to timeout, %v\n", err)
		} else {
			fmt.Fprintf(os.Stderr, "failed to upload object, %v\n", err)
		}
		os.Exit(1)
	}

	fmt.Printf("successfully uploaded file to %s/%s\n", os.Getenv("AWS_BUCKET_NAME"), os.Getenv("AWS_OBJECT_KEY"))
}
