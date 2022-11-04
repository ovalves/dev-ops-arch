package services

import (
	s3_client "encoder/infra/aws"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"runtime"
	"strings"
)

type VideoUpload struct {
	Paths     []string
	VideoPath string
	Errors    []string
}

func NewVideoUpload() *VideoUpload {
	return &VideoUpload{}
}

func (vu *VideoUpload) uploadObject(objectPath string) error {
	path := strings.Split(objectPath, os.Getenv("localStoragePath")+"/")
	file, err := os.Open(objectPath)

	if err != nil {
		return err
	}

	defer file.Close()

	awsClient := s3_client.NewAwsClient()

	fmt.Println(file)
	fmt.Println(path[1])
	fmt.Println(path)
	awsClient.Upload(file, path[1])

	return nil
}

func (vu *VideoUpload) loadPaths() error {

	err := filepath.Walk(vu.VideoPath, func(path string, info os.FileInfo, err error) error {

		if !info.IsDir() {
			vu.Paths = append(vu.Paths, path)
		}
		return nil
	})

	if err != nil {
		return err
	}
	return nil
}

func (vu *VideoUpload) ProcessUpload(concurrency int, doneUpload chan string) error {

	in := make(chan int, runtime.NumCPU())
	returnChannel := make(chan string)

	err := vu.loadPaths()
	if err != nil {
		return err
	}

	for process := 0; process < concurrency; process++ {
		go vu.uploadWorker(in, returnChannel)
	}

	go func() {
		for x := 0; x < len(vu.Paths); x++ {
			in <- x
		}
		close(in)
	}()

	for r := range returnChannel {
		if r != "" {
			doneUpload <- r
			break
		}
	}

	return nil

}

func (vu *VideoUpload) uploadWorker(in chan int, returnChan chan string) {

	for x := range in {
		err := vu.uploadObject(vu.Paths[x])

		if err != nil {
			vu.Errors = append(vu.Errors, vu.Paths[x])
			log.Printf("error during the upload: %v. Error: %v", vu.Paths[x], err)
			returnChan <- err.Error()
		}

		returnChan <- ""
	}

	returnChan <- "upload completed"
}
