>[!example] Sur Android dans Termux
```bash
pkg install openssh
passwd    #mise en place sur mdp de la connexion ssh
sshd      #lancement du serveur
ifconfig  #on récupère l'ip du wifi
ssh -p <ip>
termux-wake-lock #utiliser le ssh avec le téléphone en veille
pkg update && pkg upgrade
```
