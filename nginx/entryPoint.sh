#!/bin/bash

sed -i "s/SERVER_ADDRESS/$SERVER_ADDRESS/g" /etc/nginx/nginx.conf

exec "$@"