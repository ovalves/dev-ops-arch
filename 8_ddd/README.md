# Domain Driven Design

## Ponto de Partida do DDD
TODO

## Softwares complexos
- DDD é/deve ser aplicado para casos de projetos de softwares complexos;
- Grandes projetos possuem muitas áreas, muitas regras de negócio, muitas pessoas com diferentes visões em diferentes contextos;
- Grande parte da complexidade de projetos grandes não vem da tecnologia, mas sim da comunicação, separação de contextos, entedimento do negócio;

## Como DDD pode ajudar
- Entender com profundidade o domínio e o subdomínio da aplicação;
- Ter uma linguagem universal (linguagem ubíqua) entre todos os envolvidos;
- Criar o design estratégico utilizando Bounded Contexts;
- Criar o design tático para conseguir mapear e agregar as entidades e objetos de valor da aplicação, bem como os eventos de domínio;
- Clareza do que é complexidade de negócio e complexidade técnica.

## Domínios e subdomínios
DDD Context Map

![](../_assets/DDD_Context_Map.jpg "DDD Context Map")

## Espaço de problema e Espaço de Solução
- Espaço de problema
    - Visão geral do domínio e suas complexidades

- Espaço de Solução
    - Análise e modelagem do domínio
    - Gera os contextos delimitados

## Contexto Delimitado
TODO

## Elementos Transversais
TODO

## Context Mapping
![](../_assets/ddd-context-mapping-1.png "DDD Context Map")

- ACL: Anticorruption-layer;
- Integração Conformista: Quando há um grande acoplamente entre a sua plataforma e uma plataforma de terceiros;
- Shared Kernel: Compartilhamento de recursos utilizados por diversos contextos;
- D: Downstream (Utiliza o serviço)
- U: Upstream (Fornece o serviço)

## Padrões de Context Mapping
- Partnership
- Shared Kernel
- Customer-Supplier Development
- Conformist
- Anticorruption-layer
- Open host service
- Published language
- Separate ways
- Big Ball of Mud

### Context Map cheat sheet
> [context-map-cheat-sheet](https://github.com/ddd-crew/context-mapping)
![](../_assets/context-map-cheat-sheet.png "context map cheat sheet")