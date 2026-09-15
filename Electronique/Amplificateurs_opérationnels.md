---
aliases:
  - "AOP"
  - "Amplificateurs opérationnels"
  - "Amplificateur op"
  - "Contre-réaction"
  - "Sommateur inverseur"
  - "Sommateur non inverseur"
  - "Régime linéaire AOP"
tags:
  - electronique
  - AOP
  - amplificateurs
  - circuits
related: "[[Capteurs_et_conditionnement]]"
---

# Amplificateurs opérationnels (AOP)

Sources : [[Polytech/S6/CAO(Capteurs_et Amplificateurs_Operationels/pt3 La contre réaction|pt3]] · [[Polytech/S6/CAO(Capteurs_et Amplificateurs_Operationels/pt4 Les applications des AOP|pt4]] · [[Polytech/S6/CAO(Capteurs_et Amplificateurs_Operationels/Ref/Sommateur non inverseur|Sommateur non inverseur]]

ALI = **A**mplificateur **L**inéaire **I**ntégré.

## Contre-réaction (rétroaction)

* **Rétroaction sur le +** : le signal de sortie est amplifié encore et encore → au bout d'un moment, **régime de saturation**.
* **Rétroaction sur le −** : le signal reste compatible avec le signal d'entrée → **régime linéaire**.

>[!important] Gain indépendant de l'ampli op
>Le gain en tension $\frac{Vs}{Ve}$ du montage ne dépend **que des éléments de la boucle de retour** (rétroaction), pas de l'ampli op lui-même.

## Sommateur inverseur

$V- = \frac{V1/R1 + V2/R2 + V3/R3 + Vs/R}{1/R1 + 1/R2 + 1/R3 + 1/R}$,  $V+ = 0$

$$Vs = -R\left(\frac{V1}{R1} + \frac{V2}{R2} + \frac{V3}{R3}\right)$$

Si $R1 = R2 = R3$ : $Vs = -(V1 + V2 + V3)$

## Sommateur non inverseur

![[Sommateur non inverseur]]

$V- = \frac{R1}{R1+R2}Vs$ ;  $V+ = \frac{V1+V2}{2}$

$$Vs = \frac{R1+R2}{2R1}(V1+V2)$$