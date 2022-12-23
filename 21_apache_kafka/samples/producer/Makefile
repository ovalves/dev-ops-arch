SHELL := /bin/bash

help:
	@echo ""
	@echo "Commands:"
	@echo "  producer            Iniciar o kafka producer"
	@echo "  build-venv          Criar o ambiente virtual"
	@echo "  start-venv          Iniciar o ambiente virtual"
	@echo "  start               Iniciar todos os serviços"
	@echo "  stop                Parar todos os serviços"
	@echo "  deps                Instalar as libs do projeto"
	@echo "  code_formatter      Rodar a formatação dos códigos"

build-venv:
	python -m venv venv

start-venv:
	@source venv/bin/activate

deps:
	pip3 install -r requirements.txt
	pip3 install -r requirements.dev.txt

producer:
	python src/main.py

dev-start:
	docker compose up -d

dev-stop:
	docker compose down -v

code_formatter:
	black src
