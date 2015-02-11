%define name nsis
%define version 2.46

# work around to include windows binaries, see https://www.redhat.com/archives/rhl-devel-list/2006-June/msg00822.html
%define __spec_install_post /usr/lib/rpm/brp-compress
%define __os_install_post /usr/lib/rpm/brp-compress

Summary: Nullsoft Scriptable Install System
Name: %{name}
Version: %{version}
Release: %{release}
Packager: Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
License: zlib/libpng
Group: Office Suite and Productivity
BuildRequires: gcc gcc-c++ scons
# yum-builddep says: Error: No Package found for glibc-devel.i686. Therefore we install it manually in setup.sh
#BuildRequires: glibc-devel.i686 libstdc++-devel.i686
BuildRoot: /tmp/buildroot
Source: nsis-%{version}-src.tar.bz2
Source1: nsis-%{version}.zip
Patch1: gcc46NameLookupChanges.patch

%description
NSIS (Nullsoft Scriptable Install System) is a professional open source system to create Windows installers.

%prep
[ -d $RPM_BUILD_ROOT ] && [ "/" != "$RPM_BUILD_ROOT" ] && rm -rf $RPM_BUILD_ROOT
%setup -q -n nsis-%{version}-src
unzip ../../SOURCES/nsis-%{version}.zip
%patch1 -p1

%build
scons SKIPSTUBS=all SKIPPLUGINS=all SKIPUTILS=all SKIPMISC=all NSIS_CONFIG_CONST_DATA_PATH=no PREFIX=`pwd`/nsis-%{version} install-compiler

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/nsis
cp -r `pwd`/nsis-%{version}/* $RPM_BUILD_ROOT/usr/local/nsis
cp -r `pwd`/build/release/makensis/makensis $RPM_BUILD_ROOT/usr/local/nsis
cd $RPM_BUILD_ROOT/usr/local/nsis; ln -s . bin

%clean
# Clean up after ourselves, but be careful in case someone sets a bad buildroot
[ -d $RPM_BUILD_ROOT ] && [ "/" != "$RPM_BUILD_ROOT" ] && rm -rf $RPM_BUILD_ROOT

%files
/usr/local/nsis

%post

%changelog
* Wed Feb 11 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
- Fix build for CentOS7
* Thu Nov 20 2014 Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
- First build
