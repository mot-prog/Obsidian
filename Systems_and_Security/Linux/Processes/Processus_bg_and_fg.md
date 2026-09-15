---
tags: [linux, processes]
---
Permet de mettre des processus en avant et arrière plan. Utilisé dans [[Polytech/S6/OS/TP/tp1|tp1]]
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

## Gérer plusieurs jobs avec `jobs`

```bash
./boucle.sh  >> /dev/pts/3 &   # lance en arrière-plan sur un autre terminal
```

```bash
jobs
[1]  + running    ./boucle.sh >> /dev/pts/3

fg %1   # met en pause le process dans le terminal 2 et le reprend dans le terminal actuel
jobs
[1]  + suspended  ./boucle.sh >> /dev/pts/3

bg %1   # le process reprend instantanément en arrière-plan
jobs
[1]  + running    ./boucle.sh >> /dev/pts/3
```

>[!tip] Exécution de scripts au premier plan
>`ps -u $USER` liste les processus ; `pstree -aps $(pgrep -n boucle.sh)` montre l'arbre du processus le plus récent ; `kill $(pgrep -n boucle.sh)` le termine. Voir [[Voir_les_processus_internes_au_terminal]].
