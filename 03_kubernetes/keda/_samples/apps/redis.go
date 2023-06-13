package main

import (
	"fmt"
	"os"

	"github.com/go-redis/redis"
)

func makeClient() *redis.Client {
	options := &redis.Options{
		Addr:     os.Getenv("REDIS_ADDRESS"),
		Password: "",
		DB:       0,
	}

	return redis.NewClient(options)
}

func Publish() (int64, error) {
	client := makeClient()

	values := make([]string, 100)
	for i := range values {
		values[i] = fmt.Sprintf("Message #%d\n", i)
	}

	cmd := client.RPush("default", values)
	if cmd.Err() != nil {
		return 0, cmd.Err()
	}
	return cmd.Result()
}

func Drain() (string, error) {
	client := makeClient()
	cmd := client.LTrim("default", 1, 0)

	if cmd.Err() != nil {
		return "error", cmd.Err()
	}
	return cmd.Result()
}
