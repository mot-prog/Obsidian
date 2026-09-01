---
tags: [personal]
---
```sh
#!/bin/bash
# chemin du fichier
cd /home/manjaro_mot/Documents/Obsidian/
# ==========================================
# CONFIGURATION
# ==========================================
# Nom du dossier de ton sous-module (ex: Polytech)
SUBMODULE_PATH="Polytech"

# Branche principale du sous-module (main ou master ?)
SUBMODULE_BRANCH="main"

# Message de commit par défaut (si aucun argument n'est donné)
DEFAULT_MSG_SUB="Polytech Update"
DEFAULT_MSG_PARENT="Obsidian Update"

# ==========================================
# COULEURS (Pour le retour visuel)
# ==========================================
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}=== Start of the syncronisation Obsidian/Polytech ===${NC}"

# ==========================================
# ÉTAPE 1 : PULL (Mise à jour depuis le Cloud)
# ==========================================
echo -e "${YELLOW}[1/4] Update of PARENT folder (Obsidian)...${NC}"
git pull
if [ $? -ne 0 ]; then
echo -e "${RED}Error when pulling the parent. Check connexion or conflits.${NC}"
exit 1
fi

echo -e "${YELLOW}[2/4] Update of the subfile ($SUBMODULE_PATH)...${NC}"
if [ -d "$SUBMODULE_PATH" ]; then
cd "$SUBMODULE_PATH" || exit
# ---------------------------------------------------------
# HACK TECHNIQUE : Fixer le "Detached HEAD"
# Les submodules pointent par défaut sur un commit (SHA), pas une branche.
# Pour pouvoir "pull" ou "push" plus tard, on doit forcer l'attachement à la branche.
# ---------------------------------------------------------
echo -e " -> Checkout to main '$SUBMODULE_BRANCH'..."
git checkout "$SUBMODULE_BRANCH" 2>/dev/null
echo -e " -> pull..."
git pull origin "$SUBMODULE_BRANCH"
cd ..
else
echo -e "${RED}Erreur : The subFile $SUBMODULE_PATH doesn't exists !${NC}"
exit 1
fi 

# ==========================================
# ÉTAPE 2 : PUSH (Envoi vers le Cloud)
# ==========================================
# On demande confirmation avant d'envoyer, pour éviter les erreurs.
echo -e "${CYAN}------------------------------------------------${NC}"
read -r -p "Do you want to push local files ? [(Y/n)] " response
response=${response:-Y} # Si vide, prend "Y" par défaut
echo # Nouvelle ligne
if [[ ! "$response" =~ ^[Yy]$ ]]; then
echo -e "${GREEN}Done (local updates).${NC}"
exit 0
fi

# ==========================================
# ÉTAPE 3 : TRAITEMENT INTELLIGENT DES COMMITS
# ==========================================

# --- A. SOUS-MODULE ---
cd "$SUBMODULE_PATH" || exit
# Vérifie s'il y a des changements (fichiers modifiés ou non trackés)
if [ -n "$(git status --porcelain)" ]; then
echo -e "${YELLOW}[Polytech] was modified.${NC}"
read -r -p " -> Commit message [$DEFAULT_MSG_SUB] : " MSG_SUB
MSG_SUB=${MSG_SUB:-$DEFAULT_MSG_SUB} # Utilise le défaut si vide

git add .
git commit -m "$MSG_SUB" --quiet
echo -e " -> Push to GitHub..."
git push origin "$SUBMODULE_BRANCH" --quiet
echo -e "${GREEN} -> Success !${NC}"

else
echo -e "${CYAN}[Polytech] Nothing to push (Clean folder).${NC}"
fi
cd ..

# --- B. PARENT ---
# Note : On doit check s'il y a des modifs dans les notes OU si le pointeur du submodule a bougé
if [ -n "$(git status --porcelain)" ]; then
echo -e "${YELLOW}[Obsidian Global] was modified.${NC}"
read -r -p " -> Commit message [$DEFAULT_MSG_PARENT] : " MSG_PARENT
MSG_PARENT=${MSG_PARENT:-$DEFAULT_MSG_PARENT}
  
git add .
git commit -m "$MSG_PARENT" --quiet
echo -e " -> Push to..."
git push --quiet
echo -e "${GREEN} -> Success !${NC}"
else
echo -e "${CYAN}[Obsidian Global] Nothing to push.${NC}"
fi

echo -e "${CYAN}=== All is syncronized ! ===${NC}"
```