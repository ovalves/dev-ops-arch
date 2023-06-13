package main

import (
	"fmt"
	"log"
	"os"

	"github.com/urfave/cli"
)

func main() {
	app := &cli.App{
		Name:  "app",
		Usage: "Keda Sample",
		Commands: []cli.Command{
			{
				Name:  "api",
				Usage: "Runs simple API on PORT 3003",
				Action: func(c *cli.Context) error {
					StartAPI()
					return nil
				},
			},
			{
				Name:  "redis",
				Usage: "redis methods",
				Subcommands: []cli.Command{
					{
						Name:  "publish",
						Usage: "Publishes messages to Redis list",
						Action: func(c *cli.Context) error {
							result, err := Publish()
							if err != nil {
								fmt.Println("Failed to publish messages")
								log.Fatal(err)
							} else {
								fmt.Printf("Published messages, actual list len: %d\n", result)
							}
							return nil
						},
					},
					{
						Name:  "drain",
						Usage: "Drains the Redis list",
						Action: func(c *cli.Context) error {
							_, err := Drain()
							if err != nil {
								fmt.Println("Failed to drain Redis list")
								log.Fatal(err)
							} else {
								fmt.Println("Queue drained.")
							}
							return nil
						},
					},
				},
			},
		},
	}

	err := app.Run(os.Args)
	if err != nil {
		log.Fatal(err)
	}
}
