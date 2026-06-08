```reference
file : ./Polytech/S6/SDA/TP/Makefile
lang : Makefile
fold : true
unwrap : false
title : Bioteos
```

Cré un fichier `build` si il n'existe pas ([[Mkdir -p]]). Range tout les `.0` et le `main`.
Les fichiers `.d`sont générés dans `gcc`par `-MMD`. Ils permettent de  lister les header associés à leurs fichiers `.c`. 
La ligne `-include $(wildcard build/*.d)`permet de "dire" à gcc d'inclure les headers. 
>[!remarque]
>Un fichier qui n'a pas de `.h` aura juste un `.d `vide.

On le retrouve dans [[Polytech/S6/SD/TP/TP|TP]].

