#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkmahjongg
Version  : 23.08.3
Release  : 60
URL      : https://download.kde.org/stable/release-service/23.08.3/src/libkmahjongg-23.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.3/src/libkmahjongg-23.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.3/src/libkmahjongg-23.08.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0
Requires: libkmahjongg-data = %{version}-%{release}
Requires: libkmahjongg-lib = %{version}-%{release}
Requires: libkmahjongg-license = %{version}-%{release}
Requires: libkmahjongg-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains the library used for loading and rendering of Mahjongg tilesets and associated backgrounds, used by KMahjongg and KShisen.
Shared data is installed to {kdedir}/share/apps/kmahjongglib/*

%package data
Summary: data components for the libkmahjongg package.
Group: Data

%description data
data components for the libkmahjongg package.


%package dev
Summary: dev components for the libkmahjongg package.
Group: Development
Requires: libkmahjongg-lib = %{version}-%{release}
Requires: libkmahjongg-data = %{version}-%{release}
Provides: libkmahjongg-devel = %{version}-%{release}
Requires: libkmahjongg = %{version}-%{release}

%description dev
dev components for the libkmahjongg package.


%package lib
Summary: lib components for the libkmahjongg package.
Group: Libraries
Requires: libkmahjongg-data = %{version}-%{release}
Requires: libkmahjongg-license = %{version}-%{release}

%description lib
lib components for the libkmahjongg package.


%package license
Summary: license components for the libkmahjongg package.
Group: Default

%description license
license components for the libkmahjongg package.


%package locales
Summary: locales components for the libkmahjongg package.
Group: Default

%description locales
locales components for the libkmahjongg package.


%prep
%setup -q -n libkmahjongg-23.08.3
cd %{_builddir}/libkmahjongg-23.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702018136
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
%cmake ..
make  %{?_smp_mflags}
popd
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
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
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
export SOURCE_DATE_EPOCH=1702018136
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkmahjongg
cp %{_builddir}/libkmahjongg-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/libkmahjongg/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/libkmahjongg-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libkmahjongg/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libkmahjongg-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libkmahjongg/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/libkmahjongg-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkmahjongg/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang libkmahjongg5
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kmahjongglib/backgrounds/chinese_landscape.copyright
/usr/share/kmahjongglib/backgrounds/chinese_landscape.desktop
/usr/share/kmahjongglib/backgrounds/chinese_landscape.svgz
/usr/share/kmahjongglib/backgrounds/color_plain.desktop
/usr/share/kmahjongglib/backgrounds/default.copyright
/usr/share/kmahjongglib/backgrounds/default.desktop
/usr/share/kmahjongglib/backgrounds/default.svgz
/usr/share/kmahjongglib/backgrounds/egyptian.copyright
/usr/share/kmahjongglib/backgrounds/egyptian.desktop
/usr/share/kmahjongglib/backgrounds/egyptian.svgz
/usr/share/kmahjongglib/backgrounds/summerfield.copyright
/usr/share/kmahjongglib/backgrounds/summerfield.desktop
/usr/share/kmahjongglib/backgrounds/summerfield.svgz
/usr/share/kmahjongglib/backgrounds/wood_light.copyright
/usr/share/kmahjongglib/backgrounds/wood_light.desktop
/usr/share/kmahjongglib/backgrounds/wood_light.svgz
/usr/share/kmahjongglib/tilesets/alphabet.copyright
/usr/share/kmahjongglib/tilesets/alphabet.desktop
/usr/share/kmahjongglib/tilesets/alphabet.svgz
/usr/share/kmahjongglib/tilesets/classic.copyright
/usr/share/kmahjongglib/tilesets/classic.desktop
/usr/share/kmahjongglib/tilesets/classic.svgz
/usr/share/kmahjongglib/tilesets/default.copyright
/usr/share/kmahjongglib/tilesets/default.desktop
/usr/share/kmahjongglib/tilesets/default.svgz
/usr/share/kmahjongglib/tilesets/egypt.copyright
/usr/share/kmahjongglib/tilesets/egypt.desktop
/usr/share/kmahjongglib/tilesets/egypt.svgz
/usr/share/kmahjongglib/tilesets/jade.copyright
/usr/share/kmahjongglib/tilesets/jade.desktop
/usr/share/kmahjongglib/tilesets/jade.svgz
/usr/share/kmahjongglib/tilesets/traditional.copyright
/usr/share/kmahjongglib/tilesets/traditional.desktop
/usr/share/kmahjongglib/tilesets/traditional.svgz
/usr/share/qlogging-categories5/libkmahjongg.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KMahjongg/KMahjonggBackground
/usr/include/KF5/KMahjongg/KMahjonggConfigDialog
/usr/include/KF5/KMahjongg/KMahjonggTileset
/usr/include/KF5/KMahjongg/kmahjonggbackground.h
/usr/include/KF5/KMahjongg/kmahjonggconfigdialog.h
/usr/include/KF5/KMahjongg/kmahjongglib_version.h
/usr/include/KF5/KMahjongg/kmahjonggtileset.h
/usr/include/KF5/KMahjongg/libkmahjongg_export.h
/usr/lib64/cmake/KF5KMahjongglib/KF5KMahjonggTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5KMahjongglib/KF5KMahjonggTargets.cmake
/usr/lib64/cmake/KF5KMahjongglib/KF5KMahjongglibConfig.cmake
/usr/lib64/cmake/KF5KMahjongglib/KF5KMahjongglibConfigVersion.cmake
/usr/lib64/libKF5KMahjongglib.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5KMahjongglib.so.5.1.0
/usr/lib64/libKF5KMahjongglib.so.5
/usr/lib64/libKF5KMahjongglib.so.5.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkmahjongg/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/libkmahjongg/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/libkmahjongg/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/libkmahjongg/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f libkmahjongg5.lang
%defattr(-,root,root,-)

