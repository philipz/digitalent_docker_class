FROM philipz/rpi-raspbian:latest

ENV QEMU_EXECVE 1
COPY qemu/cross-build-end qemu/cross-build-start qemu/qemu-arm-static qemu/sh-shim /usr/bin/
RUN [ "cross-build-start" ]
RUN apt-get update && apt-get install -y mosquitto-clients
RUN [ "cross-build-end" ]
