# 🔄 Workflow : PC ↔️ Mobile

Procédure à suivre pour garantir la cohérence des notes de cours.

## En cours (Mobile 📱)
1. Vérifier que **Dropsync** a fini la synchro montante en arrivant.
2. Utiliser le clavier Bluetooth pour la saisie rapide.
3. Créer des schémas de stack/mémoire via [[Excalidraw]].
4. **Important** : Ne pas toucher aux dossiers système `.git`.

## Git classique comme avant (PC 💻)
1. Laisser Dropbox télécharger les modifs du téléphone.
2. Ouvrir le terminal dans `~/Documents/Polytech`.
3. Effectuer le versionnage :
   - `git add .`
   - `git commit -m "Notes du cours de [Sujet]"`
   - `git push origin main`

## Sécurité
[[Configuration_Technique_PC#2. Exclusion Dropbox (xattr)|Ignorer le .git]] garantit que Git ne s'emmêle pas les pinceaux avec la synchro Cloud.