#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : libkmahjongg
Version  : 18.08.0
Release  : 1
URL      : https://download.kde.org/stable/applications/18.08.0/src/libkmahjongg-18.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/18.08.0/src/libkmahjongg-18.08.0.tar.xz
Source99 : https://download.kde.org/stable/applications/18.08.0/src/libkmahjongg-18.08.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: libkmahjongg-lib
Requires: libkmahjongg-license
Requires: libkmahjongg-data
Requires: libkmahjongg-locales
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev qtbase-extras mesa-dev

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
Requires: libkmahjongg-lib
Requires: libkmahjongg-data
Provides: libkmahjongg-devel

%description dev
dev components for the libkmahjongg package.


%package lib
Summary: lib components for the libkmahjongg package.
Group: Libraries
Requires: libkmahjongg-data
Requires: libkmahjongg-license

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
%setup -q -n libkmahjongg-18.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535236558
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535236558
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libkmahjongg
cp COPYING %{buildroot}/usr/share/doc/libkmahjongg/COPYING
cp COPYING.DOC %{buildroot}/usr/share/doc/libkmahjongg/COPYING.DOC
cp COPYING.LIB %{buildroot}/usr/share/doc/libkmahjongg/COPYING.LIB
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

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KF5KMahjongg/kmahjonggbackground.h
/usr/include/KF5/KF5KMahjongg/kmahjonggconfigdialog.h
/usr/include/KF5/KF5KMahjongg/kmahjongglib_version.h
/usr/include/KF5/KF5KMahjongg/kmahjonggtileset.h
/usr/include/KF5/KF5KMahjongg/libkmahjongg_export.h
/usr/lib64/cmake/KF5KMahjongglib/KF5KMahjonggLibraryDepends-relwithdebinfo.cmake
/usr/lib64/cmake/KF5KMahjongglib/KF5KMahjonggLibraryDepends.cmake
/usr/lib64/cmake/KF5KMahjongglib/KF5KMahjongglibConfig.cmake
/usr/lib64/cmake/KF5KMahjongglib/KF5KMahjongglibConfigVersion.cmake
/usr/lib64/libKF5KMahjongglib.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5KMahjongglib.so.5
/usr/lib64/libKF5KMahjongglib.so.5.0.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/libkmahjongg/COPYING
/usr/share/doc/libkmahjongg/COPYING.DOC
/usr/share/doc/libkmahjongg/COPYING.LIB

%files locales -f libkmahjongg5.lang
%defattr(-,root,root,-)

