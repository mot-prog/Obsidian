---
aliases:
  - "Capteurs"
  - "Circuits de conditionnement"
  - "Pont de Wheatstone"
  - "Montage en pont"
  - "LM35"
  - "Capteurs actifs et passifs"
tags:
  - electronique
  - capteurs
  - mesures
  - AOP
related: "[[Amplificateurs_opérationnels]]"
---

# Capteurs et circuits de conditionnement

Sources : [[Polytech/S6/CAO(Capteurs_et Amplificateurs_Operationels/pt1 Circuits_de_conditionnements|pt1]] · [[Polytech/S6/CAO(Capteurs_et Amplificateurs_Operationels/pt2 Circuits_de_conditionnements|pt2]] · [[Polytech/S6/CAO(Capteurs_et Amplificateurs_Operationels/Introduction|Introduction]]

## Capteurs actifs vs passifs

- **Capteur actif** : doit être **alimenté** pour fonctionner (ex : photodiode).
- **Capteur passif** : pas besoin d'alimentation. Ex : capteur de pression / **résistance flexible** — sa résistance change avec une variation *mécanique* (non électrique).

## Ordres de grandeur

* $R_{générateur} \approx 50\ \Omega$
* $R_{oscillo} \approx 1\ M\Omega$

$R_o \gg R_g$ pour qu'il y ait très peu de courant → la mesure se rapproche de la valeur réelle.

## Caractéristique d'un capteur (ex : LM35)

| Métrique | Valeur |
| --- | --- |
| Limite d'utilisation | $-55°C$ à $50°C$ |
| Étendue de mesures | $205°C$ |
| Résolution | $0,5°C$ |
| Précision | $\pm 1/4 °C$ |
| Linéarité | non linéaire |

Voir [[lm35.pdf]] (p.8).

## Diviseur de tension avec capteur résistif

$Vm = \frac{Rx.E}{R1 + Rx}$  (si $Rx \ll Rc$, $Rc$ ≈ circuit ouvert)

**Variations** : $\Delta Vm = \frac{E}{4}\cdot\frac{\Delta Rx}{Rx0}$

## Montage en pont

* $Vm = Va - Vb$ ; $Rs = 0 \implies Vs = E$
* $Va = \frac{Rx}{Rx + R3}E$ ; $Vb = \frac{R2}{R2 + R1}E$
* $Vm = \left(\frac{Rx}{Rx+R3} - \frac{R2}{R2 + R1}\right)E$
* Si $R1=R2=R3=R0$ et $RX=R0+\Delta Rx$ :
  $Vm = \frac{\Delta Rx}{2(2R0 + \Delta Rx)}E \xrightarrow{\Delta Rx \ll 2R0} Vm = \frac{\Delta Rx E}{4R0}$

### Exercice capteur de pression (linéaire)
1. $V = \frac{R - R0}{2(R + R0)}E$
2. On suppose $R = aP + b$ — mesures : $P=0$ mb $\to R=1000\ \Omega$, $P=4000$ mb $\to R=3000\ \Omega$
   $\implies a=\frac{1}{2}$, $b=1000$ → $R = \frac{1}{2}P + 1000$
3. À $V=0$ : $R=R0$, $P=1013$ mb $\implies R0 = \frac{1013}{2}+1000 \approx 1506\ \Omega$
4. La relation $V = f(P)$ n'est **pas linéaire** :
   $V = \frac{0,5P - 506}{2(0,5P + 2506)}E$
5. Avec $E=12V$ : à $P=900$ mb → $V \approx -113,6$ mV (erreur 0,5 %) ; à $P=1100$ mb → $V \approx 86,4$ mV (erreur 0,69 %)

## ALI / AOP

ALI = Amplificateur Linéaire Intégré. Voir [[Amplificateurs_opérationnels]] (contre-réaction, sommateurs). Datasheet : le LM741 → https://www.ti.com/lit/ds/symlink/lm741.pdf