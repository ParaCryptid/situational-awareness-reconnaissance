#!/bin/bash
APP=training_simulation_system
mkdir -p AppDir/usr/bin
cp -r src/* AppDir/usr/bin/
echo -e '#!/bin/bash\npython3 /usr/bin/main.py' > AppDir/AppRun
chmod +x AppDir/AppRun

cat > AppDir/$APP.desktop <<EOF
[Desktop Entry]
Name=Training Simulation
Exec=AppRun
Icon=app
Type=Application
Categories=Utility;
EOF

wget -nc https://github.com/AppImage/AppImageKit/releases/latest/download/appimagetool-x86_64.AppImage
chmod +x appimagetool-x86_64.AppImage
./appimagetool-x86_64.AppImage AppDir build/$APP.AppImage