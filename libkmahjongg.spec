#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 94c6be0
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkmahjongg
Version  : 24.12.2
Release  : 78
URL      : https://download.kde.org/stable/release-service/24.12.2/src/libkmahjongg-24.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.2/src/libkmahjongg-24.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.2/src/libkmahjongg-24.12.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
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
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : qt6base-dev
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n libkmahjongg-24.12.2
cd %{_builddir}/libkmahjongg-24.12.2
pushd ..
cp -a libkmahjongg-24.12.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738947570
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
%cmake ..   -G 'Unix Makefiles'
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
%cmake ..   -G 'Unix Makefiles'
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
export SOURCE_DATE_EPOCH=1738947570
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkmahjongg
cp %{_builddir}/libkmahjongg-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/libkmahjongg/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/libkmahjongg-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libkmahjongg/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libkmahjongg-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libkmahjongg/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/libkmahjongg-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkmahjongg/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
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
%find_lang libkmahjongg6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kmahjongglib/backgrounds/chinese_landscape.desktop
/usr/share/kmahjongglib/backgrounds/chinese_landscape.svgz
/usr/share/kmahjongglib/backgrounds/color_plain.desktop
/usr/share/kmahjongglib/backgrounds/default.desktop
/usr/share/kmahjongglib/backgrounds/default.svgz
/usr/share/kmahjongglib/backgrounds/egyptian.desktop
/usr/share/kmahjongglib/backgrounds/egyptian.svgz
/usr/share/kmahjongglib/backgrounds/summerfield.desktop
/usr/share/kmahjongglib/backgrounds/summerfield.svgz
/usr/share/kmahjongglib/backgrounds/wood_light.desktop
/usr/share/kmahjongglib/backgrounds/wood_light.svgz
/usr/share/kmahjongglib/tilesets/alphabet.desktop
/usr/share/kmahjongglib/tilesets/alphabet.svgz
/usr/share/kmahjongglib/tilesets/classic.desktop
/usr/share/kmahjongglib/tilesets/classic.svgz
/usr/share/kmahjongglib/tilesets/default.desktop
/usr/share/kmahjongglib/tilesets/default.svgz
/usr/share/kmahjongglib/tilesets/egypt.desktop
/usr/share/kmahjongglib/tilesets/egypt.svgz
/usr/share/kmahjongglib/tilesets/jade.desktop
/usr/share/kmahjongglib/tilesets/jade.svgz
/usr/share/kmahjongglib/tilesets/traditional.desktop
/usr/share/kmahjongglib/tilesets/traditional.svgz
/usr/share/qlogging-categories6/libkmahjongg.categories
/usr/share/qlogging-categories6/libkmahjongg.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KMahjongg6/KMahjonggBackground
/usr/include/KMahjongg6/KMahjonggConfigDialog
/usr/include/KMahjongg6/KMahjonggTileset
/usr/include/KMahjongg6/kmahjonggbackground.h
/usr/include/KMahjongg6/kmahjonggconfigdialog.h
/usr/include/KMahjongg6/kmahjongglib_version.h
/usr/include/KMahjongg6/kmahjonggtileset.h
/usr/include/KMahjongg6/libkmahjongg_export.h
/usr/lib64/cmake/KMahjongglib6/KMahjongglib6Config.cmake
/usr/lib64/cmake/KMahjongglib6/KMahjongglib6ConfigVersion.cmake
/usr/lib64/cmake/KMahjongglib6/KMahjongglib6Targets-relwithdebinfo.cmake
/usr/lib64/cmake/KMahjongglib6/KMahjongglib6Targets.cmake
/usr/lib64/libKMahjongg6.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKMahjongg6.so.6.0.241202
/usr/lib64/libKMahjongg6.so.6
/usr/lib64/libKMahjongg6.so.6.0.241202

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkmahjongg/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/libkmahjongg/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/libkmahjongg/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/libkmahjongg/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f libkmahjongg6.lang
%defattr(-,root,root,-)

