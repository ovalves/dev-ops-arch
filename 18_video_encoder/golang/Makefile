test:
	go test -cover ./...

run:
	docker compose up -d
	go run framework/cmd/server/server.go

.PHONY: server test