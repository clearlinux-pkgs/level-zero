#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : level-zero
Version  : 1.9.9
Release  : 8
URL      : https://github.com/oneapi-src/level-zero/archive/v1.9.9/level-zero-1.9.9.tar.gz
Source0  : https://github.com/oneapi-src/level-zero/archive/v1.9.9/level-zero-1.9.9.tar.gz
Summary  : Level Zero
Group    : Development/Tools
License  : MIT
Requires: level-zero-lib = %{version}-%{release}
Requires: level-zero-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : git
BuildRequires : glibc-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# oneAPI Level Zero
This repository contains the following components of oneAPI:

%package dev
Summary: dev components for the level-zero package.
Group: Development
Requires: level-zero-lib = %{version}-%{release}
Provides: level-zero-devel = %{version}-%{release}
Requires: level-zero = %{version}-%{release}

%description dev
dev components for the level-zero package.


%package lib
Summary: lib components for the level-zero package.
Group: Libraries
Requires: level-zero-license = %{version}-%{release}

%description lib
lib components for the level-zero package.


%package license
Summary: license components for the level-zero package.
Group: Default

%description license
license components for the level-zero package.


%prep
%setup -q -n level-zero-1.9.9
cd %{_builddir}/level-zero-1.9.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678285089
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1678285089
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/level-zero
cp %{_builddir}/level-zero-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/level-zero/6ec9ed37578702833be1af0c8089e57132b8a6bf || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/level_zero/layers/zel_tracing_api.h
/usr/include/level_zero/layers/zel_tracing_ddi.h
/usr/include/level_zero/layers/zel_tracing_register_cb.h
/usr/include/level_zero/loader/ze_loader.h
/usr/include/level_zero/ze_api.h
/usr/include/level_zero/ze_ddi.h
/usr/include/level_zero/zes_api.h
/usr/include/level_zero/zes_ddi.h
/usr/include/level_zero/zet_api.h
/usr/include/level_zero/zet_ddi.h
/usr/lib64/libze_loader.so
/usr/lib64/libze_tracing_layer.so
/usr/lib64/libze_validation_layer.so
/usr/lib64/pkgconfig/level-zero.pc
/usr/lib64/pkgconfig/libze_loader.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libze_loader.so.1
/usr/lib64/libze_loader.so.1.9.0
/usr/lib64/libze_tracing_layer.so.1
/usr/lib64/libze_tracing_layer.so.1.9.0
/usr/lib64/libze_validation_layer.so.1
/usr/lib64/libze_validation_layer.so.1.9.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/level-zero/6ec9ed37578702833be1af0c8089e57132b8a6bf
