---
aliases:
  - "Chaîne de compilation"
  - "Chaine de compilation"
  - "Édition de liens"
  - "Librairies statiques"
  - "ELF"
  - "Objdump"
tags:
  - programming
  - c
  - compilation
  - assembly
  - elf
  - linker
related: "[[Makefile]]"
---

# Compilation

Sources : [[Chaîne de compilation]] · [[Adresses et registres]] · [[librairies]] · [[tp_makefile]]

## La chaîne de compilation

Toute compilation passe par 5 étapes, de l'écriture du code jusqu'au binaire exécutable :

1. **Preprocessing** : charge les `#include`, traite les `#define`. Les fichiers `.i` permettent de voir le contenu des headers après cette étape.
   ```bash
   gcc -E monfichier.i
   ```
2. **AST (Abstract Syntax Tree)** : arbre abstrait de compilation (visualisable avec `clang`). Il vérifie que la **grammaire** est correcte (opérations autorisées, ex : `5 = x;` est refusé) et permet les **optimisations**. Cette étape est la même pour Python, C++, Fortran…
3. **IR (Intermediate Representation)** : assembleur pour une machine idéale — infinité de registres et de RAM, latence nulle. *Indépendante de la chaîne de compilation.*
4. **ASM (assembleur)** : dépendant de la cible (MacOS, Windows, Android, Linux…). C'est ici qu'interviennent les **optimisations** (ex : un code de 40 lignes séparé en 4 boucles de 10 lignes pour faire travailler 4 cœurs).
5. **Binaire** : fichier exécutable ([[Adresses et registres|ELF]]).

>[!info] Pourquoi Python et Java sont lents ?
>Python et Java passent par une **machine virtuelle** qui traduit le code *avant* de l'envoyer à l'OS : c'est la raison principale de leur lenteur.

## Les options de gcc

| Option | Étape | Effet |
| --- | --- | --- |
| `-E` | Preprocesseur | S'arrête après les `#define`, recherche les `.h`, enlève les commentaires, remplace les constantes par leur valeur |
| `-S` | Compilateur | Convertit le code en assembleur → fichier `.s` (si aucun problème) |
| `-c` | Assembleur | Produit le fichier objet `.o` |
| `-d` | — | Convertit les instructions (ADD, SUB…) en hexadécimal |
| `-o` | Linker | Ajoute le code manquant (ex : saut vers `printf` dans la `libc`) |

## ELF : Executable Linking Format

- **Adresse du point d'entrée** = adresse où le programme commence. Ex : `0x1050` = adresse de `_start`, qui lance `_start_main`.
- Chaîne `C → ELF (exe)` via `GCC` : (préprocesseur → compilateur → assembleur → linker) → ELF contenant la `libc`, stocké en **RAM**.
- Le **shell/terminal** demande au noyau d'aller chercher le ELF et de l'exécuter.
- Un `.o` non lié a des adresses relatives à sa section `.text` (décalages, ex : `str_len` à `0x00`, `str_copy` à `0x2f`) — c'est le **linker** qui attribue les adresses virtuelles définitives dans l'exécutable.

### Sections mémoire (visibles avec `objdump -t`)

| Section | Contenu |
| --- | --- |
| `.text` | Code machine (fonctions, runtime C, `_start`, `main`) |
| `.data` | Variables globales/statiques *initialisées* |
| `.bss` | Variables globales/statiques *non initialisées* (remplies de zéros au lancement) |
| `.rodata` | Données en lecture seule (chaînes littérales) |

```bash
objdump -t prog_static | grep -e .text -e .data -e .bss
```

*Lien avec les adresses : voir [[Adresses et registres]].*

## Librairies statiques (`.a`)

Création d'une archive avec `ar` :

```bash
ar rcs libstrutils.a strutils.o
```

- **r (replace)** : insère les fichiers dans l'archive, remplace les membres existants.
- **c (create)** : crée l'archive si elle n'existe pas.
- **s (index)** : écrit l'index des symboles (équivaut à `ranlib`), accélère l'édition de liens.

Utilisation :

```bash
gcc -Wall -Wextra main.c -L. -lstrutils -o prog_static
```

### Mécanisme de l'édition de liens statique
- **Intégration directe** : le lieur extrait le code objet (`.o`) de l'archive et le copie physiquement dans l'exécutable.
- **Exécutable autonome** : la suppression de l'archive `.a` après la compilation n'affecte pas le programme.

### Intérêts
- **Gain de temps de compilation** : la bibliothèque est compilée une fois, seul `main.c` est recompilé à chaque modification.
- **Syntaxe allégée** : `-lstrutils` évite de lister des dizaines de `.o` dans le Makefile.
- **Protection de la propriété intellectuelle** : seul le client reçoit les `.h` et le binaire `.a` (implémentation `.c` secrète).
- **Optimisation mémoire (embarqué)** : édition de liens **sélective** — seuls les modules `.o` contenant les fonctions réellement appelées sont copiés.