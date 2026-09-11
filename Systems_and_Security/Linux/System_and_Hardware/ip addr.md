```bash
ip addr  
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000  
   link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00  
   inet 127.0.0.1/8 scope host lo  
      valid_lft forever preferred_lft forever  
   inet6 ::1/128 scope host noprefixroute    
      valid_lft forever preferred_lft forever  
2: enp8s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000  
   link/ether 08:8f:c3:1f:59:4a brd ff:ff:ff:ff:ff:ff  
   altname enx088fc31f594a  
3: wlp0s20f3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000  
   link/ether ca:41:78:db:ef:38 brd ff:ff:ff:ff:ff:ff permaddr 90:cc:df:07:c5:ba  
   altname wlx90ccdf07c5ba  
   inet 172.26.177.50/22 brd 172.26.179.255 scope global dynamic noprefixroute wlp0s20f3  
      valid_lft 2038sec preferred_lft 2038sec  
   inet6 fe80::9341:cf43:2d83:8b88/64 scope link noprefixroute    
      valid_lft forever preferred_lft forever  
4: tailscale0: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP> mtu 1280 qdisc fq_codel state UNKNOWN group default qlen 500  
   link/none    
   inet 100.124.135.103/32 scope global tailscale0  
      valid_lft forever preferred_lft forever  
   inet6 fd7a:115c:a1e0::fd38:8768/128 scope global    
      valid_lft forever preferred_lft forever  
   inet6 fe80::7876:3964:b5e7:8c2b/64 scope link stable-privacy proto kernel_ll    
      valid_lft forever preferred_lft forever  
5: ztsjspchmi: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 2800 qdisc fq_codel state UNKNOWN group default qlen 1000  
   link/ether 12:41:9b:d8:d5:c1 brd ff:ff:ff:ff:ff:ff  
   inet 10.125.43.25/24 brd 10.125.43.255 scope global ztsjspchmi  
      valid_lft forever preferred_lft forever  
   inet6 fe80::1041:9bff:fed8:d5c1/64 scope link proto kernel_ll    
      valid_lft forever preferred_lft forever
```

+ `lo` : interface loopback (locale). Si on communique à cette addresse, littéralement on "parle à soi-même". Utilisée pour les services qui tournent sur la machine elle-même.
+ `enp8s0` : interface Ethernet filaire (carte réseau physique). Actuellement `DOWN` (pas de câble branché, état `NO-CARRIER`).
+ `wlp0s20f3` : interface Wi-Fi (carte réseau sans fil physique). Actuellement `UP` et connectée à un réseau.
+ `tailscale0` : interface virtuelle Tailscale (réseau VPN mesh). Fournit une addresse IP stable (`100.124.135.103`) pour accéder à la machine depuis d'autres appareils du réseau Tailscale.
+ `ztsjspchmi` : interface virtuelle (probablement un VPN ZeroTier ou similaire). Addresse dans le réseau `10.125.43.0/24`.

## Champs principaux de la sortie

### Au niveau de l'interface (1ère ligne)
| Champ | Signification |
| --- | --- |
| `<FLAGS>` | État et modes de l'interface (ex: `UP`, `LOOPBACK`, `BROADCAST`, `MULTICAST`) |
| `mtu` | Maximum Transmission Unit — taille maximale d'un paquet en octets (1500 = standard, 65536 = loopback) |
| `qdisc` | Discipline de file d'attente (gestion de la mise en file des paquets) |
| `state` | État actuel : `UP`, `DOWN`, `UNKNOWN` |
| `qlen` | Longueur de la file d'attente des paquets |

### Au niveau de la couche 2 (link/ether)
| Champ | Signification |
| --- | --- |
| `link/ether` | Adresse MAC de l'interface |
| `brd` | Adresse de broadcast |
| `altname` | Nom alternatif de l'interface (symlink dans `/sys/class/net/`) |

### Au niveau de la couche 3 (inet / inet6)
| Champ | Signification |
| --- | --- |
| `inet` | Adresse IPv4 avec masque en notation CIDR (ex: `/22` = masque `255.255.252.0`) |
| `inet6` | Adresse IPv6 |
| `scope` | Portée : `host` (locale), `link` (réseau local), `global` (accessible depuis l'extérieur) |
| `brd` | Adresse de broadcast du sous-réseau |
| `valid_lft` | Durée de validité de l'adresse (lease DHCP) — `foreman` = permanente |
| `preferred_lft` | Durée pendant laquelle l'adresse est préférée |
| `dynamic` | Addresse obtenue par DHCP |
| `noprefixroute` | Ne crée pas automatiquement de route pour ce préfixe |

## Commandes utiles liées

```bash
# Afficher uniquement les adresses IPv4
ip -4 addr

# Afficher une interface spécifique
ip addr show wlp0s20f3

# Afficher les interfaces en détail (avec les compteurs de paquets)
ip -s link

# Renouveler une adresse DHCP
sudo dhclient wlp0s20f3

# Activer/Désactiver une interface
sudo ip link set enp8s0 up
sudo ip link set enp8s0 down
```