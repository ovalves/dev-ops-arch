SHELL := /bin/bash

help:
	@echo ""
	@echo "Commands:"
	@echo "  dev-start           Iniciar todos os serviços do Kafka"
	@echo "  dev-stop            Parar todos os serviços do Kafka"
	@echo "  logs                Exibir todos os logs"

dev-start:
	docker compose -f ./.docker/docker-compose_dev.yaml up -d

dev-stop:
	docker compose -f ./.docker/docker-compose_dev.yaml down -v

logs:
	docker compose logs