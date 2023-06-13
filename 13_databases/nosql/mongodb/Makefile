SHELL := /bin/bash

help:
	@echo ""
	@echo "Commands:"
	@echo "  dev-start Iniciar todos os serviços"
	@echo "  dev-stop  Parar todos os serviços"
	@echo "  logs      Exibir todos os logs"

logs:
	docker compose logs

dev-start:
	docker compose -f ./docker-compose_dev.yml up -d

dev-stop:
	docker compose -f ./docker-compose_dev.yml down -v