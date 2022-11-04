package main

import (
	"encoder/application/repositories"
	"encoder/domain"
	"encoder/framework/database"
	s3_client "encoder/infra/aws"
	"log"
	"os"
	"time"

	"github.com/joho/godotenv"
)

func loadEnv() {
	err := godotenv.Load()
	if err != nil {
		log.Fatalf("Error loading .env file")
	}
}

func prepare() (*domain.Video, repositories.VideoRepositoryDb) {
	db := database.NewDbTest()
	defer db.Close()

	video := domain.NewVideo()
	video.ID = "file_example_MP4_480_1_5MG.mp4"
	video.FilePath = "file_example_MP4_480_1_5MG.mp4"
	video.CreatedAt = time.Now()

	repo := repositories.VideoRepositoryDb{Db: db}

	return video, repo
}

func main() {
	loadEnv()
	awsClient := s3_client.NewAwsClient()
	awsClient.Upload(os.Stdin, "file_example_MP4_480_1_5MG.mp4")

	awsClient.Download("file_example_MP4_480_1_5MG.mp4")
}
