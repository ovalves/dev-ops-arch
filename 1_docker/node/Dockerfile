FROM node:18.9.0-alpine3.16

RUN apk add --no-cache bash

RUN npm i -g @nestjs/cli@9.1.5
RUN npm i mongodb --save

COPY src app
COPY .docker/entrypoint.sh app/entrypoint.sh
COPY package.json app/package.json

WORKDIR /app

CMD [ "sh", "./entrypoint.sh" ]