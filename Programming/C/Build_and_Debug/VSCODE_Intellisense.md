---
tags: [programming, c, debugging]
---
Le but est d'enlever les erreurs indiquées par l'intellisense de VSCODE pour avoir un rep de fichiers propre.
`crtl + shift + p` -> `edit Configuarations (JSON)`
```JSON
{
    "configurations": [
        {
            "name": "AVR (Microcontrôleur)",
            "includePath": [
                "${workspaceFolder}/**"
            ],
            "defines": [],
            "compilerPath": "/usr/bin/avr-gcc",
            "compilerArgs": [
                "-mmcu=atmega32u4"
            ],
            "cStandard": "c11",
            "cppStandard": "c++11",
            "intelliSenseMode": "linux-gcc-x64"
        },
        {
            "name": "Linux (PC Host)",
            "includePath": [
                "${workspaceFolder}/**"
            ],
            "defines": [],
            "compilerPath": "/usr/bin/gcc",
            "cStandard": "c11",
            "cppStandard": "c++11",
            "intelliSenseMode": "linux-gcc-x64"
        }
    ],
    "version": 4
}
```

- Choisir le profil en fonction de si on est sur un code AVR ou un code PC (en bas à droite) :
![[profile_vscode.png]]
![[profile_vscode2.png]]