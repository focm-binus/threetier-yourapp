
FROM node:lts-buster

COPY ./entryPoint.sh /
RUN chmod +x entryPoint.sh

WORKDIR /usr/src/app/my-app

COPY . .

RUN npm install

EXPOSE 8080

ENTRYPOINT ["/entryPoint.sh"]
CMD ["npm", "run", "serve"]