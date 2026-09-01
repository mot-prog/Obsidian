# 🏗️ Architecture du Vault Polytech et des vault obsidian

Ce fichier résume la **synchronisation** d'**Obsidian** sur mon téléphone et mes PC via **Dropbox**.

## Concept Global
Le dossier est un **dépôt Git localisé physiquement dans Dropbox** pour permettre la synchronisation en temps réel vers **Android**, tout en restant accessible via un chemin standard sur Linux.

## Liens Logiques
- [[Configuration_Technique_PC_plus_a_jour]] : Commandes ZSH et attributs de fichiers.
- [[Workflow_Quotidien]] : Procédure pour éviter les conflits entre Git et Dropsync.
- [[Prise_de_Notes_Mobile]] : Optimisation pour le clavier BT et Excalidraw.

## Structure des Chemins
- **Source Réelle** : `~/Dropbox/DropsyncFiles/Obsidian_Vault/Polytech`
- **Point d'Entrée Git** : `~/Documents/Polytech` (via Symlink)