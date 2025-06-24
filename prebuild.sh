#!/bin/bash -xe

if [[ $DIST_TYPE == el && $DIST_VERSION == [89] ]]; then
    # EPEL7: libtelnet, libuv, libwebsockets
    # EPEL8: libssh2
    build_dl "https://dl.fedoraproject.org/pub/epel/epel-release-latest-$DIST_VERSION.noarch.rpm"
    rpm -Uvh "$CACHEDIR/epel-release-latest-$DIST_VERSION.noarch.rpm"
else
    echo "FATAL: Unsupported build target, DIST=$DIST"
    exit 2
fi
