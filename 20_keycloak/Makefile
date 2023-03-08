SHELL := /bin/bash

help:
	@echo ""
	@echo "Commands:"
	@echo "  dev-start           Iniciar todos os serviços do keycloak"
	@echo "  dev-stop            Parar todos os serviços do keycloak"
	@echo "  logs                Exibir todos os logs"

dev-start:
	docker compose -f docker-compose.yaml up -d

dev-stop:
	docker compose -f docker-compose.yaml down -v

logs:
	docker compose logs