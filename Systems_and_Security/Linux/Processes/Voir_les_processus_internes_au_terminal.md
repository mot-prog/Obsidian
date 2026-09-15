---
tags: [linux, processes]
---
```bash
 ps
 ```
 >[!example]
 > ```bash
 > ps  
    PID TTY          TIME CMD  
 626017 pts/4    00:00:06 zsh  
 626024 pts/4    00:00:00 zsh  
 626035 pts/4    00:00:00 zsh  
 626036 pts/4    00:00:00 zsh  
 626038 pts/4    00:00:00 gitstatusd  
 644817 pts/4    00:00:00 boucle.sh  
 644872 pts/4    00:00:00 sleep  
 644873 pts/4    00:00:00 ps
 > ```
 
 [[tty]]

## Commandes utiles

```bash
ps -u $USER                    # processus de l'utilisateur courant
pstree -aps $(pgrep -n boucle.sh)  # arbre du processus le plus récent
kill $(pgrep -n boucle.sh)     # tue le processus le plus récent
```

## Explorer un processus via /proc

```bash
cd /proc/644817                # dossier virtuel du processus (par PID)
cat status | grep -e State -e switch
# State:  S (sleeping)
# voluntary_ctxt_switches: 760
# nonvoluntary_ctxt_switches: 16

ls -l exe && ls -l cwd
# exe -> /usr/bin/bash          (binaire exécuté)
# cwd -> /home/.../exo5         (répertoire courant)
```

>[!info] `/proc` est un système de fichiers virtuel
>Chaque processus y a un dossier nommé par son **PID**. `exe` pointe vers le programme lancé, `cwd` vers son répertoire de travail, `status` expose son état et son nombre de commutations de contexte.
 