# Service Discovery

> https://www.consul.io/

- Descobre as máquinas disponíveis para acesso
- Segmentação de máquindas para garantir segurança
- Resolução via DNS
- Health Check

# Consul
- Service Discovery
- Service Segmentation
- Load Balancer na borda (Layer 7)
- Key / Value Configuration

# Agent, Client e Server
- Agent: Processe que fica sendo executado em todos nós do cluster. Pode estar sendo executado em Client Mode ou Server Mode
- Client: Registro os serviços localmente, Health Check, encaminha as informações e configurações dos serviços para o Server
- Server: Mantém o estado do cluster, registra os serviços, Membership (quem é client e quem é server), retorno de queries (DNS ou API),
troca de informações entre datacenters, etc

# Criando Cluster Consul
```bash
# Criar os containers
docker-compose up -d

# Acessar os containers
winpty docker exec -it consulserver01 sh

# Pegar o o IP do container docker
ifconfig

# Criar os diretórios de configs do consul
mkdir /etc/consul.d
mkdir /var/lib/consul

# Criar o server do consul
consul agent -server -bootstrap-expect=3 -node=consulserver01 -bind=172.21.0.4 -data-dir=/var/lib/consul -config-dir=/etc/consul.d

# Visualizando os servers
consul members

# Fazer join dos servers
consul join IP_DO_SERVER_CONSUL
```

# Criando Client Consul
```bash
# Criar os containers
docker-compose up -d

# Acessar os containers
winpty docker exec -it consulserver01 sh

# Pegar o o IP do container docker
ifconfig

# Criar os diretórios de configs do consul
mkdir /etc/consul.d
mkdir /var/lib/consul

# Criar o server do consul
consul agent -bind=172.21.0.5 -data-dir=/var/lib/consul -config-dir=/etc/consul.d

# Visualizando os servers
consul members

# Fazer join dos servers
consul join IP_DO_SERVER_CONSUL
```

# Registrando Serviço
```bash
# Acessar os containers
winpty docker exec -it consulclient01 sh

consul reload
```

# Listando Serviços
```bash
# Acessar os containers
winpty docker exec -it consulclient01 sh

consul catalog nodes -service nginx

consul catalog nodes -detailed

dig @localhost -p 8600 nginx.service.consul

curl localhost:8500/v1/catalog/services
```

# Registrando segundo Serviço - Retry Join
```bash
# Acessar os containers
winpty docker exec -it consulclient01 sh

consul agent -bind=172.21.0.5 -data-dir=/var/lib/consul -config-dir=/etc/consul.d -retry-join=IP_DO_SERVER_CONSUL
```