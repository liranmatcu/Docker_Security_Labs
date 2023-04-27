FROM node

WORKDIR /app

COPY package*.json ./

RUN npm install --production

COPY . .

CMD ["npm", "start"]
