---
tags: [linux, hardware]
---
:wq
```bash
ncdu
```
Version interactive (TUI / curses) de `du` : permet de voir **visuellement** ce qui prend la place sur le disque et de naviguer dedans avec les flèches. Beaucoup plus rapide que `du -h | sort` quand on cherche où passent les Go.

À installer sur Arch :

```bash
sudo pacman -S ncdu
```

## Utilisation de base

```bash
ncdu                # scanne le répertoire courant
ncdu /var/log       # scanne un répertoire précis
ncdu -x /           # scanne "/" sans traverser les autres systèmes de fichiers
```

> [!tip] `-x` est quasi obligatoire sur `/`
> Sans `-x`, le scan descend dans `/proc`, `/sys`, les points de montage… et peut prendre des heures. Avec `-x` on reste sur le même filesystem.

## Options utiles

| Option | Rôle |
| --- | --- |
| `-x` | Ne pas traverser les frontières de fichiersystems |
| `-e`, `--extended` | Affiche en plus proprio / permissions / date de modification (≈ +30 % de RAM) |
| `--exclude pattern` | Exclut du calcul les fichiers correspondant au motif (répétable) |
| `-X FILE`, `--exclude-from` | Charge les motifs d'exclusion depuis un fichier (un motif par ligne) |
| `-L`, `--follow-symlinks` | Suit les liens symboliques et compte la taille de la cible |
| `-o FILE` | Exporte l'arbre en JSON au lieu d'ouvrir l'interface |
| `-O FILE` | Exporte l'arbre en binaire (compressé, meilleur pour de très gros arbres) |
| `-f FILE` | Réimporte un export précédent |
| `-t NUM` | Nombre de threads pour le scan |
| `-q` | Met le scan en mode silencieux (utile en SSH pour économiser de la bande passante) |
| `-r` | Mode lecture seule : `-r` désactive la suppression, `-rr` désactive aussi le shell |
| `--color dark` | Palette de couleurs pour fond sombre |
| `--sort name-desc` | Colonne de tri par défaut |
| `-h`, `--help` | Aide |

## Raccourcis clavier

| Touche | Action |
| --- | --- |
| `↑` `↓` / `j` `k` | Naviguer dans la liste |
| `→` `Entrée` / `l` | Entrer dans un répertoire |
| `←` / `h` | Remonter au répertoire parent |
| `?` | Ouvrir l'aide intégrée (le meilleur réflexe) |
| `n` | Trier par nom |
| `s` | Trier par taille |
| `C` | Trier par nombre d'éléments |
| `M` | Trier par date de modification (nécessite `-e`) |
| `t` | Répertoires avant fichiers |
| `a` | Basculer entre taille **sur disque** et taille **apparente** |
| `e` | Afficher / masquer les fichiers cachés |
| `g` | Afficher pourcentage / barre de proportion / les deux / rien |
| `c` | Afficher le nombre d'éléments enfants |
| `m` | Afficher la date de modification (nécessite `-e`) |
| `u` | Basculer la colonne taille partagée / unique (hard links) |
| `i` | Infos détaillées sur l'élément sélectionné |
| `r` | Recalculer le répertoire courant |
| `b` | Ouvrir un shell dans le répertoire courant |
| `d` | **Supprimer** l'élément sélectionné (confirmation par défaut) |
| `q` | Quitter |

> [!warning] La touche `d` supprime réellement les données
> L'archivage n'est pas possible, c'est un `rm -rf`. Une confirmation est demandée par défaut, mais elle peut être désactivée par erreur avec `--no-confirm-delete`. Pour explorer sans risque :
> ```bash
> ncdu -r          # ou ncdu --disable-delete --disable-shell
> ```

## Drapeaux affichés devant les entrées

| Drapeau | Signification |
| --- | --- |
| `!` | Erreur de lecture sur ce répertoire |
| `.` | Erreur dans un sous-répertoire, la taille affichée peut être fausse |
| `<` | Exclu par un motif d'exclusion |
| `>` | Se trouve sur un autre filesystem |
| `^` | Pseudo-filesystem Linux (`/proc`, `/sys`…) exclu |
| `@` | Ni fichier ni dossier (lien symbolique, socket…) |
| `H` | Fichier déjà compté (hard link) |
| `e` | Répertoire vide |

> [!exemple] Difference entre taille sur disque et taille apparente
> Un fichier de 2 Go en troué (« sparse ») occupe quasi rien sur le disque mais fait 2 Go en taille apparente. La touche `a` permet de voir la différence, c'est souvent là que se cachent les gros volumes.

## Export / import

Scanner un gros dossier est long. On peut le faire une fois, sans interface, et parcourir le résultat plus tard :

```bash
ncdu -1xO export.ncdu /     # scan + export binaire
ncdu -f export.ncdu         # parcours plus tard
```

Export JSON compressé en zstd :

```bash
ncdu -co- / | tee export.json.zst | ./ncdu -f-
```

Scanner une machine distante et parcourir chez soi (gain : pas de latence réseau, pas de RAM consommée au loin) :

```bash
ssh user@system ncdu -co- / | ./ncdu -f-
```

Dans un cron, remplacer `-1` par `-0` pour supprimer la sortie de progression inutile.

## Configuration

Les options peuvent être mises dans `/etc/ncdu.conf` ou `~/.config/ncdu/config`, **une option par ligne**, les lignes commençant par `#` sont ignorées, un `@` en début de ligne supprime les erreurs de parsing. La config système est chargée avant la config utilisateur, et la ligne de commande passe au-dessus des deux.

```bash
# /etc/ncdu.conf

# Toujours activer le mode étendu
-e

# Désactiver la suppression
--disable-delete

# Exclure les dossiers .git
--exclude .git

# Lire les exclusions depuis ~/.ncduexcludes sans erreur si absent
@--exclude-from ~/.ncduexcludes
```

`--ignore-config` permet d'ignorer completely ces fichiers.

## Rappel utile

> [!note]
> - `[[df -h]]` → quel filesystem est plein ?
> - `[[du -h]]` → taille brute d'un dossier
> - `ncdu` → **où** est la place, avec navigation interactive
