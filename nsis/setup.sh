#!/bin/bash

# see also https://cwiki.apache.org/confluence/display/DIRxSBOX/Installing+NSIS+-+All+platforms

yum -y install glibc-devel.i686 libstdc++-devel.i686

# rpmbuild has problems with the windows files.
# see also https://www.redhat.com/archives/rhl-devel-list/2006-June/msg00821.html
mv /usr/bin/strip /usr/bin/strip.bak
ln -s /bin/true /usr/bin/strip
