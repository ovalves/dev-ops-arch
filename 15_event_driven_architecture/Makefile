SHELL := /bin/bash

help:
	@echo ""
	@echo "Commands:"
	@echo "  dev-start     Iniciar todos os serviços"
	@echo "  dev-stop      Parar todos os serviços"
	@echo "  build-wallet  Fazer o build da imagem"

dev-start:
	@docker compose -f docker-compose.yml up -d --force-recreate

dev-stop:
	@docker compose -f docker-compose.yml down -v

build-eda-image:
	@docker build -t eda-wallet/eda-wallet-dev:1.0 wallet -f Dockerfile --no-cache