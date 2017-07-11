#
# spec file for buubleserver app...
#
Summary: BubbleUPnP Server makes your LAN Media Servers available for streaming over mobile (3G/4G) and WiFi connections
Name: bubbleserver
Version: 0.9.update25
Release: 1
License: (c) 2011 - 2015 Michael Pujos. All rights reserved. (See LICENCE.txt)
Group: Applications/Sound
URL: https://bubblesoftapps.com/
Vendor: Michael Pujos
Packager: Sanghoon LEE <noohgnas@gmail.com>
Source: %{name}-%{version}.zip
Source1: bubbleserver-init.d
#BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: nss >= 3.23, java-1.8.0-openjdk-headless >= 1.8
BuildRequires: wget, unzip
AutoReqProv: no

%description
BubbleUPnP Server provides new services, many of them running on top of your
existing UPnP/DLNA devices:

- make various media formats not natively supported by Chromecast playable
  with transcoding. Works in tandem with Android BubbleUPnP
- secure Internet access to your UPnP/DLNA Media Servers content with
  Android BubbleUPnP and foobar2000:
  - stream and download your music, video, photos with your Android
    device from a mobile or WiFi connection with optional transcoding to
    reduce bandwidth.
  - no need to sync, to upload to the cloud, to register to an online
    service
- create OpenHome Media Renderers from any UPnP AV renderer (provides
  on-device playlist, multiple Control Point access to the same renderer)
- fix issues of UPnP/DLNA Media Servers (discovery issues, broken data,
  add some audio DLNA compliance) by creating a proxy Media Server
- access your UPnP/DLNA Media Servers across different networks

BUBBLEUPNP SERVER IS NOT AN UPNP AV MEDIA SERVER.

%prep
%setup -q -c
DOWNLOAD_BASE_URL=https://bubblesoftapps.com/bubbleupnpserver/core
INSTALL_DIR=/usr/share/bubbleupnpserver
ARCH=`uname -m`
FFMPEG_ZIP=

if [ "$ARCH" = "x86_64" ]; then
  FFMPEG_ZIP=ffmpeg_linux.zip
elif [ "$ARCH" = "i386" -o  "$ARCH" = "i686" ]; then
  FFMPEG_ZIP=ffmpeg_linux_32bit.zip
elif [ "$ARCH" = "armv7l" ]; then
  FFMPEG_ZIP=ffmpeg_linux_armv7l.zip
fi
FFMPEG_ZIP=ffmpeg_linux.zip
if [ ! -z $FFMPEG_ZIP ]; then
  cd ${RPM_BUILD_DIR}/%{name}-%{version}
  wget -q ${DOWNLOAD_BASE_URL}/$FFMPEG_ZIP
  unzip $FFMPEG_ZIP
  rm $FFMPEG_ZIP
  chmod +x ffmpeg ffprobe
fi

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
chown %{name}:%{name} -R /opt/bubbleserver

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
/opt/bubbleserver/
%{_initrddir}/%{name}
