L'**ARP** (Address Resolution Protocol ou protocole de résolution d'adresse) est un protocole fondamental dans les réseaux informatiques qui permet de faire correspondre une adresse IP (logique, de couche 3) à une adresse MAC (physique, de couche 2).

# Envoi paquet ARP

- MAC destination (On envoit à tout le monde):
ff ff ff ff ff ff 

- MAC source :
00 11 11 11 11 02

- Protocole ARP:
08 06

- Type de matériel:
00 01

- IpV4:
08 00

- Maddr_Len :
06

- Laddr_en:
04

- Opération (internet):
00 01

- Maddr_emetteur:
00 11 11 11 11 02

- Laddr_emeteur:
172.26.145.102
ac 1a 91 66

- Maddr_cible (on connait pas justement):
00 00 00 00 00 00

- Laddr_cible:
172.26.145.62
ac 1a 91 3e

- On execute sur notre machine :
```bash
sudo ether -i bridge -s
ff ff ff ff ff ff 00 11 11 11 11 02 08 06 00 01 08 00 06 04 00 01 00 11 11 11 11 02 ac 1a 91 66 00 00 00 00 00 00 ac 1a 91 3e
```

- On envoit à la Zabeth12 (`host zabeth12`). On recoit ce paquet :
```bash
Packet received at Mon Sep 14 15:35:12 2026
00 11 11 11 11 02 20 3a 43 04 5f 99 08 06 00 01 
08 00 06 04 00 02 20 3a 43 04 5f 99 ac 1a 91 3e 
00 11 11 11 11 02 ac 1a 91 66 00 00 00 00 00 00 
00 00 00 00 00 00 00 00 00 00 00 00 
```
- On recoit bien sont adresse MAC :
```bash
20 3a 43 04 5f 99
```

# Réponse paquet ARP