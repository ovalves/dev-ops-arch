FROM node:18.9.0

COPY ["/app/package.json", "/app/package-lock.json*"]
COPY app app

WORKDIR /app
RUN npm install

CMD [ "node", "./src/server.js" ]