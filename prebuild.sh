#!/bin/bash -xe

if [[ $DIST == el6 || $DIST == el7 ]]; then
    # EPEL6: libwebp
    # EPEL7: libtelnet, libuv, libwebsockets
    build_dl "https://dl.fedoraproject.org/pub/epel/epel-release-latest-$DIST_VERSION.noarch.rpm"
    rpm -Uvh "$CACHEDIR/epel-release-latest-$DIST_VERSION.noarch.rpm"
fi
