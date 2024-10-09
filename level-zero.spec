#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
Name     : level-zero
Version  : 1.18.2
Release  : 35
URL      : https://github.com/oneapi-src/level-zero/archive/v1.18.2/level-zero-1.18.2.tar.gz
Source0  : https://github.com/oneapi-src/level-zero/archive/v1.18.2/level-zero-1.18.2.tar.gz
Source1  : https://github.com/gabime/spdlog/archive/refs/tags/v1.13.0.tar.gz
Summary  : Level Zero
Group    : Development/Tools
License  : MIT
Requires: level-zero-lib = %{version}-%{release}
Requires: level-zero-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : spdlog-dev
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
%setup -q -n level-zero-1.18.2
cd %{_builddir}
tar xf %{_sourcedir}/v1.13.0.tar.gz
cd %{_builddir}/level-zero-1.18.2
mkdir -p source/utils/spdlog
cp -r %{_builddir}/spdlog-1.13.0/* %{_builddir}/level-zero-1.18.2/source/utils/spdlog
pushd ..
cp -a level-zero-1.18.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728484853
mkdir -p clr-build
pushd clr-build
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
%cmake .. -DFETCHCONTENT_FULLY_DISCONNECTED=ON  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DFETCHCONTENT_FULLY_DISCONNECTED=ON  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

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
export SOURCE_DATE_EPOCH=1728484853
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/level-zero
cp %{_builddir}/level-zero-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/level-zero/6ec9ed37578702833be1af0c8089e57132b8a6bf || :
cp %{_builddir}/level-zero-%{version}/third_party/spdlog_headers/LICENSE %{buildroot}/usr/share/package-licenses/level-zero/bab970f85d9d9b485a36b93f8678fff4850d76fd || :
cp %{_builddir}/spdlog-1.13.0/LICENSE %{buildroot}/usr/share/package-licenses/level-zero/bab970f85d9d9b485a36b93f8678fff4850d76fd || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/V3/usr/lib64/libze_loader.so.1.18.2
/V3/usr/lib64/libze_tracing_layer.so.1.18.2
/V3/usr/lib64/libze_validation_layer.so.1.18.2
/usr/lib64/libze_loader.so.1
/usr/lib64/libze_loader.so.1.18.2
/usr/lib64/libze_tracing_layer.so.1
/usr/lib64/libze_tracing_layer.so.1.18.2
/usr/lib64/libze_validation_layer.so.1
/usr/lib64/libze_validation_layer.so.1.18.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/level-zero/6ec9ed37578702833be1af0c8089e57132b8a6bf
/usr/share/package-licenses/level-zero/bab970f85d9d9b485a36b93f8678fff4850d76fd
