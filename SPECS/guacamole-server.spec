%if ! 0%{?make_build:1}
%define make_build %{__make} %{?_smp_mflags}
%endif

%if 0%{?rhel} == 7
# debugedit (called by find-debuginfo.sh) fails on el7
# Failed to write file: invalid section alignment
%define debug_package %{nil}
%endif

%global username guacd

%if 0%{?rhel} <= 6 || 0%{?rhel} >= 8
%define libtelnet_version   0.23
%define libtelnet           libtelnet-%{libtelnet_version}
%endif

%if 0%{?rhel} <= 7
%define nasm_version        2.15.03
%define nasm                nasm-%{nasm_version}

%define libvnc_version      0.9.11
%define libvnc              libvncserver-LibVNCServer-%{libvnc_version}
%define libvnc_patch_url    https://git.rockylinux.org/staging/rpms/libvncserver/-/raw/imports/r8/libvncserver-%{libvnc_version}-17.el8/SOURCES
%endif

%if 0%{?rhel} <= 6
%define freerdp_version     2.2.0
%define freerdp             FreeRDP-%{freerdp_version}
%define freerdp_patch_url   https://git.rockylinux.org/staging/rpms/freerdp/-/raw/imports/r8/freerdp-%{freerdp_version}-7.el8_5/SOURCES

%define libjpeg_version     1.5.3
%define libjpeg             libjpeg-turbo-%{libjpeg_version}
%define libjpeg_patch_url   https://git.rockylinux.org/staging/rpms/libjpeg-turbo/-/raw/imports/r8/libjpeg-turbo-%{libjpeg_version}-12.el8/SOURCES
%endif

%define ffmpeg_version      4.2.6
%define ffmpeg              ffmpeg-%{ffmpeg_version}

Name:           guacamole-server14z
Version:        1.4.0
Release:        4%{?dist}.zenetys
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
Patch2:         guacamole-server-init.patch
%endif

%if 0%{?rhel} <= 6 || 0%{?rhel} >= 8
Source150:      https://github.com/seanmiddleditch/libtelnet/archive/%{libtelnet_version}.tar.gz#/%{libtelnet}.tar.gz
Patch150:       libtelnet-AM-PROG-AR.patch
%endif

%if 0%{?rhel} <= 7
Source200:      https://www.nasm.us/pub/nasm/releasebuilds/%{nasm_version}/%{nasm}.tar.gz
%endif

Source260:      https://ffmpeg.org/releases/%{ffmpeg}.tar.bz2
Patch261:       https://pkgs.rpmfusion.org/cgit/free/ffmpeg.git/plain/fix_ppc_build.patch?h=el8&id=4604cc7aed7b3fa49f50a7f7cdf35814d17c988e#/ffmpeg-fix_ppc_build.patch

%if 0%{?rhel} <= 6
Source320:      https://github.com/FreeRDP/FreeRDP/archive/%{freerdp_version}/%{freerdp}.tar.gz
Patch320:       %freerdp_patch_url/6741.patch#/freerdp-6741.patch
Patch321:       %freerdp_patch_url/Add-checks-for-bitmap-and-glyph-width-heigth-values.patch#/freerdp-Add-checks-for-bitmap-and-glyph-width-heigth-values.patch
Patch322:       %freerdp_patch_url/Implement-missing-TSG-debug-functions.patch#/freerdp-Implement-missing-TSG-debug-functions.patch
Patch323:       %freerdp_patch_url/Refactored-RPC-gateway-parser.patch#/freerdp-Refactored-RPC-gateway-parser.patch

Source350:      https://downloads.sourceforge.net/libjpeg-turbo/%{libjpeg}.tar.gz
Patch350:       %libjpeg_patch_url/libjpeg-turbo14-noinst.patch#/libjpeg-turbo-noinst.patch
Patch351:       %libjpeg_patch_url/libjpeg-turbo-header-files.patch#/libjpeg-turbo-header-files.patch
Patch352:       %libjpeg_patch_url/libjpeg-turbo-CVE-2018-11813.patch#/libjpeg-turbo-CVE-2018-11813.patch
Patch353:       %libjpeg_patch_url/libjpeg-turbo-CVE-2018-1152.patch#/libjpeg-turbo-CVE-2018-1152.patch
Patch354:       %libjpeg_patch_url/libjpeg-turbo-honor-naflags.patch#/libjpeg-turbo-honor-naflags.patch
Patch355:       %libjpeg_patch_url/libjpeg-turbo-coverity.patch#/libjpeg-turbo-coverity.patch
Patch356:       %libjpeg_patch_url/libjpeg-turbo-CET.patch#/libjpeg-turbo-CET.patch
Patch357:       %libjpeg_patch_url/libjpeg-turbo-CVE-2018-14498.patch#/libjpeg-turbo-CVE-2018-14498.patch
Patch358:       %libjpeg_patch_url/libjpeg-turbo-CVE-2020-17541.patch#/libjpeg-turbo-CVE-2020-17541.patch
Patch399:       libjpeg-turbo-freerdp-winpr-type-redef.patch
%endif

%if 0%{?rhel} <= 7
Source400:      https://github.com/LibVNC/libvncserver/archive/LibVNCServer-%{libvnc_version}.tar.gz
Patch400:       %libvnc_patch_url/0040-Ensure-compatibility-with-gtk-vnc-0.7.0.patch#/libvncserver-Ensure-compatibility-with-gtk-vnc-0.7.0.patch
Patch401:       %libvnc_patch_url/0001-libvncserver-Add-API-to-add-custom-I-O-entry-points.patch#/libvncserver-Add-API-to-add-custom-I-O-entry-points.patch
Patch402:       %libvnc_patch_url/0002-libvncserver-Add-channel-security-handlers.patch#/libvncserver-Add-channel-security-handlers.patch
Patch403:       %libvnc_patch_url/0001-auth-Add-API-to-unregister-built-in-security-handler.patch#/libvncserver-auth-Add-API-to-unregister-built-in-security-handler.patch
Patch404:       %libvnc_patch_url/libvncserver-0.9.11-system_minilzo.patch#/libvncserver-system_minilzo.patch
Patch405:       %libvnc_patch_url/libvncserver-0.9.1-multilib.patch#/libvncserver-multilib.patch
Patch407:       %libvnc_patch_url/libvncserver-0.9.11-Validate-client-cut-text-length.patch#/libvncserver-Validate-client-cut-text-length.patch
Patch408:       %libvnc_patch_url/libvncserver-0.9.11-Limit-client-cut-text-length-to-1-MB.patch#/libvncserver-Limit-client-cut-text-length-to-1-MB.patch
Patch409:       %libvnc_patch_url/libvncserver-0.9.11-Fix-CVE-2018-15127-Heap-out-of-bounds-write-in-rfbse.patch#/libvncserver-Fix-CVE-2018-15127-Heap-out-of-bounds-write-in-rfbse.patch
Patch410:       %libvnc_patch_url/libvncserver-0.9.11-libvncclient-cursor-limit-width-height-input-values.patch#/libvncserver-cursor-limit-width-height-input-values.patch
Patch411:       %libvnc_patch_url/libvncserver-0.9.11-CVE-2017-18922.patch
Patch412:       %libvnc_patch_url/libvncserver-0.9.11-CVE-2019-20840.patch
Patch413:       %libvnc_patch_url/libvncserver-0.9.11-CVE-2019-20839.patch
Patch414:       %libvnc_patch_url/libvncserver-0.9.11-CVE-2018-21247.patch
Patch415:       %libvnc_patch_url/libvncserver-0.9.11-CVE-2020-14405.patch
Patch416:       %libvnc_patch_url/libvncserver-0.9.11-CVE-2020-14397.patch
Patch417:       %libvnc_patch_url/libvncserver-0.9.11-CVE-2020-25708.patch
# Patch LibVNCServer-0.9.10-system-crypto-policy.patch is not included
# because @KEYWORD style priority strings are not supported either by
# the version of gnutls (el6) or by the distro (el7).
# Patch libvncserver-0.9.11-soname.patch is not included because we only
# build the library to link it statically with guacamole.
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(ossp-uuid)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(vorbis)

%if 0%{?rhel} >= 8
BuildRequires:  pkgconfig(libvncserver)
%ifarch %{ix86} x86_64
BuildRequires:  nasm
%endif
%endif

%if 0%{?rhel} >= 7
BuildRequires:  libgcrypt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(freerdp-client2)
BuildRequires:  pkgconfig(winpr2)
%endif

%if 0%{?rhel} == 7
BuildRequires:  libwebsockets-devel
BuildRequires:  lzo-devel
BuildRequires:  pkgconfig(libtelnet)
%endif

%if 0%{?rhel} <= 6
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  gstreamer-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  gcc-c++
BuildRequires:  gsm-devel
BuildRequires:  lzo-devel
BuildRequires:  pkgconfig(libpcsclite)
%endif

%if 0%{?rhel} <= 6
BuildRequires:  gnutls-devel
%else
BuildRequires:  pkgconfig(gnutls)
%endif

Requires(pre):  shadow-utils

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

Requires:       dejavu-sans-mono-fonts

# Make sure freerdp is up-to-date on el7 and el8 to avoid
# undefined symbol issues
%if 0%{?rhel} >= 8
Requires:       freerdp-libs >= 2:2.2.0
%else
%if 0%{?rhel} >= 7
Requires:       freerdp-libs >= 2.1.1
%endif
%endif

Provides:       guacd
Provides:       libguac
%if 0%{?rhel} == 7
Provides:       libguac-client-kubernetes
%endif
Provides:       libguac-client-rdp
Provides:       libguac-client-ssh
Provides:       libguac-client-telnet
Provides:       libguac-client-vnc

Obsoletes:      guacd
Obsoletes:      libguac
%if 0%{?rhel} == 7
Obsoletes:      libguac-client-kubernetes
%endif
Obsoletes:      libguac-client-rdp
Obsoletes:      libguac-client-ssh
Obsoletes:      libguac-client-telnet
Obsoletes:      libguac-client-vnc

%description
Guacamole is an HTML5 remote desktop gateway.

Guacamole provides access to desktop environments using remote desktop protocols
like VNC and RDP. A centralized server acts as a tunnel and proxy, allowing
access to multiple desktops through a web browser.

No browser plugins are needed, and no client software needs to be installed. The
client requires nothing more than a web browser supporting HTML5 and AJAX.

The main web application is provided by the "guacamole-client" package.

%package -n %{name}-devel
Summary:        Development files for guacamole-server
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       libguac-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{name}-devel
The libguac-devel package contains libraries and header files for
developing applications that use guacamole-server

%prep
# guacamole-server
%setup -n guacamole-server-%{version}
%if 0%{?rhel} <= 6
%patch1 -p1
%endif

%if 0%{?rhel} <= 6 || 0%{?rhel} >= 8
# libtelnet
%setup -T -D -a 150 -n guacamole-server-%{version}
%if 0%{?rhel} <= 8
cd %{libtelnet}
%patch150 -p1
cd ..
%endif
%endif

%if 0%{?rhel} <= 7
# nasm
%setup -T -D -a 200 -n guacamole-server-%{version}
cd %{nasm}
# nasm patches
cd ..
%endif

# ffmpeg
%setup -T -D -a 260 -n guacamole-server-%{version}
cd %{ffmpeg}
%patch261 -p1
cd ..

%if 0%{?rhel} <= 6
# freerdp
%setup -T -D -a 320 -n guacamole-server-%{version}
cd %{freerdp}
%patch320 -p1
%patch321 -p1
%patch322 -p1
%patch323 -p1
cd ..
# libjpeg
%setup -T -D -a 350 -n guacamole-server-%{version}
cd %{libjpeg}
%patch350 -p1 -b .noinst
%patch351 -p1 -b .header-files
%patch352 -p1 -b .CVE-2018-11813
%patch353 -p1 -b .CVE-2018-1152
%patch354 -p1 -b .honor-naflags
%patch355 -p1 -b .coverity
%patch356 -p1 -b .CET
%patch357 -p1 -b .CVE-2018-14498
%patch358 -p1 -b .CVE-2020-17541
%endif
%if 0%{?rhel} <= 7
# libvnc
%setup -T -D -a 400 -n guacamole-server-%{version}
cd %{libvnc}
%patch400 -p1
%patch401 -p1
%patch402 -p1
%patch403 -p1
%patch404 -p1
%patch405 -p1
%patch407 -p1
%patch408 -p1
%patch409 -p1
%patch410 -p1
%patch411 -p1
%patch412 -p1
%patch413 -p1
%patch414 -p1
%patch415 -p1
%patch416 -p1
%patch417 -p1
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
guac_extra_libs=

%if 0%{?rhel} <= 6 || 0%{?rhel} >= 8
# libtelnet
cd %{libtelnet}
autoreconf -vif
%configure --enable-static --disable-shared
%make_build
guac_extra_cflags+=" -I$PWD"
guac_extra_ldflags+=" -L$PWD/.libs"
guac_extra_libs+=" -lz"
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

# ffmpeg
cd %{ffmpeg}
./configure \
    --prefix=$PWD/build \
    --arch='%{_target_cpu}' \
    --disable-all \
    --enable-avcodec \
    --enable-avfilter \
    --enable-avformat \
    --enable-encoder=rawvideo,mpeg4 \
    --enable-ffmpeg \
    --enable-filter=scale \
    --enable-gpl \
    --enable-muxer=rawvideo,mov,mp4,m4v \
    --enable-pic \
    --enable-protocol=file \
    --enable-small \
    --enable-static \
    --enable-swresample \
    --enable-swscale \
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
    export LDFLAGS+=" -Wl,-z,ibt -Wl,-z,shstk"
    %endif
    ./configure --prefix=$PWD/install --enable-static --disable-shared
)
%make_build
make install
libjpeg_cflags="-I$PWD/install/include"
libjpeg_ldflags="-L$PWD/install/lib"
guac_extra_cflags+=" $libjpeg_cflags"
guac_extra_ldflags+=" $libjpeg_ldflags"
guac_extra_libs+=" -ljpeg"
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
        -DCHANNEL_URBDRC=OFF \
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
guac_extra_ldflags+=" -L$PWD/install/usr/%{_lib} -L$PWD/install/usr/%{_lib}/freerdp2"
guac_extra_ldflags+=" -lrt -lfreerdp-client2 -lfreerdp2 -lwinpr2"
for l in $PWD/install/usr/%{_lib}/freerdp2/*.a; do
    l=${l##*/}; l=${l#lib}; l=${l%.a}
    guac_extra_ldflags+=" -l$l"
done
cd ..
%endif

%if 0%{?rhel} <= 7
# libvnc
cd %{libvnc}
autoreconf -vif
(
    CFLAGS+=${libjpeg_cflags:+" $libjpeg_cflags"}
    LDFLAGS+=${libjpeg_ldflags:+" $libjpeg_ldflags"}
    export JPEG_LDFLAGS="-ljpeg"
    ./configure \
        --prefix=$PWD/install \
        --enable-static \
        --disable-shared \
        --with-gcrypt \
        --with-png
)
%make_build
make install
guac_extra_cflags+=" -I$PWD/install/include"
guac_extra_ldflags+=" -L$PWD/install/lib -lgnutls"
%if 0%{?rhel} == 7
guac_extra_ldflags+=" -lz -ljpeg -lgcrypt"
%endif
guac_extra_libs+=" -lminilzo"
cd ..
%endif

# guacamole-server
CFLAGS+=" $guac_extra_cflags"
LDFLAGS+=" $guac_extra_ldflags"
PKG_CONFIG_PATH+="$guac_extra_pkgconfig_path"
export LIBS="$guac_extra_libs"

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
patch -p0 %{buildroot}%{_initrddir}/guacd %{PATCH2}
mkdir -p %{buildroot}%{_var}/run/guacd
%endif

%pre
getent group %username >/dev/null || groupadd -r %username &>/dev/null || :
getent passwd %username >/dev/null || useradd -r -s /sbin/nologin \
    -d %{_sharedstatedir}/guacd -M -c 'Guacamole proxy daemon' -g %username %username &>/dev/null || :
exit 0

%if 0%{?rhel} >= 7
%post
/sbin/ldconfig
%systemd_post guacd.service
%preun
%systemd_preun guacd.service
%postun
/sbin/ldconfig
%systemd_postun_with_restart guacd.service
%else
%post
/sbin/ldconfig
/sbin/chkconfig --add guacd
%preun
if [ "$1" = 0 ]; then
    /sbin/service guacd stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del guacd
fi
%postun
/sbin/ldconfig
if [ "$1" -ge "1" ]; then
    /sbin/service guacd condrestart >/dev/null 2>&1 || :
fi
%endif

%files
%if 0%{?rhel} >= 7
%license LICENSE
%else
%doc LICENSE
%endif
%doc README CONTRIBUTING
%config(noreplace) %{_sysconfdir}/sysconfig/guacd
%{_libdir}/libguac.so.*

# The libguac source code dlopen's these plugins, and they are named without
# the version in the shared object; i.e. "libguac-client-$(PROTOCOL).so".
%if 0%{?rhel} == 7
%{_libdir}/libguac-client-kubernetes.so
%{_libdir}/libguac-client-kubernetes.so.*
%endif
%{_libdir}/libguac-client-rdp.so
%{_libdir}/libguac-client-rdp.so.*
%{_libdir}/freerdp2/*.so
%{_libdir}/libguac-client-ssh.so
%{_libdir}/libguac-client-ssh.so.*
%{_libdir}/libguac-client-telnet.so
%{_libdir}/libguac-client-telnet.so.*
%{_libdir}/libguac-client-vnc.so
%{_libdir}/libguac-client-vnc.so.*

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
%attr(755,%{username},%{username}) %{_var}/run/guacd
%endif
%attr(750,%{username},%{username}) %{_sharedstatedir}/guacd

%files -n %{name}-devel
%doc html
%{_includedir}/*
%{_libdir}/libguac.so
