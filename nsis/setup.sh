#!/bin/bash

# see also https://cwiki.apache.org/confluence/display/DIRxSBOX/Installing+NSIS+-+All+platforms

# only do this on CentOS, not on Fedora
OS=`cat /etc/redhat-release | awk '{print $1}'`
if [[ "$OS" == "CentOS" ]
then 
  yum -y install glibc-devel.i686 libstdc++-devel.i686 glibc-devel libstdc++-devel
fi
