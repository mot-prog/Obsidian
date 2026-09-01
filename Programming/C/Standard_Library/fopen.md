---
tags: [programming, c, stdlib]
---
```c
FILE *fopen(const char *restrict path, const char *restrict mode);
```
Retourne `NULL` si ne parvient pas à ouvrir le fichier.
###mode :
* `"r"`=READ
* `"w"`=WRITE
* `"a"`=APPEND
**Exemple**: utilisé dans [[Polytech/S6/SD/TP/TP|TP]] : 
```c
FILE *nba;
nba = fopen(filename, "r");
``` 

