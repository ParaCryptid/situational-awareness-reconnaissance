#!/bin/bash
APP_NAME=training-simulation-system
VERSION=1.0.0
ARCH=amd64
INSTALL_DIR=/opt/$APP_NAME

mkdir -p build/$APP_NAME/DEBIAN
mkdir -p build/$APP_NAME$INSTALL_DIR
cp -r src/* build/$APP_NAME$INSTALL_DIR/
cp requirements.txt build/$APP_NAME$INSTALL_DIR/

cat <<EOF > build/$APP_NAME/DEBIAN/control
Package: $APP_NAME
Version: $VERSION
Section: base
Priority: optional
Architecture: $ARCH
Depends: python3, python3-pip
Maintainer: ParaCryptid
Description: Secure training simulation system
EOF

dpkg-deb --build build/$APP_NAME