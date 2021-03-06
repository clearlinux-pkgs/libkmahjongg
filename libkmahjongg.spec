#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkmahjongg
Version  : 21.04.2
Release  : 29
URL      : https://download.kde.org/stable/release-service/21.04.2/src/libkmahjongg-21.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.04.2/src/libkmahjongg-21.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.04.2/src/libkmahjongg-21.04.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: libkmahjongg-data = %{version}-%{release}
Requires: libkmahjongg-lib = %{version}-%{release}
Requires: libkmahjongg-license = %{version}-%{release}
Requires: libkmahjongg-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data

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
%setup -q -n libkmahjongg-21.04.2
cd %{_builddir}/libkmahjongg-21.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623391295
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1623391295
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkmahjongg
cp %{_builddir}/libkmahjongg-21.04.2/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkmahjongg/3e8971c6c5f16674958913a94a36b1ea7a00ac46
pushd clr-build
%make_install
popd
%find_lang libkmahjongg5

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
/usr/share/kmahjongglib/backgrounds/default.svg
/usr/share/kmahjongglib/backgrounds/egyptian.copyright
/usr/share/kmahjongglib/backgrounds/egyptian.desktop
/usr/share/kmahjongglib/backgrounds/egyptian.svgz
/usr/share/kmahjongglib/backgrounds/summerfield.copyright
/usr/share/kmahjongglib/backgrounds/summerfield.desktop
/usr/share/kmahjongglib/backgrounds/summerfield.svg
/usr/share/kmahjongglib/backgrounds/wood_light.copyright
/usr/share/kmahjongglib/backgrounds/wood_light.desktop
/usr/share/kmahjongglib/backgrounds/wood_light.svg
/usr/share/kmahjongglib/tilesets/alphabet.copyright
/usr/share/kmahjongglib/tilesets/alphabet.desktop
/usr/share/kmahjongglib/tilesets/alphabet.svgz
/usr/share/kmahjongglib/tilesets/classic.copyright
/usr/share/kmahjongglib/tilesets/classic.desktop
/usr/share/kmahjongglib/tilesets/classic.svg
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
/usr/include/KF5/KF5KMahjongg/KMahjonggBackground
/usr/include/KF5/KF5KMahjongg/KMahjonggConfigDialog
/usr/include/KF5/KF5KMahjongg/KMahjonggTileset
/usr/include/KF5/KF5KMahjongg/kmahjonggbackground.h
/usr/include/KF5/KF5KMahjongg/kmahjonggconfigdialog.h
/usr/include/KF5/KF5KMahjongg/kmahjongglib_version.h
/usr/include/KF5/KF5KMahjongg/kmahjonggtileset.h
/usr/include/KF5/KF5KMahjongg/libkmahjongg_export.h
/usr/lib64/cmake/KF5KMahjongglib/KF5KMahjonggTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5KMahjongglib/KF5KMahjonggTargets.cmake
/usr/lib64/cmake/KF5KMahjongglib/KF5KMahjongglibConfig.cmake
/usr/lib64/cmake/KF5KMahjongglib/KF5KMahjongglibConfigVersion.cmake
/usr/lib64/libKF5KMahjongglib.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5KMahjongglib.so.5
/usr/lib64/libKF5KMahjongglib.so.5.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkmahjongg/3e8971c6c5f16674958913a94a36b1ea7a00ac46

%files locales -f libkmahjongg5.lang
%defattr(-,root,root,-)

