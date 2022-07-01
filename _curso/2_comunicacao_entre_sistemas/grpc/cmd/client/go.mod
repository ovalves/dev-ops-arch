module github.com/ovalves/sample-grpc/client

go 1.16

replace github.com/ovalves/sample-grpc/pb => ../../pb

require (
	github.com/ovalves/sample-grpc/pb v0.0.0-00010101000000-000000000000
	google.golang.org/grpc v1.47.0
)
