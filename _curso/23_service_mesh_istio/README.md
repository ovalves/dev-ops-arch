# Service Mesh com Istio
Simplifica a observabilidade, gerenciamento de tráfego, segurança e política com service mesh.

> [istio](https://istio.io/)
> [kiali](https://kiali.io/)

## Service Mesh
Service mesh (malha de serviços) é uma camada extra adicional que tem a função de
para monitor e modificar em tempo real o trafego das aplicações, bem como elevar o nível
de segurança e confiabilidade de todo ecossistema

## Istio
Pode ser usado com:
- Kubernetes
- Apache Mesos
- Consul
- Nomad

### Principais Recursos
- Gerenciamento de trafego
    - gateways (entrada e saída)
    - Load balancing
    - Timeout
    - Políticas de retry
    - Circuit breaker
    - Fault Injection
- Observabilidade
    - Métricas
    - Traces distribuidos
    - Logs
- Segurança
    - Main-in-the-middle
    - mTLS
    - AAA (Authentication, Authorization, Audit)

### Arquitetura do Istio

![](../_assets/sidecar-proxy.png "sidecar proxy")
> sidecar proxy

![](../_assets/istiod.png "Arquitetura do Istio")
> istiod

### Criando cluster K8s com minikube
```bash
.minikube/k8s-minikube.sh start # starts the minikube cluster (alias: up)
```


### Criando tunnel com minikube
```bash
# tunnel creates a route to services deployed with type LoadBalancer and sets their Ingress to their ClusterIP.
# for a detailed example see https://minikube.sigs.k8s.io/docs/tasks/loadbalancer
minikube tunnel
```

### Verificando o serviço do Kiali no K8s
```bash
kubectl -n istio-system get svc kiali
```


### Instalando Istio no cluster
```bash
.minikube/k8s-minikube.sh istio # installs Istio into the minikube cluster
```

#### Injetando Envoy sidecar proxies
Adicione um label de namespace para o Istio injetar automaticamente os sidecar proxies do Envoy no deploy da aplicação

```bash
kubectl label namespace default istio-injection=enabled
```

#### Instalando os Addons do Istio
```bash
kubectl apply -f https://raw.githubusercontent.com/istio/istio/master/samples/addons/grafana.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/master/samples/addons/jaeger.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/master/samples/addons/kiali.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/master/samples/addons/prometheus.yaml
```

### Instalando o Fortio
```bash
go install fortio.org/fortio@latest
cp /home/viniciusoa/.asdf/installs/golang/1.19.1/packages/bin/fortio /usr/local/bin
```

### Executando requisições com Fortio
```bash
fortio load -c 2 -qps 0 -t 200s -loglevel Warning http://10.105.70.198:8000
```


### Gerenciamento de trafego
É possível colocar regras de trafego na destination rule ou nos subsets da destination rule

#### Gateway
Gerencia a entrada e saída do trafego. Trabalha nas layers 4-6, garantindo o gerenciamento de portas, host e TLS.
É conectado diretamente a um Virtual Service que é responsável pelo roteamento.

Tipos:
- Ingress Gateway
- Egress Gateway

#### Virtual Service
Roteador de requisições para um serviço.

Com o Virtual Service podemos configurar regras para:
- Roteamento de trafego
- Subsets
- Fault Injection
- Retries
- Timeout

#### Tipos de Load Balancer
- Round-robin (K8s default)
- random
- Least Conn

### Stick Session e Consistent Hash
TODO

### Circuit Breaker
TODO

### Gateways
TODO
