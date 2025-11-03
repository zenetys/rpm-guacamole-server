#!/bin/bash -xe

if [[ $DIST_TYPE == el && $DIST_VERSION =~ ^(8|9|10)$ ]]; then
    # EPEL8: libssh2-devel, libtelnet-devel, libwebsockets-devel
    # EPEL9: libssh2-devel, libtelnet-devel, libvncserver-devel, libwebsockets-devel
    # EPEL10: freerdp2-devel, libssh2-devel, libtelnet-devel, libvncserver-devel, libwebsockets-devel, libwinpr2-devel
    build_dl "https://dl.fedoraproject.org/pub/epel/epel-release-latest-$DIST_VERSION.noarch.rpm"
    rpm -Uvh "$CACHEDIR/epel-release-latest-$DIST_VERSION.noarch.rpm"
else
    echo "FATAL: Unsupported build target, DIST=$DIST"
    exit 2
fi
