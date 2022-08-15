# Clean Architecture

## Regras vs Detalhes
* Regras de negócio trazem o real valor para o software
* Detalhes ajudam a suportar as regras de negócio
* Detalhes não devem impactar nas regras de negócio
* Frameworks, banco de dados, APIs, não devem impactar as regras de negócio

## Keep Options Open
...

## Use Cases
Casos de uso representam intenções. Cada itenção de deve ter seu próprio caso de uso. Exemplo em um CRUD cada etapa deve ter seu próprio caso de uso.

## DTO (Data Transfer Object)
* Usado para Trafegar dados entre os limites arquiteturais;
* Objeto anêmico, sem comportamento;
* Contém dados (input ou output);
* Não deve possuir regras de negócio.


