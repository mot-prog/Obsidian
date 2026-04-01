# --- 1. INITIALISATION & AUTOCOMPLÉTION ---
autoload -Uz compinit
compinit
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'

# --- 2. CONFIGURATION GIT ---
autoload -Uz vcs_info
zstyle ':vcs_info:*' enable git
zstyle ':vcs_info:*' check-for-changes true
zstyle ':vcs_info:git:*' unstagedstr '%F{red}●%f'
zstyle ':vcs_info:git:*' stagedstr '%F{green}●%f'
zstyle ':vcs_info:git:*' formats ' %B%F{yellow}(%b)%f%u%c%b'
zstyle ':vcs_info:git:*' actionformats ' %B%F{yellow}(%b|%a)%f%u%c%b'

precmd() {
    vcs_info
}

# --- 3. PROMPT ---
setopt PROMPT_SUBST
PROMPT='%B%F{cyan}%n@%m%f:%F{magenta}%~%f${vcs_info_msg_0_}$ %b'

# --- 4. COLORATION SYNTAXIQUE (SPÉCIFIQUE DEBIAN) ---
# Le chemin change ici par rapport à Manjaro
if [ -f /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh ]; then
    source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
    
    # Configuration des couleurs (Orange pour les commandes)
    ZSH_HIGHLIGHT_STYLES[command]='fg=208,bold'
    ZSH_HIGHLIGHT_STYLES[alias]='fg=208,bold'
    ZSH_HIGHLIGHT_STYLES[builtin]='fg=208,bold'
fi

# --- 5. HISTORIQUE & ALIAS ---
HISTFILE=~/.zsh_history
HISTSIZE=1000
SAVEHIST=1000
setopt APPEND_HISTORY
setopt SHARE_HISTORY
setopt HIST_IGNORE_DUPS
setopt HIST_IGNORE_SPACE
setopt HIST_REDUCE_BLANKS
setopt CORRECT

if [ -f /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh ]; then
    source /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh
    ZSH_AUTOSUGGEST_STRATEGY=(history completion)
fi

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias ll='ls -l'
alias la='ls -la'
bindkey -e

fastfetch
# --- Auto-détection ID Clavier ---

# On récupère l'ID dynamiquement
# awk cherche la ligne contenant le nom et extrait le nombre après "id="
KEYBOARD_ID=$(xinput list | grep "AT Translated Set 2 keyboard" | grep -o 'id=[0-9]*' | cut -d= -f2)

# On vérifie si un ID a bien été trouvé pour éviter les erreurs
if [ -n "$KEYBOARD_ID" ]; then
    alias off='xinput set-prop $(xinput list | grep "AT Translated Set 2 keyboard" | grep -o "id=[0-9]*" | cut -d= -f2) "Device Enabled" 0'
alias on='xinput set-prop $(xinput list | grep "AT Translated Set 2 keyboard" | grep -o "id=[0-9]*" | cut -d= -f2) "Device Enabled" 1'
else
    echo "Erreur : Clavier interne non détecté pour les alias off/on."
fi

alias e="exit"
alias s='systemctl suspend'  #==Sleep
alias sync='~/sync.sh'
