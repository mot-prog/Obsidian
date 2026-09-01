---
tags: [programming, c, debugging]
---
### On rajoute le -g pour utiliser gdb à la compilation
```bash
gcc -g fichier.c -o fichier
```
### Lancement de gdb
```bash
gdb ./fichier.c
```
### lancement du débugg
```bash
r
```
`run`
### Point d'arrêt
```bash
break 12
```
break at the line 12.
Mettre `c`comme `continue`pour passer au `break`.
## Avancer après un break
#### NEXT
```bash
n
```
Comme `next`. Il suffit de faire `enter`pour avancer ligne par ligne.
#### STEP
```bash
s
```
On rentre dans une fonction après un `next`.

## Affichage
#### PRINT
```bash
p i
p &i
p i + j
p f(k)
```
affiche la valeur de `i` (après un boucle par exemple). Affiche appel d'une fonction...
#### PILE
 ```bash
 where
 ```
Affiche l'état de la pile.
```bash
up
down
```
permet de naviguer dans la pile.

### FINISH
```bash
finish
```
Permet de sortir d'une fonction.