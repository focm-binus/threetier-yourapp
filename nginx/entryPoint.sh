#!/bin/bash

sed -i "s/SERVER_ADDRESS/$SERVER_ADDRESS/g" /etc/nginx/nginx.conf
sed -i "s/BACKEND_ADDRESS/$BACKEND_ADDRESS/g" /etc/nginx/nginx.conf
sed -i "s/FRONTEND_ADDRESS/$FRONTEND_ADDRESS/g" /etc/nginx/nginx.conf

exec "$@"