# GRPC

## Quando utilizar?
- Ideal para microserviços
- Mobile, Browsers e Backend
- Geração de bibliotecas de forma automática
- Streaming bidirecional utilizando HTTP/2

## Protocol Buffers vs JSON
- Arquivos binários < JSON
- Processo de serialização é mais leve (CPU) do que JSON
- Gasta menos recursos de rede
- Processo é mais veloz

## HTTP/2
- Nome original criado pela Google era SPDY
- Lançado em 2015
- Dados trafegados são binários e não texto como HTTP 1.1
- Utiliza a mesma conexão TCP para enviar e receber dados do cliente e do servidor (Multiplex)
- Server Push
- Headers são comprimidos
- Processo é mais veloz

## gRPC - API "Unary"
## gRPC - API "Server Streaming"
## gRPC - API "Client Streaming"
## gRPC - API "Bi directional Streaming"

## Site gRPC
> https://grpc.io/

## Site Protocol Buffers
> https://developers.google.com/protocol-buffers

## Instalando dependências do Proto buffers e gRPC
```
go get google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest

go get google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
```

## Exemplo de implementação de gRPC

1. Suba o container rodando:
```
docker-compose up -d
```

2. Acesse o container:
```
docker-compose exec app sh
```

3. Caso queira gerar novamente as stubs:
```
protoc --proto_path=proto/ proto/*.proto --plugin=$(go env GOPATH)/bin/protoc-gen-go-grpc --go-grpc_out=. --go_out=.
```