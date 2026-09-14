Composition of an ip address :
![[ip adress]]

Masque de sous réseau : nombre de bit qu'on attribut  à l'@ du réseau. 
(ex : ci-dessus l'addresse ip à un masque de sous réseau de 16 bits)

**types de masques :**
* 8 bits (/8) : 1 $\rightarrow$  127
* 16 bits (/16) : 128 $\rightarrow$  191
* 24 bits (/24) : 192 $\rightarrow$  ...

DHCP : Dynamic Host Configuration Protocol
demande une address. Un ou plusieurs serveurs répondent. Et dans ce cas le protocole répond à un, prend le masque. Si le masque de la cible n'est pas la même, alors il faut passer par un routeur. 


>[!example] Réseau de 192.168.3.0/24 doit  être subdivisé en 5 VLAN différents. lpouvoir contenir au moins 63 machines 
>![[exerccie_ip]]

MASQUE =  tout les bits à 1 de mon réseau
>[!example] Combien d'ordinateurs peuvent faire partie du même sous-réseau si ce dernier  à un masque qui vaut 255.255.248.2
>![[exrcice2_ip]]

>[!example] Un administrateur réseau de classe C 192.168.0.0 doit subdiviser en différents sous-réseaux. Chaque sous_réseaux correspondra à un VLAN particulier. Un sous-réseau comportera 32 machines, 2 sous-réseaux 16 machines et un dernier 12 machines. DOnnez la valeur des masques pour chacun des sous-réseaux et l'adresse de réseau correspondante.
>![[exercice3_ip]]

