---
aliases:
  - "Transistor émetteur commun"
  - "Emetteur commun"
  - "h11"
  - "Impédances transistor"
  - "Gain en courant transistor"
tags:
  - electronique
  - transistor
  - formules
  - systemes_embarques
related: "[[Amplificateurs_opérationnels]]"
---

# Transistor : montage émetteur commun

Sources : [[Polytech/S6/EG/Diapo 41 Note sur la page|Diapo 41 note]] · [[Polytech/S6/EG/Diapo 41 suite|Diapo 41 suite]]

## Résistance d'entrée $h_{11}$

Issue de la caractéristique exponentielle de la jonction base-émetteur :
$I_b = I_s\left(e^{\frac{qV_{be}}{kT}} - 1\right) \approx I_s e^{\frac{qV_{be}}{kT}}$

$$h_{11} = \frac{\beta V_T}{I_{C0}} \quad \text{avec } V_T = \frac{kT}{q} \approx 26\,\text{mV à 300K}$$

> [!info] $h_{11}$ varie selon le **point de polarisation** (dépend de $I_{C0}$).

## Impédance d'entrée $Z_e$

$$Z_e = R_p \parallel [h_{11} + \beta(R_e \parallel Z_{Ce})]$$

* $R_e$ **découplé** ($Z_{Ce} \to 0$) : $Z_e = R_p \parallel h_{11}$
* $R_e$ **non découplé** ($Z_{Ce} \to \infty$) : $Z_e = R_p \parallel (h_{11} + \beta R_e)$

## Gain en courant $A_{Icc}$

$$A_{Icc} = \frac{I_s}{I_e}\bigg|_{V_s=0} = \frac{\beta}{\frac{h_{11} + \beta(R_e \parallel Z_{Ce})}{R_p} + 1}$$

> [!summary] Résultats finaux
> **$R_e$ découplé :** $\dfrac{I_s}{I_e} = \dfrac{\beta R_p}{R_p + h_{11}}$
>
> **$R_e$ non découplé :** $\dfrac{I_s}{I_e} = \dfrac{\beta R_p}{\beta R_e + h_{11} + R_p}$

## Impédance de sortie $Z_s$

Avec $V_e = 0$ : maille d'entrée ⇒ $i_b = 0$ ⇒ $\beta i_b = 0$ (source commandée ouverte). Il ne reste que la résistance de collecteur vue de la sortie :

$$Z_s = R_c$$

## Gain en tension et fréquence

$$A_{vv} = \frac{V_s}{E_g} \approx \frac{-\beta R_c}{h_{11} + (R_e \parallel Z_{ce})\beta}$$

**Rôle de la capacité de découplage $C_e$ :**
* **En dynamique (HF)** : court-circuite $R_e$ → le gain **augmente**.
* **En statique (DC)** : circuit ouvert → $R_e$ stabilise le point de repos (contre les variations de température).

**Fonction de transfert (filtre "shelf")** :

$$A = A_0 \times \frac{1 + j\frac{\omega}{\omega_z}}{1 + j\frac{\omega}{\omega_p}}$$

* $\omega \to 0$ (BF) : gain faible (rétroaction par $R_e$).
* $\omega \to \infty$ (HF) : gain fort (découplage par $C_e$).

**Impédance d'émetteur selon la fréquence :**
1. $0 < f < f_{c1}$ : condensateur ouvert → impédance $= R_e$
2. $f_{c1} < f < f_{c2}$ : condensateur partiellement en court-circuit → inchangé
3. $f > f_{c2}$ : condensateur en court-circuit → impédance $\approx 0$