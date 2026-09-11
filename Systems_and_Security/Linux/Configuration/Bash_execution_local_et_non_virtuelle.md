---
tags: [linux, configuration]
---
```bash
. ./script.sh
```
Cela va executer le script dans le terminal actuel et non le terminal virtuel qu'il aurait lancé normalement.

>[!example] test.sh
>```bash
>#!/bin/bash
>cd Documents
pwd
cd /bin
pwd
>```

![[Pasted image 20260427142225.png]]

