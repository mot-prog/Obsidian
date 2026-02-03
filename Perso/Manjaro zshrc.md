```bash
GNU nano 8.7                                    .zshrc                                                  
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
alias s='systemctl suspend'  #==Sleep
alias sync='cd ~/ && source .zshrc'  
  
./sync.sh
```