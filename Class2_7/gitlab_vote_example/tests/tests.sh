#!/bin/sh
curl -sS -X POST --data "vote=b" http://vote > /dev/null
sleep 10
if phantomjs render.js http://result | grep -q '1 vote'; then
  echo -e "\e[42m------------"
  echo -e "\e[92mTests passed"
  echo -e "\e[42m------------"
  exit 0
fi
  echo -e "\e[41m------------"
  echo -e "\e[91mTests failed"
  echo -e "\e[41m------------"
  exit 1
