---
tags: [linux, processes]
---
Permet de mettre des processus en avant et arrière plan. Utilisé dans [[tp1]]
```bash
bg  #permet de mettre le processus en arriere plan
```
```bash
fg  #permet de mettre le processus en avant plan
# -> crtl +z permet de susspendre le process
# fg permet de le reprendre 
```

Processus de manière **asynchrone**:
```bash
process & #Un peut similaire à bg
```
Pour arrêter un processus en **bg** ou en **asynchrone** :
* on le met en `fg` et on l'arrête avec `crtl +c`
* on le tue avec 
 ```bash
 kill $(pgrep -n process)
 ```
