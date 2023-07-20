help:
	@echo ""
	@echo "Commands:"
	@echo "  deps            Instalar as dependências"
	@echo "  start           Iniciar a API"
	@echo "  stop            Parar a API"
	@echo "  code_formatter  Formatar os códigos"
	@echo "  test            Rodar os testes"
	@echo "  mutation        Rodar os testes de mutação"

deps:
	pip3 install -r requirements.txt
	pip3 install -r requirements.dev.txt

test:
	nose2 -v --with-coverage --coverage-report html --coverage-report term --coverage-report xml

code_formatter:
	black src
	black tests

mutation:
	mutmut run --disable-mutation-types=decorator

start:
	@docker compose -f docker-compose.yaml up -d

stop:
	@docker compose -f docker-compose.yaml down -v