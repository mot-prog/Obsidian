---
tags: [personal]
---
# AppImage
```bash
wget https://github.com/linuxdeploy/linuxdeploy/releases/download/continuous/linuxdeploy-x86_64.AppImage chmod +x linuxdeploy-x86_64.AppImage
```

```bash
mkdir -p AppDir/usr/bin/Lutins
cp src/build/main AppDir/usr/bin/main
cp -r src/Lutins/* AppDir/usr/bin/Lutins/
cat << 'EOF' > custom-apprun
#!/bin/bash
HERE="$(dirname "$(readlink -f "${0}")")"
export LD_LIBRARY_PATH="${HERE}/usr/lib:${LD_LIBRARY_PATH}"
cd "${HERE}/usr/bin"
exec ./main "$@"
EOF
chmod +x custom-apprun
cat << 'EOF' > SpaceInvaders.desktop
[Desktop Entry]
Name=SpaceInvaders
Exec=main
Icon=icone
Type=Application
Categories=Game;
Terminal=false
EOF
NO_STRIP=1 ./linuxdeploy-x86_64.AppImage --appdir AppDir --executable AppDir/usr/bin/main --custom-apprun custom-apprun --desktop-file SpaceInvaders.desktop --icon-file icone.png --output appimage
rm -rf AppDir SpaceInvaders.desktop custom-apprun
```

# Windows (.exe)
```bash
# Installe le compilateur natif vers Windows
sudo pacman -S mingw-w64-gcc

# Installe les librairies SDL2 pour Windows via l'outil pamac (AUR)
pamac build mingw-w64-sdl2 mingw-w64-sdl2_ttf
```

A la racine du projet :
* Icone
```bash
convert icone.png icone.ico
nano ressources.rc # 1 ICON "icone.ico"
x86_64-w64-mingw32-windres ressources.rc -O coff -o ressources.res
```
* Compilation
```bash
x86_64-w64-mingw32-gcc src/C_files/*.c src/Graphique-2.0/*.c ressources.res -o SpaceInvaders.exe -I/usr/x86_64-w64-mingw32/include/SDL2 -L/usr/x86_64-w64-mingw32/lib -lmingw32 -lSDL2main -lSDL2 -lSDL2_ttf -mwindows
```
```bash
# 1. Créer le dossier final
mkdir SpaceInvaders

# 2. Déplacer l'exécutable dedans
mv SpaceInvaders.exe SpaceInvaders/

# 3. Copier ton dossier d'images et polices
cp -r src/Lutins SpaceInvaders/

# 4. Copier TOUTES les DLL nécessaires au fonctionnement de la SDL2 Windows
cp /usr/x86_64-w64-mingw32/bin/*.dll SpaceInvaders/
```
```bash
zip -r SpaceInvaders_Windows.zip SpaceInvaders
```
