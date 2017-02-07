%define name nsis
%define version 3.01

# work around to include windows binaries, see https://www.redhat.com/archives/rhl-devel-list/2006-June/msg00822.html
%define __spec_install_post /usr/lib/rpm/brp-compress
%define __os_install_post /usr/lib/rpm/brp-compress

# do not build a debuginfo package. this avoids error on CentOS7:
# Fehler: Datei /root/rpmbuild/BUILD/nsis-2.46-src/debugfiles.list aus %files konnte nicht geöffnet: Datei oder Verzeichnis nicht gefunden
%define debug_package %{nil}

Summary: Nullsoft Scriptable Install System
Name: %{name}
Version: %{version}
Release: %{release}
Packager: Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
License: zlib/libpng
Group: Office Suite and Productivity
BuildRequires: gcc gcc-c++ scons zlib-devel
# yum-builddep says: Error: No Package found for glibc-devel.i686. Therefore we install it manually in setup.sh
#BuildRequires: glibc-devel.i686 libstdc++-devel.i686
BuildRoot: /tmp/buildroot
Source: nsis-%{version}-src.tar.bz2
Source1: nsis-%{version}.zip

%description
NSIS (Nullsoft Scriptable Install System) is a professional open source system to create Windows installers.

%prep
[ -d $RPM_BUILD_ROOT ] && [ "/" != "$RPM_BUILD_ROOT" ] && rm -rf $RPM_BUILD_ROOT
%setup -q -n nsis-%{version}-src
unzip ../../SOURCES/nsis-%{version}.zip

%build
scons SKIPSTUBS=all SKIPPLUGINS=all SKIPUTILS=all SKIPMISC=all NSIS_CONFIG_CONST_DATA_PATH=no PREFIX=`pwd`/nsis-%{version} install-compiler

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/nsis
cp -r `pwd`/nsis-%{version}/* $RPM_BUILD_ROOT/usr/local/nsis
cp -r `pwd`/build/urelease/makensis/makensis $RPM_BUILD_ROOT/usr/local/nsis
cd $RPM_BUILD_ROOT/usr/local/nsis; ln -s . bin
cd $RPM_BUILD_ROOT/usr/local; ln -s nsis/{Contrib,Include,Plugins,Stubs} .

%clean
# Clean up after ourselves, but be careful in case someone sets a bad buildroot
[ -d $RPM_BUILD_ROOT ] && [ "/" != "$RPM_BUILD_ROOT" ] && rm -rf $RPM_BUILD_ROOT

%files
/usr/local/nsis
/usr/local/Contrib
/usr/local/Include
/usr/local/Plugins
/usr/local/Stubs

%post

%changelog
* Tue Feb 07 2017 Timotheus Pokorra <tp@tbits.net> - 3.0.1-2
- need symbolic links with CentOS6
* Fri Jan 20 2017 Timotheus Pokorra <tp@tbits.net> - 3.0.1
- Upgrade to NSIS 3.01
* Wed Sep 28 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 3.0
- Upgrade to NSIS 3.0
* Wed Feb 11 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
- Fix build for CentOS7
* Thu Nov 20 2014 Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
- First build
