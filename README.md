bubbleserver-rpm
===

Instructions Build Package:
```
dnf install mock rpm-build rpmdevtools
rpmdev-setuptree
wget --output-document=rpmbuild/SOURCES/bubbleserver-0.9.update25.zip https://bubblesoftapps.com/bubbleupnpserver/BubbleUPnPServer-distrib.zip

git clone https://github.com/noohgnas/bubbleserver-rpm.git
cp -R bubbleserver-rpm/SOURCES rpmbuild/
cp -R bubbleserver-rpm/SPECS rpmbuild/

spectool -g -R rpmbuild/SPECS/bubbleserver.spec
rpmbuild --clean -ba rpmbuild/SPECS/bubbleserver.spec

/usr/bin/mock -r epel-6-i386 rpmbuild/SRPMS/bubbleserver-0.9.update25-1.src.rpm
```

Install:
```
# to install ffmpeg
dnf -y install http://www.squeezecommunity.org/repo/squeezecommunity-repo.noarch.rpm
dnf -y update squeezecommunity-repo
dnf install ./bubbleserver-0.9.update25-1.noarch.rpm
```
