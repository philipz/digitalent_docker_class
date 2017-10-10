FROM resin/raspberry-pi-python:3.6-slim
MAINTAINER Philpz <philipzheng@gmail.com>

ENV QEMU_EXECVE 1
COPY qemu/cross-build-end qemu/cross-build-start qemu/qemu-arm-static qemu/sh-shim /usr/bin/
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN [ "cross-build-start" ]
RUN pip install --no-cache-dir -r requirements.txt
RUN [ "cross-build-end" ]
COPY mqtt_client.py /usr/src/app
CMD ["python","mqtt_client.py"]
