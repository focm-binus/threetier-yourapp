
FROM node:14.17.5-buster AS build

COPY ./entryPoint.sh /
RUN chmod +x entryPoint.sh

WORKDIR /usr/src/app/my-app

COPY . .

RUN grep "fetch" /usr/src/app/my-app/src/components/Main.vue

RUN npm install
RUN npm run build

FROM nginx:1.19 AS production

COPY nginx.conf /etc/nginx/nginx.conf

USER root

COPY --from=build /usr/src/app/my-app/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]