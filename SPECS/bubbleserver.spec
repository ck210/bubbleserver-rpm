#
# spec file for buubleserver app...
#
Summary: BubbleUPnP Server makes your LAN Media Servers available for streaming over mobile (3G/4G) and WiFi connections
Name: bubbleserver
Version: 0.8.2
Release: 1
License: (c) 2011 - 2012 Michael Pujos. All rights reserved. (See LICENCE.txt)
Group: Applications/Sound
URL: http://www.bubblesoftapps.com/bubbleupnpserver/
Distribution: RedHat/CentOS Linux
Vendor: Michael Pujos
Packager: Marcel Beck <marcel.beck@outlook.com>
Source: %{name}-%{version}.zip
Source1: bubbleserver-init.d
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# Requires: java >= 1.6

%description
BubbleUPnP Server:
-    extends your existing UPnP AV Media Servers and Media Renderers on your network with new functionality
-    allow easy Internet streaming and downloading of your music and videos over mobile and WiFi 
     connections with BubbleUPnP for Android, in a secure and network bandwidth efficient way.
-    since v0.5.3 it is possible to do Internet streaming on Windows as well

%prep
%setup -q -c

%install
%{__mkdir_p} %{buildroot}/opt/
cp -R ${RPM_BUILD_DIR}/%{name}-%{version} %{buildroot}/opt/bubbleserver
%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_initrddir}/%{name}

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} \
    -s /sbin/nologin -c "%{name} daemon" %{name}
exit 0

%preun
service %{name} stop
chkconfig --del %{name}
exit 0

%postun
if [ $1 = 0 ]; then
	chkconfig --del %{name}
	getent passwd %{name} >/dev/null && \
	userdel -r %{name} 2>/dev/null
fi
exit 0

%post
chkconfig --add %{name}

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
/opt/bubbleserver/
%{_initrddir}/%{name}
