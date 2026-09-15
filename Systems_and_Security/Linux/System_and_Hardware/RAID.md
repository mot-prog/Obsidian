---
aliases:
  - "RAID 5"
  - "Redundant Array of Inexpensive Disks"
  - "Redondance disques"
tags:
  - storage
  - hardware
  - linux
  - raid
related: "[[Etat_de_vie_SDA_et_NVME]]"
---

# RAID

Sources : [[Polytech/S6/OS/RAID|RAID (OS)]]

**RAID** = **R**edundant **A**rray of **I**nexpensive **D**isks.

Principe : quand on écrit sur un disque, on écrit sur un autre en même temps. Différentes fonctions permettent de **reconstruire** le disque en cas de panne.

## RAID 5

Répartition des données et de la parité sur plusieurs disques : tolère la perte d'un disque sans perte de données.

![[Drawing 2026-02-16 17.59.35.excalidraw]]