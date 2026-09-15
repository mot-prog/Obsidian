---
aliases:
  - "USB-C"
  - "Classes USB"
  - "Connecteurs USB"
  - "Communication USB"
  - "lsusb"
  - "Périphériques USB"
tags:
  - hardware
  - usb
  - embedded
  - linux
related: "[[lusb]]"
---

# USB

Sources : [[Connecteurs USB]] · [[Ordre code]] · [[Polytech/S6/OS/Chapitre 1|OS Chapitre 1]]

## Principes généraux

- **Paire différentielle D+/D-** : on regarde les signaux *entre* les 2 paires. Alimentées en **3.3V**.
- Un **contrôleur** initie toujours la conversation vis-à-vis d'un **périphérique**.
  >[!example] Clavier
  >Le clavier attend que le microcontrôleur fasse le scan des interruptions avant d'exécuter la demande. *Test :* 2 claviers branchés en même temps — sur MAJ sur l'un, la lumière de l'autre clignote en même temps.

## USB-C

* 4 paires différentielles
* 2 liaisons série haute vitesse
* **GND + VBUS** : récupèrent la puissance sur le port
* **CC1 + VCONN** : paire différentielle de dialogue — le périphérique y demande la tension dont il a besoin (microcontrôleur intégré au port)
* **SBU1 + SBU2** : 6ᵉ paire différentielle — pas de fonction particulière, usage libre

## Classes de périphériques

| Classe | Description | Exemple |
| --- | --- | --- |
| 00h | Inconnu | Spécifique |
| 01h | Audio | Carte son |
| 02h | Communications | Carte réseau |
| 03h | Human Interface Device (HID) | Clavier |
| 05h | Physical Interface Device (PID) | Équipement à retour de force |
| 06h | Image | Webcam |
| 07h | Printer | Imprimante |
| 08h | Mass storage | Clef USB |
| 09h | USB hub | Répéteur USB |
| 0Bh | Smart Card | Lecteur de carte |
| 0Dh | Content security | Lecteur d'empreinte digitale |
| 0Eh | Video | Webcam |
| 0Fh | Personal Healthcare | Tensiomètre |
| E0h | Wireless Controller | Adaptateur Bluetooth |

## Lire un périphérique avec `lsusb`

```bash
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 008: ID 25a7:fa61 Areson Technology Corp Elecom Co., Ltd MR-K013 Multicard Reader
Bus 001 Device 009: ID 1532:0098 Razer USA, Ltd Razer DeathAdder Essential
```

- **ID** = `fabriquant : produit`
- **Device** : numéro unique du périphérique
- **Interface** : classe du périphérique
- **Endpoint descriptor** : point d'accès avec lequel on communique. Le **bit de poids fort** indique si c'est un canal **IN ou OUT** (DDR sur l'AVR). **bInterval** : fréquence de scrutation du périphérique (tous les x ms).

```bash
lsusb -vvvv -d 1532:0098   # description détaillée du device
```

>[!remarque] L'endpoint 0
>Un clavier est un périphérique INPUT… pourtant contrôlable par le PC : tous les périphériques USB ont un **endpoint 0** permettant d'être IN et OUT à la fois. On ne l'utilise pas tout le temps car il se comporte comme une **interruption** (priorité trop importante).

## Modes de communication

1. **Par interruption** (le plus courant)
2. **Isochrone** : débit réservé (vidéo)
3. **Volume / Bulk** : débit maximal (transfert)
4. **Contrôle** : commande courte avec réponse (souris, clavier)

Ordre de communication :
1. À qui je m'adresse (*address*)
2. J'envoie les octets

## Programmation : ordre du code

1. Initialiser la librairie
2. Boucler sur toutes les connexions (id vendeur + id produit) → pointeur sur USB device
3. `libusb set configuration`
4. `libusb open device / handle` (récupérer l'interface)
5. Trouver le point d'accès dans la structure "configuration" → on peut communiquer avec le port

**LUFA** : une fonction dans la boucle principale doit appeler `usb_USBTask` (ou ne pas bloquer cette fonction) pour lire la boucle infinie.

## Éjection USB (cache d'écriture)

Éjecter l'USB avant de déconnecter la clef : **tous les octets ne sont pas forcément écrits** sur la clef quand on la retire directement. L'éjection garantit que le cache d'écriture est vide → éviter la corruption.