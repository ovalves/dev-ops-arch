FROM python:3.11.4-slim

RUN apt update && apt install -y --no-install-recommends \
                    default-jre \
                    git \
                    curl \
                    wget \
                    gcc \
                    libmariadb-dev

RUN useradd -ms /bin/bash python

COPY /bin /app/bin
COPY /src /app/src
COPY .env /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV MY_PYTHON_PACKAGES=/app/__pypackages__/3.11
ENV PYTHONPATH=${PYTHONPATH}/app/src
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH $PATH:${MY_PYTHON_PACKAGES}/bin

ENTRYPOINT ["python", "bin/server"]