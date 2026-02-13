```bash
  GNU nano 8.4                         .zshrc                                   
SAVEHIST=1000
setopt APPEND_HISTORY
setopt SHARE_HISTORY
setopt HIST_IGNORE_DUPS

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias ll='ls -l'
alias la='ls -la'
bindkey -e

fastfetch
alias e="exit"
alias off="xinput set-prop 13 'Device Enabled' 0"
alias on="xinput set-prop 13 'Device Enabled' 1"
alias s='systemctl suspend'  #==Sleep
alias sync='~/sync.sh'

# --- Auto-détection ID Clavier ---
# On récupère l'ID dynamiquement
# awk cherche la ligne contenant le nom et extrait le nombre après "id="
KEYBOARD_ID=$(xinput list | grep "AT Translated Set 2 keyboard" | grep -o 'id=[>

# On vérifie si un ID a bien été trouvé pour éviter les erreurs
if [ -n "$KEYBOARD_ID" ]; then
    alias off="xinput set-prop $KEYBOARD_ID 'Device Enabled' 0 && echo 'Clavier>
    alias on="xinput set-prop $KEYBOARD_ID 'Device Enabled' 1 && echo 'Clavier >
else
    echo "Erreur : Clavier interne non détecté pour les alias off/on."
fi

```
