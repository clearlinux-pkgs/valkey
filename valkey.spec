#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : valkey
Version  : 8.0.2
Release  : 7
URL      : https://github.com/valkey-io/valkey/archive/8.0.2/valkey-8.0.2.tar.gz
Source0  : https://github.com/valkey-io/valkey/archive/8.0.2/valkey-8.0.2.tar.gz
Summary  : Minimalistic C client library for Redis.
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause BSL-1.0 CC0-1.0 MIT
Requires: valkey-bin = %{version}-%{release}
Requires: valkey-data = %{version}-%{release}
Requires: valkey-license = %{version}-%{release}
Requires: valkey-services = %{version}-%{release}
BuildRequires : jemalloc-dev
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-use-system-jemalloc.patch
Patch2: 0001-Set-defaults-for-services-and-config.patch

%description
jemalloc is a general purpose malloc(3) implementation that emphasizes
fragmentation avoidance and scalable concurrency support.  jemalloc first came
into use as the FreeBSD libc allocator in 2005, and since then it has found its
way into numerous applications that rely on its predictable behavior.  In 2010
jemalloc development efforts broadened to include developer support features
such as heap profiling and extensive monitoring/tuning hooks.  Modern jemalloc
releases continue to be integrated back into FreeBSD, and therefore versatility
remains critical.  Ongoing development efforts trend toward making jemalloc
among the best allocators for a broad range of demanding applications, and
eliminating/mitigating weaknesses that have practical repercussions for real
world applications.

%package bin
Summary: bin components for the valkey package.
Group: Binaries
Requires: valkey-data = %{version}-%{release}
Requires: valkey-license = %{version}-%{release}
Requires: valkey-services = %{version}-%{release}

%description bin
bin components for the valkey package.


%package data
Summary: data components for the valkey package.
Group: Data

%description data
data components for the valkey package.


%package license
Summary: license components for the valkey package.
Group: Default

%description license
license components for the valkey package.


%package services
Summary: services components for the valkey package.
Group: Systemd services
Requires: systemd

%description services
services components for the valkey package.


%prep
%setup -q -n valkey-8.0.2
cd %{_builddir}/valkey-8.0.2
%patch -P 1 -p1
%patch -P 2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736299458
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}  USE_SYSTEMD=yes


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1736299458
rm -rf %{buildroot}
## install_prepend content
export PREFIX=%{buildroot}/usr
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/valkey
cp %{_builddir}/valkey-%{version}/COPYING %{buildroot}/usr/share/package-licenses/valkey/c0b860ad12443cd2a8155ddb339382f183250630 || :
cp %{_builddir}/valkey-%{version}/deps/fpconv/LICENSE.txt %{buildroot}/usr/share/package-licenses/valkey/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/valkey-%{version}/deps/hdr_histogram/COPYING.txt %{buildroot}/usr/share/package-licenses/valkey/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/valkey-%{version}/deps/hdr_histogram/LICENSE.txt %{buildroot}/usr/share/package-licenses/valkey/1f3f949bd5fdef93522f7eaad5a31dd1cca02ca1 || :
cp %{_builddir}/valkey-%{version}/deps/hiredis/COPYING %{buildroot}/usr/share/package-licenses/valkey/7408f21b00cacbde09347e67b394a5c893a23ba8 || :
cp %{_builddir}/valkey-%{version}/deps/jemalloc/COPYING %{buildroot}/usr/share/package-licenses/valkey/c797cef3f1b13a960a5119a084fb88529a924fd7 || :
cp %{_builddir}/valkey-%{version}/deps/lua/COPYRIGHT %{buildroot}/usr/share/package-licenses/valkey/a6efc4d11f332f4843bc25b557c6bf3e5ef51458 || :
export GOAMD64=v2
GOAMD64=v2
%make_install
## install_append content
install -Dm 0644 utils/systemd-valkey_multiple_servers@.service %{buildroot}/usr/lib/systemd/system/systemd-valkey_multiple_servers@.service
install -Dm 0644 utils/systemd-valkey_server.service %{buildroot}/usr/lib/systemd/system/systemd-valkey_server.service
install -Dm 0644 valkey.conf %{buildroot}/usr/share/defaults/etc/valkey.conf
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/redis-benchmark
/usr/bin/redis-check-aof
/usr/bin/redis-check-rdb
/usr/bin/redis-cli
/usr/bin/redis-sentinel
/usr/bin/redis-server
/usr/bin/valkey-benchmark
/usr/bin/valkey-check-aof
/usr/bin/valkey-check-rdb
/usr/bin/valkey-cli
/usr/bin/valkey-sentinel
/usr/bin/valkey-server

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/valkey.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/valkey/1f3f949bd5fdef93522f7eaad5a31dd1cca02ca1
/usr/share/package-licenses/valkey/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/valkey/7408f21b00cacbde09347e67b394a5c893a23ba8
/usr/share/package-licenses/valkey/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/valkey/a6efc4d11f332f4843bc25b557c6bf3e5ef51458
/usr/share/package-licenses/valkey/c0b860ad12443cd2a8155ddb339382f183250630
/usr/share/package-licenses/valkey/c797cef3f1b13a960a5119a084fb88529a924fd7

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/systemd-valkey_multiple_servers@.service
/usr/lib/systemd/system/systemd-valkey_server.service
