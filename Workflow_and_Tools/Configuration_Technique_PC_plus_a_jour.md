---
tags: [workflow, tools]
---
# 🛠️ Configuration Technique (Manjaro)

Détails des commandes utilisées pour maintenir l'intégrité du système.

## 1. Le Lien Symbolique
Le dossier dans `Documents` n'est qu'un pointeur pour ne pas casser les scripts et l'habitude du terminal :
`ln -s "/home/manjaro_mot/Dropbox/DropsyncFiles/Obsidian_Vault/Polytech" ~/Documents/Polytech`
[[ln -s]]
## [[2. Exclusion Dropbox (xattr)]]
Pour éviter que Dropbox ne synchronise les objets Git (blobs, index) qui causent des conflits :
`attr -s com.dropbox.ignored -V 1 ~/Dropbox/DropsyncFiles/Obsidian_Vault/Polytech/.git`
[[attr]]

Retour à l'[[Architecture_Synchronisation|Accueil de l'Architecture]].