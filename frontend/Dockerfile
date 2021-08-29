FROM node:14.17.4

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends less

COPY ./package.json .
COPY ./package-lock.json .

RUN npm install

COPY . .