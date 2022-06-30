## Ambiente para executar o Laminas API Tools

```bash
git clone https://github.com/codeedu/api-tools-skeleton.git api-tools-test
docker build -t api-tools-test .
docker run -p 8000:80 -v $(pwd):/var/www api-tools-test
```

> Acesse: http://localhost:8000