# Gitops

## Criando a imagem
```bash
docker build --tag gitops-node-server:latest --no-cache .
```

## Executando a imagem
```bash
docker run --rm -p 3000:3000 gitops-node-server:latest
```

## Matando o container
```bash
docker stop $(docker ps -a -q)
```