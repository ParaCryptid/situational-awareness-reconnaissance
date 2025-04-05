#!/bin/bash
set -e

echo "[+] Starting full build and packaging..."

# Clean previous builds
rm -rf dist build-release out || true
mkdir -p dist out

# Build .exe with PyInstaller (Windows)
echo "[+] Building Windows .exe..."
pyinstaller --onefile --name osint_toolkit src/main.py
mv dist/osint_toolkit.exe out/

# Build Linux AppImage using AppImage toolchain (placeholder here)
echo "[+] Preparing AppImage (requires AppImageTool)..."
# ./appimagetool.AppImage <AppDir> out/osint_toolkit.AppImage
echo "AppImage build skipped (tool not installed)"

# Build .deb package (Debian/Ubuntu)
echo "[+] Building .deb package..."
mkdir -p build-release/usr/local/bin
cp dist/osint_toolkit build-release/usr/local/bin/osint_toolkit
dpkg-deb --build build-release out/osint-toolkit.deb

echo "[✓] All builds complete. Files in /out:"
ls -lh out
