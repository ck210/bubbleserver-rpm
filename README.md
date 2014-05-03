bubbleserver-rpm
===

Instructions:
```
rpmdev-setuptree
wget --output-document=rpmbuild/SOURCES/bubbleserver-0.8.2.zip http://bubblesoftapps.com/bubbleupnpserver/BubbleUPnPServer-distrib.zip

spectool -g -R rpmbuild/SPECS/bubbleserver.spec
rpmbuild --clean -ba rpmbuild/SPECS/bubbleserver.spec
```