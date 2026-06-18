```bash
USE_POWERLINE="true"  
# Has weird character width  
# Example:  
#    is not a diamond  
HAS_WIDECHARS="false"  
# Source manjaro-zsh-configuration  
if [[ -e /usr/share/zsh/manjaro-zsh-config ]]; then  
 source /usr/share/zsh/manjaro-zsh-config  
fi  
# Use manjaro zsh prompt  
if [[ -e /usr/share/zsh/manjaro-zsh-prompt ]]; then  
 source /usr/share/zsh/manjaro-zsh-prompt  
fi  
fastfetch  
alias open_ssh='gocryptfs ~/.coffre ~/acces_coffre'  
alias close_ssh='fusermount -u ~/acces_coffre'  
alias e='exit'  
alias s='systemctl suspend'  
alias sync='~/sync.sh'  
alias spell='~/spell.sh'  
alias def='~/def.sh'  
alias trans='~/translate.sh'  
alias trad='~/translate.sh -f'  
alias autoclick='~/autoclicker.py &'  
alias temp='sensors'  
alias arsenic='ssh mterrier@portier.polytech-lille.fr -p2222'  
alias BDD='ssh mterrier@portier.polytech-lille.fr -p2222 && ssh kohm@172.26.77.5'  
alias bot='~/Discord/DJ_monkey/start.sh'  
alias bot_error='cat ~/Discord/DJ_monkey/bot.log'
```