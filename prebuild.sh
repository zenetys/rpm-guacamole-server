#!/bin/bash -xe

if [[ $DIST_TYPE == el ]]; then
    # EPEL6: libwebp
    # EPEL7: libtelnet, libuv, libwebsockets
    # EPEL8: libssh2
    build_dl "https://dl.fedoraproject.org/pub/epel/epel-release-latest-$DIST_VERSION.noarch.rpm"
    rpm -Uvh "$CACHEDIR/epel-release-latest-$DIST_VERSION.noarch.rpm"
fi
