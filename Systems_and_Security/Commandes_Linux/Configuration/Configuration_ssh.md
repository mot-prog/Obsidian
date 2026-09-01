---
tags: [linux, configuration]
---
#key #ssh
# Lien git
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

# Génération d'un clef ssh
```bash
ssh-keygen -t ed25519 -C "name"
```

#### récupération de la clef 
```bash
cat ~/.ssh/id_ed25519.pub
```

# Connexion ssh à distance

## Connexion polytech
```bash
ssh mterrier@portier.polytech-lille.fr -p2222
```

## Connexion Android
* Installer Termux sur F-droid
* Configurer le psw dans termux :
```bash
pkg update
pkg install openssh
sshd
passwd
```
* Recupérer le user 
```bash
whoami
```
* Récupérer l'ip du wifi (`ifconfig`)
* Connexion depuis le pc
```bash
ssh user@ip_address -p 8022 #By default its port 22 wich is forbidden in termux
```

