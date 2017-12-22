FROM node

RUN mkdir -p /app

WORKDIR /app

COPY package.json .

RUN npm cache clean

RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "server.js"]