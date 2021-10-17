#!/bin/bash

sed -i "s/SERVER_ADDRESS/$SERVER_ADDRESS/g" /usr/src/app/my-app/src/components/Main.vue
sed -i "s/SERVER_PORT/$SERVER_PORT/g" /usr/src/app/my-app/src/components/Main.vue

exec "$@"