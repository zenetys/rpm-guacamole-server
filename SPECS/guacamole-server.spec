# Supported targets: el7, el8, el9

%if ! 0%{?make_build:1}
%define make_build %{__make} %{?_smp_mflags}
%endif

%if 0%{?rhel} == 7
# debugedit (called by find-debuginfo.sh) fails on el7
# Failed to write file: invalid section alignment
%define debug_package %{nil}
%endif

%global username guacd

%if 0%{?rhel} <= 7
%define nasm_version        2.15.03
%define nasm                nasm-%{nasm_version}

%define libvnc_version      0.9.11
%define libvnc              libvncserver-LibVNCServer-%{libvnc_version}
%define libvnc_patch_url    https://git.rockylinux.org/staging/rpms/libvncserver/-/raw/imports/r8/libvncserver-%{libvnc_version}-17.el8/SOURCES
%endif

%define ffmpeg_version      4.2.9
%define ffmpeg              ffmpeg-%{ffmpeg_version}

Name:           guacamole-server15z
Version:        1.5.1
Release:        2%{?dist}.zenetys
Summary:        Server-side native components that form the Guacamole proxy
License:        ASL 2.0
URL:            http://guac-dev.org/

Source0:        https://github.com/apache/guacamole-server/archive/%{version}.tar.gz#/guacamole-server-%{version}.tar.gz
Source1:        https://src.fedoraproject.org/rpms/guacamole-server/raw/5b6baa5c934b7698dc0d7c1b093eafcc6c0718f1/f/guacamole-server.sysconfig
Source2:        https://src.fedoraproject.org/rpms/guacamole-server/raw/5b6baa5c934b7698dc0d7c1b093eafcc6c0718f1/f/guacamole-server.service

%if 0%{?rhel} <= 7
Source200:      https://www.nasm.us/pub/nasm/releasebuilds/%{nasm_version}/%{nasm}.tar.gz
%endif

Source260:      https://ffmpeg.org/releases/%{ffmpeg}.tar.bz2
Patch261:       https://pkgs.rpmfusion.org/cgit/free/ffmpeg.git/plain/fix_ppc_build.patch?h=el8&id=4604cc7aed7b3fa49f50a7f7cdf35814d17c988e#/ffmpeg-fix_ppc_build.patch

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
BuildRequires:  libgcrypt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(freerdp-client2)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libtelnet)

%if 0%{?rhel} >= 8
BuildRequires:  pkgconfig(libvncserver)
%ifarch %{ix86} x86_64
BuildRequires:  nasm
%endif
%endif

BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebsockets)
BuildRequires:  pkgconfig(ossp-uuid)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(winpr2)
BuildRequires:  systemd-devel

Requires(pre):  shadow-utils
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

Requires:       dejavu-sans-mono-fonts

# Make sure freerdp is up-to-date on el7 and el8 to avoid
# undefined symbol issues
%if 0%{?rhel} <= 7
Requires:       freerdp-libs >= 2.1.1
%else
Requires:       freerdp-libs >= 2:2.2.0
%endif

Provides:       guacd
Provides:       libguac
Provides:       libguac-client-kubernetes
Provides:       libguac-client-rdp
Provides:       libguac-client-ssh
Provides:       libguac-client-telnet
Provides:       libguac-client-vnc

Obsoletes:      guacd
Obsoletes:      libguac
Obsoletes:      libguac-client-kubernetes
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
%if 0%{?rhel} <= 7
base_cflags="%{optflags}"
base_cxxflags="%{optflags}"
base_ldflags="%{__global_ldflags}"
%else
base_cflags="%{build_cflags}"
base_cxxflags="%{build_cxxflags}"
base_ldflags="%{build_ldflags}"
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

ffmpeg_configure_opts=(
    --prefix=$PWD/build
    --arch='%{_target_cpu}'
    --disable-all
    --enable-avcodec
    --enable-avfilter
    --enable-avformat
    --enable-encoder=rawvideo,mpeg4
    --enable-ffmpeg
    --enable-filter=scale
    --enable-gpl
    --enable-muxer=rawvideo,mov,mp4,m4v
    --enable-pic
    --enable-protocol=file
    --enable-small
    --enable-static
    --enable-swresample
    --enable-swscale
    --x86asmexe="$AS"
)
%if 0%{?rhel} >= 9
ffmpeg_configure_opts+=( --enable-lto )
%endif

./configure "${ffmpeg_configure_opts[@]}"
%make_build
make install
guac_extra_pkgconfig_path+=":$PWD/build/lib/pkgconfig"
cd ..

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

cd doc/libguac
doxygen Doxyfile
cd ../..

cd doc/libguac-terminal
doxygen Doxyfile
cd ../..

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
mv doc/libguac/doxygen-output/html libguac
mv doc/libguac-terminal/doxygen-output/html libguac-terminal

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/guacd
mkdir -p %{buildroot}%{_sharedstatedir}/guacd

# Systemd unit files
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 -D %{SOURCE2} %{buildroot}%{_unitdir}/guacd.service

%pre
getent group %username >/dev/null || groupadd -r %username &>/dev/null || :
getent passwd %username >/dev/null || useradd -r -s /sbin/nologin \
    -d %{_sharedstatedir}/guacd -M -c 'Guacamole proxy daemon' -g %username %username &>/dev/null || :
exit 0

%post
/sbin/ldconfig
%systemd_post guacd.service
%preun
%systemd_preun guacd.service
%postun
/sbin/ldconfig
%systemd_postun_with_restart guacd.service

%files
%license LICENSE
%doc README CONTRIBUTING
%config(noreplace) %{_sysconfdir}/sysconfig/guacd
%{_libdir}/libguac.so.*

# The libguac source code dlopen's these plugins, and they are named without
# the version in the shared object; i.e. "libguac-client-$(PROTOCOL).so".
%{_libdir}/libguac-client-kubernetes.so
%{_libdir}/libguac-client-kubernetes.so.*
%{_libdir}/libguac-client-rdp.so
%{_libdir}/libguac-client-rdp.so.*
%{_libdir}/freerdp2/*.so
%{_libdir}/libguac-client-ssh.so
%{_libdir}/libguac-client-ssh.so.*
%{_libdir}/libguac-client-telnet.so
%{_libdir}/libguac-client-telnet.so.*
%{_libdir}/libguac-client-vnc.so
%{_libdir}/libguac-client-vnc.so.*
%{_libdir}/libguac-terminal.so
%{_libdir}/libguac-terminal.so.*

# attr set here, see note about el7 at the end of the install section
%attr(755,-,-) %{_bindir}/guacenc

%{_bindir}/guaclog
%{_mandir}/man1/guacenc.1.*
%{_mandir}/man1/guaclog.1.*
%{_mandir}/man5/guacd.conf.5.*
%{_mandir}/man8/guacd.8.*
%{_sbindir}/guacd
%{_unitdir}/guacd.service
%attr(750,%{username},%{username}) %{_sharedstatedir}/guacd

%files -n %{name}-devel
%doc libguac
%doc libguac-terminal
%{_includedir}/*
%{_libdir}/libguac.so
