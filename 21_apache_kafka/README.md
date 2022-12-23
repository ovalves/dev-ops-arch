# Apache Kafka

## Como executar

```bash
make dev-start
```

## Visualizando todos os tópicos registrados no Kafka

```
docker compose ps

docker exec -it CONTAINER_ID /bin/bash

kafka-topics --list --bootstrap-server=localhost:9092
```

## Consumindo as mensagens dos tópicos do Kafka

```
docker compose ps

docker exec -it CONTAINER_ID /bin/bash

kafka-console-consumer --topic=NOME_DO_TOPICO --bootstrap-server=localhost:9092
```