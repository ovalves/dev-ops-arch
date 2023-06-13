FROM golang:1.19.1

WORKDIR /go/src/app
COPY apps/ .

RUN go get -v ./...

RUN go install -v .

ENTRYPOINT ["/go/bin/keda-sample"]