#!/bin/bash
docker run -ti --rm --name rpi -e QEMU_EXECVE=1 -v $(pwd)/qemu/qemu-arm-static:/usr/bin/qemu-arm-static -v $(pwd)/qemu/sh-shim:/usr/bin/sh-shim -v $(pwd)/qemu/cross-build-start:/usr/bin/cross-build-start philipz/rpi-raspbian-mqtt cross-build-start && echo "Hello World, Philipz!"
