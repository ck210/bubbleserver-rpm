bubbleserver-rpm
===

Instructions Build Package:
```
yum install mock rpm-build rpmdevtools
rpmdev-setuptree
wget --output-document=rpmbuild/SOURCES/bubbleserver-0.8.2.zip http://bubblesoftapps.com/bubbleupnpserver/BubbleUPnPServer-distrib.zip
wget --output-document=rpmbuild/SOURCES/ffmpeg.zip http://www.bubblesoftapps.com/bubbleupnpserver/ffmpeg.zip

git clone https://github.com/nexeck/bubbleserver-rpm.git
cp -R bubbleserver-rpm/SOURCES rpmbuild/
cp -R bubbleserver-rpm/SPECS rpmbuild/

spectool -g -R rpmbuild/SPECS/bubbleserver.spec
rpmbuild --clean -ba rpmbuild/SPECS/bubbleserver.spec

/usr/bin/mock -r epel-6-i386 rpmbuild/SRPMS/bubbleserver-0.8.2-3.src.rpm
```
