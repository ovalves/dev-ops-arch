# DDD: Modelagem Tática e Patterns

## Elementos táticos
Quando estamos falando sobre DDD e precisamos olhar mais a fundo um bounded context.

Precisamos ser capazes de modelarmos de forma mais assertiva os seus principais componentes, comportamentos e individualidades, bem como suas relações.

## Entidades
"Uma entidade é algo único que é capaz de ser alterado de forma contínua durante um longo período de tempo."
> Vernon, Vaughn. Implementing Domain-Driven Design

"Uma entidade é algo que possui uma continuidade em seu ciclo de vida e pode ser distinguida intependente dos atributos que são importantes para a aplicação do usuário. Pode ser uma pessoa, cidade, carro um ticket de loteria ou uma transação bancária."
> Evans, Eric. Domain-Driven Design

### Entidade anêmica
TODO

### Entidades e Domínio rico
TODO

### Consistência
TODO

### Princípio da Autovalidação
Todas as entidades do sistema precisam se autovaliar, para garantir que nenhum de seus atributos recebam dados incorretos vindos de outras partes do sistema.

### Entidade vs ORM
TODO

## Value Objects
Quando você se preocupa apenas com os atributos dos elementos de uma model, classifique isso como um Value Object.
- Os value Objects devem ser imutáveis.
- Os value Objects precisam se autovalidas
- Os Value Objects não possuem ID

## Aggregate
Um agregado é um conjunto de objetos associados que tratamos como uma unidade para propósito de mudança de dados.

![](../_assets/aggregate.png "Aggregate")

## Domain Services
"Um serviço de domínio é uma operação sem estado que cumpre uma tarefa específica do domínio.
Muitas vezes, a melhor indicação de que você deve criar um Serviço no modelo de domínio é quando a operação a ser executada parece não se encaixar
como um método em um Agregado ou como um objeto de valor."

> Vernon, Vaughn. Implementing Domain-Driven Design.

"Quando um processo ou transformação significativa no domínio não for uma responsabilidade natural de uma ENTIDADE ou OBJETE DE VALOR, adicione uma operação
ao modelo como uma interface autônoma declarada como um SERVIÇO. Defina a interface baseada na linguagem do modelo de domínio e certifique-se de que o nome da
operação faça parte do UBIQUITOUS LANGUAGE. Torne o SERVIÇO sem estado."

> Evans, Eric. Domain-Driven Design

- Quando houver muitos Domain Services em seu projeto. TALVEZ, isso pode indicar que seus agragados estão anêmicos
- Domain Services devem ser Stateless

## Repositories
Um repositório comumente se refere a um local de armazenamento, geralmente considerado um local de segurança ou preservação dos itens nele armazenados.
- Os dados armazenados em um repositório ter seu estado íntegros
- Deve ser possível buscar um item em um repositório
- Deve ser possível remover um item de um repositório
- Todo tipo **Agregado** persistente deve possuir um **Repositório**

> Vernon, Vaughn. Implementing Domain-Driven Design.

## Domain Events
Use um evento de domínio para capturar uma ocorrência de algo que aconteceu no domínio

> Vernon, Vaughn. Implementing Domain-Driven Design.

A essência de um evento de domínio é que você o usa para capturar coisas que podem desencadear uma mudança no estado do aplicativo que você está desenvolvendo. Esses objetos de evento são processados para causar alterações no sistema e armazenados para fornecer um AuditLog.

> Fowler, Martin. Domain Event

- Todo evento deve ser representado em uma ação realizada no passado:
    - UserCreated
    - OrderPlaced
    - EmailSent

### Domain Events - Quando utilizar
Normalmente um Domain Event deve ser utilizado quando queremos notificar outros Bounded Contexts de uma mudança no estado.

### Domain Events - Componentes
- Event
- Handler: Executa o processamento quando um evento é chamado
- Event Dispatcher: Responsável por armazenar e executar os handlers de um evento quando ele for disparado.

## Módulos
Em um contexto DDD, Módulos em seu modelo servem como containers nomeados para classes de objetos de domínio que são altamente coesas entre si.

O objetivo deve ser baixo acoplamento entre as classes que estão em módulos difirentes. Como os módulos usados no DDD não são compartimentos de armazenamento anêmicos ou genéricos, também é importante nomear adequadamente os Módulos.

> Vernon, Vaughn. Implementing Domain-Driven Design.

- Respeitar a linguagem Universal
- Baixo acoplamento
- Um ou mais agregados devem estar juntos somente se fazem sentido
- Organizado pelo domínio/subdomínio e não pelo tipo de objetos
- Devem respeitar a mesma divisão quando estão em camadas diferentes
