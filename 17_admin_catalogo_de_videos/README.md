# Design - Painel Administrativo de Catalogo de Vídeos

# Back of the envelope estimation
As estimativas a seguir são baseadas em algumas suposições.

* Custo de Armazenamento
    * Suponha que a aplicação terá 5 milhões usuários ativos diários (DAU).
    * Suponha que a aplicação terá 1000 vídeos ativos.
    * Os usuários assistem a 5 vídeos por dia.
    * Suponha que o tamanho médio de um vídeo seja de 300 MB.
    * **Espaço de armazenamento necessário total: 1000 vídeos * 300 MB = 300 GB**
* Custo de Streaming de Vídeos.
    * Quando o Cloud CDN serve um vídeo, você é cobrado pelos dados transferidos para fora da CDN.
    * Suponha que o custo médio per GB é $0.02.
    * **5 milhões * 5 videos * 0.3GB * $0.02 = $150.000 por dia.**

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
