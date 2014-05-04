bubbleserver-rpm
===

Instructions Build Package:
```
yum install mock rpm-build rpmdevtools
rpmdev-setuptree
wget --output-document=rpmbuild/SOURCES/bubbleserver-0.8.2.zip http://bubblesoftapps.com/bubbleupnpserver/BubbleUPnPServer-distrib.zip
wget --output-document=rpmbuild/SOURCES/ffmpeg.zip http://www.bubblesoftapps.com/bubbleupnpserver/ffmpeg.zip

spectool -g -R rpmbuild/SPECS/bubbleserver.spec
rpmbuild --clean -ba rpmbuild/SPECS/bubbleserver.spec
```
