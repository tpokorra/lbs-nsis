%define name nsis
%define version 2.64

Summary: Nullsoft Scriptable Install System
Name: %{name}
Version: %{version}
Release: %{release}
Packager: Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
License: zlib/libpng
Group: Office Suite and Productivity
BuildRequires: gcc gcc-c++ libstdc++-devel.i686 glibc-devel.i686 scons
BuildRoot: /tmp/buildroot
Source: nsis-%{version}-src.tar.bz2
Source1: nsis-%{version}.zip

%description
NSIS (Nullsoft Scriptable Install System) is a professional open source system to create Windows installers.

%prep
[ -d $RPM_BUILD_ROOT ] && [ "/" != "$RPM_BUILD_ROOT" ] && rm -rf $RPM_BUILD_ROOT
%setup -q
unzip ../../SOURCES/nsis-%{version}.zip

%build
scons SKIPSTUBS=all SKIPPLUGINS=all SKIPUTILS=all SKIPMISC=all NSIS_CONFIG_CONST_DATA_PATH=no PREFIX=`pwd`/../nsis-%{version} install-compiler

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/nsis
cp -r `pwd`/../nsis-%{version}/* $RPM_BUILD_ROOT/usr/local/nsis
cp -r `pwd`/build/release/makensis/makensis $RPM_BUILD_ROOT/usr/local/nsis
cd $RPM_BUILD_ROOT/usr/local/nsis; ln -s . bin

%clean
# Clean up after ourselves, but be careful in case someone sets a bad buildroot
[ -d $RPM_BUILD_ROOT ] && [ "/" != "$RPM_BUILD_ROOT" ] && rm -rf $RPM_BUILD_ROOT

%files
/usr/local/nsis

%post

%changelog
* Thu Nov 20 2014 Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
- First build
