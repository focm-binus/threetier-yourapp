#!/bin/sh

sudo docker build -t ${USER}/yourapp-backend:latest ./backend
sudo docker build -t ${USER}/yourapp-frontend:latest ./frontend
sudo docker build -t ${USER}/yourapp-nginx:latest ./nginx