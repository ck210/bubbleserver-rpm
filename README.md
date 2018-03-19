bubbleserver-rpm
===

Prepare environment:
```
dnf install mock rpm-build rpmdevtools
rpmdev-setuptree
```

Build Package:
```
export BUBBLE_VERSION=0.9.update30
wget --output-document=rpmbuild/SOURCES/bubbleserver-${BUBBLE_VERSION}.zip https://bubblesoftapps.com/bubbleupnpserver/BubbleUPnPServer-distrib.zip

git clone https://github.com/noohgnas/bubbleserver-rpm.git
cp -R bubbleserver-rpm/SOURCES rpmbuild/
cp -R bubbleserver-rpm/SPECS rpmbuild/

spectool -g -R rpmbuild/SPECS/bubbleserver.spec
rpmbuild --clean -ba rpmbuild/SPECS/bubbleserver.spec

/usr/bin/mock -r epel-6-i386 rpmbuild/SRPMS/bubbleserver-0.9.update30-1.src.rpm
```

Install example:
```
# to install ffmpeg
dnf -y install http://www.squeezecommunity.org/repo/squeezecommunity-repo.noarch.rpm
dnf -y update squeezecommunity-repo
dnf install ./bubbleserver-0.9.update30-1.noarch.rpm
```

bubbleupnpserver
===
https://bubblesoftapps.com/bubbleupnpserver/
