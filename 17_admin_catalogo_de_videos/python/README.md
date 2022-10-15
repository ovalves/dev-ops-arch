# Micro Video Backend

## Endpoints
TODO:

## Desenvolvimento

Para instalar as dependências do projeto utilize o `virutal env`.

```bash
python -m venv venv
source venv/bin/activate
```

Execute o comando para instalar as dependências
```bash
make
```

### Formatação de código
O código segue o padrão do `black`. Para formatar o código, use o comando:

```
make code_formatter
```

## Testes Unitários
Para executar os testes unitários execute o comando:

```
make test
```

O relatório detalhado com a cobertura dos testes fica em `htmlcov/index.html`.

## Testes de mutação

Rode o comando abaixo para execução dos testes de mutação através do `mutmut`.

```
make mutation
```

## Pesquisar

- libs python:
    - attrs (validação)
    - pydantic (validação)
    - django rest framework
- patterns:
    - Notification Pattern
- testes
    - Piramide de testes
    - Testes de mutação
- python
    - Dataclass
    - peps
        - pep 8
        - [pep 582](https://peps.python.org/pep-0582/)
    - package managers
        - pip
        - Poetry
        - PDM
            - pip install pdm
            - pdm init
            - pdm add autopep8
        - pipenv
        - autopep8 install