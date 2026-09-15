---
aliases:
  - "Fichiers polyglottes"
  - "Polyglotte"
  - "Culture numérique - fichiers"
  - "Systèmes de fichiers"
  - "CTF stéganographie"
tags:
  - security
  - forensics
  - ctf
  - steganography
  - filesystem
related: "[[binwalk]]"
---

# Stéganographie et fichiers

Sources : [[Polytech/S6/CN/Cours|Cours CN]]

## Fichiers : suite d'octets

Un fichier est une **suite d'octets** caractérisée par :
- le **format**
- les **métadonnées**
- l'**extension**

### Systèmes de fichiers
Le système de fichiers permet à l'OS de savoir comment sont organisés les fichiers :
- EXT 2 / EXT 4 (Linux)
- FAT 16 / FAT 32
- NTFS (Windows)

## Fichier polyglotte

Un fichier **polyglotte** est écrit dans une forme valide de *plusieurs* langages de programmation ou formats de fichiers. Exemple : cacher un JPEG derrière un PNG.

```bash
binwalk image.png    # affiche la description de l'image → on voit que c'est un jpeg
```

Voir [[binwalk]] et [[media]] (détails de n'importe quel media).

```bash
cat fichier1 fichier2   # concatène des fichiers
```

## Stéganographie

Cacher des choses dans des choses : dissimuler un message, un programme ou un fichier dans un support apparemment anodin (image, son, vidéo…). Technique très utilisée en **CTF** 🔍