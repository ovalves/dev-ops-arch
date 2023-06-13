FROM golang:1.19.1 As builder
ENV GO111MODULE=off
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags '-w' -o sample-app

FROM scratch
WORKDIR /app
COPY --from=builder /app/sample-app .
CMD ["/app/sample-app"]