package s3_client

import (
	"context"
	"fmt"
	"os"
	"path/filepath"
	"time"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/awserr"
	"github.com/aws/aws-sdk-go/aws/request"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
	"github.com/aws/aws-sdk-go/service/s3/s3manager"
)

type AwsClient struct {
	svc      s3.S3
	ctx      context.Context
	session  *session.Session
	cancelFn func()
}

func NewAwsClient() *AwsClient {
	aws_client := AwsClient{}
	aws_client.createSessionService()
	aws_client.createRequestContext()
	return &aws_client
}

func (client *AwsClient) createSessionService() {
	_client := session.Must(session.NewSessionWithOptions(session.Options{
		SharedConfigState: session.SharedConfigEnable,
	}))

	client.session = _client

	_svc := s3.New(_client, &aws.Config{
		CredentialsChainVerboseErrors: aws.Bool(true),
	})

	client.svc = *_svc
}

func (client *AwsClient) createRequestContext() {
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

func (client *AwsClient) Download(item string) {
	file, err := os.Create(filepath.Join(os.Getenv("localStoragePath"), item))
	if err != nil {
		fmt.Printf("Error in downloading from file %s: %v \n", item, err)
		os.Exit(1)
	}

	defer file.Close()

	downloader := s3manager.NewDownloader(client.session, func(d *s3manager.Downloader) {
		d.PartSize = 64 * 1024 * 1024
		d.Concurrency = 6
	})

	numBytes, err := downloader.Download(file,
		&s3.GetObjectInput{
			Bucket: aws.String(os.Getenv("AWS_BUCKET_NAME")),
			Key:    aws.String(item),
		})

	if err != nil {
		fmt.Printf("Error in downloading. The file %s was not found in Bucket %v \n", item, err)
		os.Exit(1)
	}

	fmt.Println("Download completed", file.Name(), numBytes, "bytes")
}
