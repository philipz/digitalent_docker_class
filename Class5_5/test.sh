#!/bin/bash
string=$(docker logs sub);

if [[ ${string} == *"Hello_World,Philipz!"* ]]; then
  echo "Passed";
  exit 0
fi
  echo "Failed"
  exit 1
