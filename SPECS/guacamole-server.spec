# Supported targets: el8, el9
# Replace distro package with: dnf install guacamole-server16z --allowerasing

%if ! 0%{?make_build:1}
%define make_build %{__make} %{?_smp_mflags}
%endif

%global username guacd

%define ffmpeg_version      4.2.10
%define ffmpeg              ffmpeg-%{ffmpeg_version}

Name:           guacamole-server16z
Version:        1.6.0
Release:        1%{?dist}.zenetys
Summary:        Server-side native components that form the Guacamole proxy
License:        ASL 2.0
URL:            http://guac-dev.org/

Source0:        https://github.com/apache/guacamole-server/archive/%{version}.tar.gz#/guacamole-server-%{version}.tar.gz
Source1:        https://src.fedoraproject.org/rpms/guacamole-server/raw/5b6baa5c934b7698dc0d7c1b093eafcc6c0718f1/f/guacamole-server.sysconfig
Source2:        https://src.fedoraproject.org/rpms/guacamole-server/raw/5b6baa5c934b7698dc0d7c1b093eafcc6c0718f1/f/guacamole-server.service
Patch0:         https://github.com/apache/guacamole-server/commit/2e2a33621d673345e7b9d22c9388be80c6d77598.patch#/guacamole-1.6.0-GUACAMOLE-2070-Correct-usage-of-struct-sockaddr_in-s.patch

Source260:      https://ffmpeg.org/releases/%{ffmpeg}.tar.bz2
Patch261:       https://pkgs.rpmfusion.org/cgit/free/ffmpeg.git/plain/fix_ppc_build.patch?h=el8&id=4604cc7aed7b3fa49f50a7f7cdf35814d17c988e#/ffmpeg-fix_ppc_build.patch

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

BuildRequires:  pkgconfig(libvncserver)
%ifarch %{ix86} x86_64
BuildRequires:  nasm
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

# Make sure freerdp is up-to-date to avoid
# undefined symbol issues
Requires:       freerdp-libs >= 2:2.2.0

Provides:       guacd
Conflicts:      guacd
Provides:       libguac
Conflicts:      libguac
Provides:       libguac-client-kubernetes
Conflicts:      libguac-client-kubernetes
Provides:       libguac-client-rdp
Conflicts:      libguac-client-rdp
Provides:       libguac-client-ssh
Conflicts:      libguac-client-ssh
Provides:       libguac-client-telnet
Conflicts:      libguac-client-telnet
Provides:       libguac-client-vnc
Conflicts:      libguac-client-vnc

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
Conflicts:      libguac-devel

%description -n %{name}-devel
The libguac-devel package contains libraries and header files for
developing applications that use guacamole-server

%prep
# guacamole-server
%setup -n guacamole-server-%{version}
%patch0 -p1

# ffmpeg
%setup -T -D -a 260 -n guacamole-server-%{version}
cd %{ffmpeg}
%patch261 -p1
cd ..

%build
base_cflags="%{build_cflags}"
base_cxxflags="%{build_cxxflags}"
base_ldflags="%{build_ldflags}"

export CFLAGS="$base_cflags -fPIC"
export CXXFLAGS="$base_cxxflags -fPIC"
export LDFLAGS="$base_ldflags"
export AS=nasm
export PKG_CONFIG_PATH
guac_extra_cflags=
guac_extra_ldflags=
guac_extra_pkgconfig_path=
guac_extra_libs=

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
