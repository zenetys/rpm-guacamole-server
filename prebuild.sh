#!/bin/bash -xe

if [[ $DIST == el6 ]]; then
    # EPEL6: libwebp
    build_dl https://archives.fedoraproject.org/pub/archive/epel/6/x86_64/epel-release-6-8.noarch.rpm
    rpm -Uvh "$CACHEDIR/epel-release-6-8.noarch.rpm"
    # el6 EOL, use archive repositories
    sed -i -re 's,mirror\.centos\.org,vault.centos.org,; s,^(mirrorlist),#\1,; s,^#(baseurl),\1,' \
        /etc/yum.repos.d/CentOS-Base.repo

elif [[ $DIST_TYPE == el ]]; then
    # EPEL7: libtelnet, libuv, libwebsockets
    # EPEL8: libssh2
    build_dl "https://dl.fedoraproject.org/pub/epel/epel-release-latest-$DIST_VERSION.noarch.rpm"
    rpm -Uvh "$CACHEDIR/epel-release-latest-$DIST_VERSION.noarch.rpm"
fi
