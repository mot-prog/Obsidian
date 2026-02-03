```bash
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="powerlevel10k/powerlevel10k"
Add wisely, as too many plugins slow down shell startup.

plugins=(git)

source $ZSH/oh-my-zsh.sh

  
as ohmyzsh="mate ~/.oh-my-zsh"

plugins=(git zsh-syntax-highlighting zsh-autosuggestions)

  

fastfetch

alias e='exit'

alias sync='cd ~/ && exec zsh'

  

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.

[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

  
./sync.sh


# Désactiver le backend gitstatusd qui pose problème sur Termux
POWERLEVEL9K_DISABLE_GITSTATUS=true
```