# Event Driven Architecture

É um design pattern arquitetural onde comunicação entre os sistemas acontece através de eventos eventos. Esses eventos geralmente são feitos para notificar a mudança de estados dos dados.

Esse tipo de arquitetura gera um baixo acoplamento entre os sistemas.

A interação entre os serviços acontece através de um message broker.

Um ponto de atenção ao utilizar o EDA é pensar em consistência eventual dos dados, como as transações são distribuídas entre os microsserviços envolvidos não é possível garantir a atomicidade das transações.

Por esse motivo, fica a cargo de cada microsserviço tratar a consistência dos dados em suas transações.

## Event Notification
Forma curta de notificação entre sistemas. Quando um sistema quer notificar outro sistema que algo aconteceu.

Exemplo:
- {"pedido": 1, "status": "aprovado"}

## Event Carried State Transfer
Formato completo para trafegar as informações. Trafega toda a informação (payload) através dos eventos.

## Event Sourcing

## Event Colaboration

## CQRS

## Event Sourcing + CQRS

## Elementos táticos de um contexto de eventos
- Evento (Carregar dados)
- Operações que serão executados quando um evento é chamado
- Gerenciador dos eventos/operações
    - Registrar os eventos e suas operações
    - Despachar o evento para executar as operações