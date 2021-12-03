#!/bin/sh

for i in {1..100}; do
  curl -X 'GET' 'http://a17c74575c5904dc096d52bf8287e5ba-1188752505.ap-southeast-2.elb.amazonaws.com/system' -H 'accept: application/json' 
  echo -ne '\n'
  sleep 1s
done
