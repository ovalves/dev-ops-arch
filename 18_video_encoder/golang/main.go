package main

import (
	aws_client "encoder/infra/aws"
	"log"
	"os"

	"github.com/joho/godotenv"
)

func loadEnv() {
	err := godotenv.Load()
	if err != nil {
		log.Fatalf("Error loading .env file")
	}
}

func main() {
	loadEnv()
	awsClient := aws_client.NewAwsClient()
	awsClient.Upload(os.Stdin, "ola mundo")
}
