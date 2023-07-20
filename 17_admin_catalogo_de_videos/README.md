# Design - Painel Administrativo de Catalogo de Vídeos


## Design

### API
Para publicar um vídeo, Uma requisição HTTP será feita ao servidor. A requisição é mostrada abaixo:
```
POST /v1/me/feed
Params:
    • content: Texto da postagem.
    • auth_token: Usado para autenticar as requisições para a API.
```

## Arquitetura

# Implementação do projeto

## Tecnologias utilizadas
* Python
* Mysql
* Docker
___

## Como rodar o projeto
```
make start-all
```

### As seguintes portas são utilizadas neste projeto:

| Server | Port  |
|--------|-------|
| mysql  | 33060 |
| API    | 5000  |


### API
