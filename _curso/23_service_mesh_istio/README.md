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

### Criando cluster K8s
```bash
k3d cluster create -p "7000:30000@loadbalancer" --agents 2
```