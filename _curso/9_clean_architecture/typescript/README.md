# Clean Architecture

## Regras vs Detalhes
* Regras de negócio trazem o real valor para o software
* Detalhes ajudam a suportar as regras de negócio
* Detalhes não devem impactar nas regras de negócio
* Frameworks, banco de dados, APIs, não devem impactar as regras de negócio

## Keep Options Open
...

## Use Cases
Casos de uso representam intenções. Cada intenção deve ter seu próprio caso de uso. Exemplo em um CRUD cada etapa deve ter seu próprio caso de uso.

## DTO (Data Transfer Object)
* Usado para Trafegar dados entre os limites arquiteturais;
* Objeto anêmico, sem comportamento;
* Contém dados (input ou output);
* Não deve possuir regras de negócio.

## Presenters
Presenters são objetos de transformação, que server para adequar o DTO de output no formato correto para entregar o resultado. Um sistema pode ter diversos formatos de entrega: Exemplo: XML, JSON, ProtoBuf, GraphQL, CLI, etc.

## Notification Pattern
...