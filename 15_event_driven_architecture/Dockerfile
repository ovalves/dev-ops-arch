FROM golang:1.19

WORKDIR /go/src/

RUN apt-get update && \
    apt-get install build-essential protobuf-compiler librdkafka-dev -y

COPY . .

RUN go mod tidy
RUN go mod download
RUN go build -ldflags="-s -w" cmd/walletcore/main.go
RUN ls -lah

EXPOSE 80
CMD ["sh", "-c", "./main"]