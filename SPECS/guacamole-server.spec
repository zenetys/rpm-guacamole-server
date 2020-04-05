%if ! 0%{?make_build:1}
%define make_build %{__make} %{?_smp_mflags}
%endif

%global username guacd

%if 0%{?rhel} >= 8
%define libssh2_version     1.9.0
%define libssh2             libssh2-%{libssh2_version}
%endif

%if 0%{?rhel} <= 6 || 0%{?rhel} >= 8
%define libtelnet_version   0.21
%define libtelnet           libtelnet-%{libtelnet_version}
%endif

%if 0%{?rhel} <= 7
%define nasm_version        2.13.03
%define nasm                nasm-%{nasm_version}
%endif

%if 0%{?rhel} <= 6
%define freerdp_version     2.0.0-rc4
%define freerdp             FreeRDP-%{freerdp_version}

%define libjpeg_version     1.5.3
%define libjpeg             libjpeg-turbo-%{libjpeg_version}
%endif

%define libx264_version     master-1771b556ee45207f8711744ccbd5d42a3949b14c
%define ffmpeg_version      4.2.2
%define libx264             x264-%{libx264_version}
%define ffmpeg              ffmpeg-%{ffmpeg_version}

Name:           guacamole-server
Version:        1.1.0
Release:        1%{?dist}
Epoch:          1
Summary:        Server-side native components that form the Guacamole proxy
License:        ASL 2.0
URL:            http://guac-dev.org/

Source0:        https://github.com/apache/guacamole-server/archive/%{version}.tar.gz#/guacamole-server-%{version}.tar.gz
Source1:        https://src.fedoraproject.org/rpms/guacamole-server/raw/5b6baa5c934b7698dc0d7c1b093eafcc6c0718f1/f/guacamole-server.sysconfig
%if 0%{?rhel} >= 7
Source2:        https://src.fedoraproject.org/rpms/guacamole-server/raw/5b6baa5c934b7698dc0d7c1b093eafcc6c0718f1/f/guacamole-server.service
%else
Source3:        https://src.fedoraproject.org/rpms/guacamole-server/raw/889f0f740e44ba6727e0db8b37bb2404fcbbe8ce/f/guacamole-server.init
Patch1:         guacamole-server-AC_REQUIRE_tap-driver.patch
%endif

%if 0%{?rhel} >= 8
Source100:      https://libssh2.org//download/%{libssh2}.tar.gz
Patch100:       https://src.fedoraproject.org/rpms/libssh2/raw/41525baf3f2396b61f9ea90591deb1eb178912bc/f/0001-libssh2-1.9.0-CVE-2019-17498.patch#/libssh2-CVE-2019-17498.patch
%endif

%if 0%{?rhel} <= 6 || 0%{?rhel} >= 8
Source150:      https://github.com/elanthis/libtelnet/archive/%{libtelnet_version}.tar.gz#/%{libtelnet}.tar.gz
Patch150:       libtelnet-AM-PROG-AR.patch
%endif

%if 0%{?rhel} <= 7
Source200:      https://www.nasm.us/pub/nasm/releasebuilds/%{nasm_version}/%{nasm}.tar.gz
Patch201:       https://git.centos.org/rpms/nasm/raw/2c880c9d584254e6fff2d6acabae431d17dac16b/f/SOURCES/0001-Remove-invalid-pure_func-qualifiers.patch#/nasm-Remove-invalid-pure_func-qualifiers.patch
%endif

Source230:      https://code.videolan.org/videolan/x264/-/archive/master/%{libx264}.tar.gz
Source260:      https://ffmpeg.org/releases/%{ffmpeg}.tar.bz2
Patch261:       https://pkgs.rpmfusion.org/cgit/free/ffmpeg.git/plain/fix_ppc_build.patch?h=el8&id=4604cc7aed7b3fa49f50a7f7cdf35814d17c988e#/ffmpeg-fix_ppc_build.patch

%if 0%{?rhel} <= 6
Source320:      https://github.com/FreeRDP/FreeRDP/archive/%{freerdp_version}/%{freerdp}.tar.gz
Source350:      https://downloads.sourceforge.net/libjpeg-turbo/%{libjpeg}.tar.gz
Patch350:       https://git.centos.org/rpms/libjpeg-turbo/raw/72e67db515b0b4d943c3bb8e6cf563d16817dd87/f/SOURCES/libjpeg-turbo14-noinst.patch#/libjpeg-turbo-noinst.patch
Patch351:       https://git.centos.org/rpms/libjpeg-turbo/raw/72e67db515b0b4d943c3bb8e6cf563d16817dd87/f/SOURCES/libjpeg-turbo-header-files.patch#/libjpeg-turbo-header-files.patch
Patch352:       https://git.centos.org/rpms/libjpeg-turbo/raw/72e67db515b0b4d943c3bb8e6cf563d16817dd87/f/SOURCES/libjpeg-turbo-CVE-2018-11813.patch#/libjpeg-turbo-CVE-2018-11813.patch
Patch353:       https://git.centos.org/rpms/libjpeg-turbo/raw/72e67db515b0b4d943c3bb8e6cf563d16817dd87/f/SOURCES/libjpeg-turbo-CVE-2018-1152.patch#/libjpeg-turbo-CVE-2018-1152.patch
Patch354:       https://git.centos.org/rpms/libjpeg-turbo/raw/72e67db515b0b4d943c3bb8e6cf563d16817dd87/f/SOURCES/libjpeg-turbo-honor-naflags.patch#/libjpeg-turbo-honor-naflags.patch
Patch355:       https://git.centos.org/rpms/libjpeg-turbo/raw/72e67db515b0b4d943c3bb8e6cf563d16817dd87/f/SOURCES/libjpeg-turbo-coverity.patch#/libjpeg-turbo-coverity.patch
Patch356:       https://git.centos.org/rpms/libjpeg-turbo/raw/72e67db515b0b4d943c3bb8e6cf563d16817dd87/f/SOURCES/libjpeg-turbo-CET.patch#/libjpeg-turbo-CET.patch
Patch357:       https://git.centos.org/rpms/libjpeg-turbo/raw/72e67db515b0b4d943c3bb8e6cf563d16817dd87/f/SOURCES/libjpeg-turbo-CVE-2018-14498.patch#/libjpeg-turbo-CVE-2018-14498.patch
Patch399:       libjpeg-turbo-freerdp-winpr-type-redef.patch
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(ossp-uuid)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(vorbis)

%if 0%{?rhel} >= 8
%ifarch %{ix86} x86_64
BuildRequires:  nasm
%endif
%endif

%if 0%{?rhel} >= 7
BuildRequires:  libjpeg-devel
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(freerdp-client2)
BuildRequires:  pkgconfig(winpr2)
%endif

%if 0%{?rhel} == 7
BuildRequires:  libwebsockets-devel
BuildRequires:  pkgconfig(libtelnet)
%endif

%if 0%{?rhel} <= 7
BuildRequires:  pkgconfig(libssh2)
%endif

%if 0%{?rhel} <= 6
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  gstreamer-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  gcc-c++
BuildRequires:  gsm-devel
BuildRequires:  pkgconfig(libpcsclite)
%endif

%if 0%{?rhel} <= 6
BuildRequires:  gnutls-devel
BuildRequires:  libvncserver-devel
%else
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libvncserver)
%endif

%description
Guacamole is an HTML5 remote desktop gateway.

Guacamole provides access to desktop environments using remote desktop protocols
like VNC and RDP. A centralized server acts as a tunnel and proxy, allowing
access to multiple desktops through a web browser.

No browser plugins are needed, and no client software needs to be installed. The
client requires nothing more than a web browser supporting HTML5 and AJAX.

The main web application is provided by the "guacamole-client" package.

%package -n libguac
Summary:        The common library used by all C components of Guacamole

%description -n libguac
libguac is the core library for guacd (the Guacamole proxy) and any protocol
support plugins for guacd. libguac provides efficient buffered I/O of text and
base64 data, as well as somewhat abstracted functions for sending Guacamole
instructions.

%package -n libguac-devel
Summary:        Development files for %{name}
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-devel
The libguac-devel package contains libraries and header files for
developing applications that use %{name}.

%if 0%{?rhel} == 7
%package -n libguac-client-kubernetes
Summary:        Kubernetes pods terminal support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-client-kubernetes
libguac-client-kubernetes is a protocol support plugin for the Guacamole proxy
(guacd) which provides support for attaching to terminals of containers running
in Kubernetes pods.
%endif

%package -n libguac-client-rdp
Summary:        RDP support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-client-rdp
libguac-client-rdp is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for RDP, the proprietary remote desktop protocol used by
Windows Remote Deskop / Terminal Services, via the libfreerdp library.

%package -n libguac-client-ssh
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:        SSH support for guacd

%description -n libguac-client-ssh
libguac-client-ssh is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for SSH, the secure shell.

%package -n libguac-client-vnc
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:        VNC support for guacd

%description -n libguac-client-vnc
libguac-client-vnc is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for VNC via the libvncclient library (part of
libvncserver).

%package -n libguac-client-telnet
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:        Telnet support for guacd

%description -n libguac-client-telnet
libguac-client-telnet is a protocol support plugin for the Guacamole proxy
(guacd) which provides support for Telnet via the libtelnet library.

%package -n guacd
Summary:        Proxy daemon for Guacamole
Requires(pre):  shadow-utils
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?rhel} >= 7
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd
%else
Requires(post):    /sbin/chkconfig
Requires(preun):   /sbin/chkconfig
Requires(preun):   /sbin/service
Requires(postun):  /sbin/service
%endif

%description -n guacd
guacd is the Guacamole proxy daemon used by the Guacamole web application and
framework to translate between arbitrary protocols and the Guacamole protocol.

%prep
# guacamole-server
%setup -q -n %{name}-%{version}
%if 0%{?rhel} <= 6
%patch1 -p1
%endif

%if 0%{?rhel} >= 8
# libssh2
%setup -T -D -a 100 -n %{name}-%{version}
cd %{libssh2}
%patch100 -p1
cd ..
%endif

%if 0%{?rhel} <= 6 || 0%{?rhel} >= 8
# libtelnet
%setup -T -D -a 150 -n %{name}-%{version}
%if 0%{?rhel} >= 8
cd %{libtelnet}
%patch150 -p1
cd ..
%endif
%endif

%if 0%{?rhel} <= 7
# nasm
%setup -T -D -a 200 -n %{name}-%{version}
cd %{nasm}
%patch201 -p1
cd ..
%endif

# x264
%setup -T -D -a 230 -n %{name}-%{version}
# ffmpeg
%setup -T -D -a 260 -n %{name}-%{version}
cd %{ffmpeg}
%patch261 -p1
cd ..

%if 0%{?rhel} <= 6
# freerdp
%setup -T -D -a 320 -n %{name}-%{version}
# libjpeg
%setup -T -D -a 350 -n %{name}-%{version}
cd %{libjpeg}
%patch350 -p1 -b .noinst
%patch351 -p1 -b .header-files
%patch352 -p1 -b .CVE-2018-11813
%patch353 -p1 -b .CVE-2018-1152
%patch354 -p1 -b .honor-naflags
%patch355 -p1 -b .coverity
%patch356 -p1 -b .CET
%patch357 -p1 -b .CVE-2018-14498
cd ..
%endif

%build
%if 0%{?rhel} >= 8
base_cflags="%{build_cflags}"
base_cxxflags="%{build_cxxflags}"
base_ldflags="%{build_ldflags}"
%else
%if 0%{?rhel} >= 7
base_cflags="%{optflags}"
base_cxxflags="%{optflags}"
base_ldflags="%{__global_ldflags}"
%else
base_cflags="%{optflags}"
base_cxxflags="%{optflags}"
base_ldflags="-Wl,-z,relro"  # no default ldflags in el6
%endif
%endif

export CFLAGS="$base_cflags -fPIC"
export CXXFLAGS="$base_cxxflags -fPIC"
export LDFLAGS="$base_ldflags"
export AS=nasm
export PKG_CONFIG_PATH
guac_extra_cflags=
guac_extra_ldflags=
guac_extra_pkgconfig_path=

%if 0%{?rhel} >= 8
# libssh2
cd %{libssh2}
%configure --enable-static --disable-shared
%make_build
guac_extra_cflags+=" -I$PWD/include"
guac_extra_ldflags+=" -L$PWD/src/.libs -lcrypto -lz"
cd ..
%endif

%if 0%{?rhel} <= 6 || 0%{?rhel} >= 8
# libtelnet
cd %{libtelnet}
autoreconf -vif
%configure --enable-static --disable-shared
%make_build
guac_extra_cflags+=" -I$PWD"
guac_extra_ldflags+=" -L$PWD/.libs"
cd ..
%endif

%if 0%{?rhel} <= 7
# nasm
cd %{nasm}
./configure
%make_build
AS="$PWD/nasm"
cd ..
%endif

# libx264
cd %{libx264}
./configure \
    --disable-avs \
    --disable-cli \
    --disable-ffms \
    --disable-gpac \
    --disable-gpl \
    --disable-lavf \
    --disable-lsmash \
    --disable-opencl \
    --disable-swscale \
    --enable-pic \
    --enable-static
%make_build
libx264_cflags="-I$PWD"
libx264_ldflags="-L$PWD -lpthread"
guac_extra_ldflags+=" $libx264_ldflags"
cd ..

# ffmpeg
cd %{ffmpeg}
./configure \
    --prefix=$PWD/build \
    --arch='%{_target_cpu}' \
    --disable-all \
    --enable-ffmpeg \
    --enable-avcodec \
    --enable-avformat \
    --enable-avfilter \
    --enable-decoder=h264 \
    --enable-demuxer=mov \
    --enable-encoder=rawvideo,libx264 \
    --enable-gpl \
    --enable-filter=scale \
    --enable-libx264 \
    --enable-muxer=rawvideo,mp4 \
    --enable-parser=h264 \
    --enable-pic \
    --enable-protocol=file \
    --enable-small \
    --enable-static \
    --enable-swresample \
    --enable-swscale \
    --extra-cflags="$libx264_cflags" \
    --extra-cxxflags="$libx264_cflags" \
    --extra-ldflags="$libx264_ldflags" \
    --x86asmexe="$AS"
%make_build
make install
guac_extra_pkgconfig_path+=":$PWD/build/lib/pkgconfig"
cd ..

%if 0%{?rhel} <= 6
# libjpeg
cd %{libjpeg}
autoreconf -vif
(
    export NAFLAGS="-g -Fdwarf"
    export CCASFLAGS="-Wa,--generate-missing-build-notes=yes"
    export NASM="$AS"
    # NASM object files are missing GNU Property note for Intel CET,
    # force it on the resulting library
    %ifarch %{ix86} x86_64
    export LDFLAGS="$base_ldflags -Wl,-z,ibt -Wl,-z,shstk"
    %endif
    ./configure --prefix=$PWD/install --enable-static --disable-shared
)
%make_build
make install
guac_extra_cflags+=" -I$PWD/install/include"
guac_extra_ldflags+=" -L$PWD/install/lib"
cd ..

# freerdp
cd %{freerdp}
mkdir build install
cp -a ../%{libjpeg}/install/include libjpeg_include
patch -d libjpeg_include -p0 < %{PATCH399}
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=OFF \
    -DWITH_ALSA=ON \
    -DWITH_CHANNELS=ON \
        -DBUILTIN_CHANNELS=OFF \
    -DWITH_CLIENT=ON \
    -DWITH_CUPS=ON \
    -DWITH_DIRECTFB=OFF \
    -DWITH_FFMPEG=OFF \
    -DWITH_GSM=ON \
    -DWITH_GSSAPI=OFF \
    -DWITH_GSTREAMER_1_0=OFF \
    -DWITH_GSTREAMER_0_10=ON \
        -DGSTREAMER_0_10_INCLUDE_DIRS=/usr/include/gstreamer-0.10 \
    -DWITH_IPP=OFF \
    -DWITH_JPEG=ON \
        -DJPEG_LIBRARY=$PWD/../../%{libjpeg}/install/lib/libturbojpeg.a \
        -DJPEG_INCLUDE_DIR=$PWD/../libjpeg_include \
    -DWITH_LIBSYSTEMD=OFF \
    -DWITH_MANPAGES=OFF \
    -DWITH_OPENH264=OFF \
    -DWITH_OPENSSL=ON \
    -DWITH_PCSC=ON \
    -DWITH_PULSE=ON \
    -DWITH_SERVER_INTERFACE=OFF \
    -DWITH_SERVER=OFF \
    -DWITH_SHADOW_MAC=OFF \
    -DWITH_SHADOW_X11=OFF \
    -DWITH_SSE2=ON \
    -DWITH_WAYLAND=OFF \
    -DWITH_X11=OFF \
    -DWITH_X264=OFF \
    -DWITH_ZLIB=ON \
    ..
%make_build
make install DESTDIR=$PWD/../install
cd ..
# Workaround symbol conflict with Guacamole during linking.
objcopy --localize-symbol=RSA_get0_key "$PWD/install/usr/%{_lib}/libfreerdp2.a"
export RDP_CFLAGS="-I$PWD/install/usr/include/freerdp2 -I$PWD/install/usr/include/winpr2"
export RDP_LIBS="-L$PWD/install/usr/%{_lib}"
cd ..
%endif

# guacamole-server
CFLAGS+=" $guac_extra_cflags"
LDFLAGS+=" $guac_extra_ldflags"
PKG_CONFIG_PATH+="$guac_extra_pkgconfig_path"

autoreconf -vif
%configure \
    --with-freerdp-plugin-dir="%{_libdir}/freerdp2" \
    --disable-silent-rules \
    --disable-static
%make_build
cd doc/
doxygen Doxyfile

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
cp -fr doc/doxygen-output/html .
%if 0%{?rhel} <= 6
rm -f html/installdox
%endif

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/guacd
mkdir -p %{buildroot}%{_sharedstatedir}/guacd

%if 0%{?rhel} >= 7
# Systemd unit files
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 -D %{SOURCE2} %{buildroot}%{_unitdir}/guacd.service
%else
install -p -m 755 -D %{SOURCE3} %{buildroot}%{_initrddir}/guacd
%endif

%if 0%{?rhel} == 7
# Although it seams to run fine, there is an issue with this binary,
# debugedit (called by find-debuginfo.sh) returns an error "invalid section
# alignment". Other tools like readelf also emit warnings.
# This chmod trick allows to exclude the binary from the debuginfo package.
# Proper mode it set back in the %file section.
chmod 644 %{buildroot}%{_bindir}/guacenc
%endif

%pre -n guacd
getent group %username >/dev/null || groupadd -r %username &>/dev/null || :
getent passwd %username >/dev/null || useradd -r -s /sbin/nologin \
    -d %{_sharedstatedir}/guacd -M -c 'Guacamole proxy daemon' -g %username %username &>/dev/null || :
exit 0

%if 0%{?rhel} >= 7
%post -n guacd
%systemd_post guacd.service
%preun -n guacd
%systemd_preun guacd.service
%postun -n guacd
%systemd_postun_with_restart guacd.service
%else
%post -n guacd
/sbin/chkconfig --add guacd
%preun -n guacd
if [ "$1" = 0 ]; then
    /sbin/service guacd stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del guacd
fi
%postun -n guacd
if [ "$1" -ge "1" ]; then
    /sbin/service guacd condrestart >/dev/null 2>&1 || :
fi
%endif

%ldconfig_scriptlets -n libguac
%if 0%{?rhel} == 7
%ldconfig_scriptlets -n libguac-client-kubernetes
%endif
%ldconfig_scriptlets -n libguac-client-rdp
%ldconfig_scriptlets -n libguac-client-ssh
%ldconfig_scriptlets -n libguac-client-vnc
%ldconfig_scriptlets -n libguac-client-telnet

%files -n libguac
%if 0%{?rhel} >= 7
%license LICENSE
%else
%doc LICENSE
%endif
%doc README CONTRIBUTING
%{_libdir}/libguac.so.*

%files -n libguac-devel
%doc html
%{_includedir}/*
%{_libdir}/libguac.so

# The libguac source code dlopen's these plugins, and they are named without
# the version in the shared object; i.e. "libguac-client-$(PROTOCOL).so".

%if 0%{?rhel} == 7
%files -n libguac-client-kubernetes
%{_libdir}/libguac-client-kubernetes.so
%{_libdir}/libguac-client-kubernetes.so.*
%endif

%files -n libguac-client-rdp
%{_libdir}/libguac-client-rdp.so
%{_libdir}/libguac-client-rdp.so.*
%{_libdir}/freerdp2/*.so

%files -n libguac-client-ssh
%{_libdir}/libguac-client-ssh.so
%{_libdir}/libguac-client-ssh.so.*

%files -n libguac-client-vnc
%{_libdir}/libguac-client-vnc.so
%{_libdir}/libguac-client-vnc.so.*

%files -n libguac-client-telnet
%{_libdir}/libguac-client-telnet.so
%{_libdir}/libguac-client-telnet.so.*

%files -n guacd
%config(noreplace) %{_sysconfdir}/sysconfig/guacd

# attr set here, see note about el7 at the end of the install section
%attr(755,-,-) %{_bindir}/guacenc

%{_bindir}/guaclog
%{_mandir}/man1/guacenc.1.*
%{_mandir}/man1/guaclog.1.*
%{_mandir}/man5/guacd.conf.5.*
%{_mandir}/man8/guacd.8.*
%{_sbindir}/guacd
%if 0%{?rhel} >= 7
%{_unitdir}/guacd.service
%else
%{_initrddir}/guacd
%endif
%attr(750,%{username},%{username}) %{_sharedstatedir}/guacd

%files -n %{name}-devel
%doc html
%{_includedir}/*
%{_libdir}/libguac.so
