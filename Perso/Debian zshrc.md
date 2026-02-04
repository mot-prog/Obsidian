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
alias sync='cd ~/ && source .zshrc'  
  
./sync.sh
```
