---
aliases:
  - "OSINT"
  - "Géolocalisation par image"
  - "Géolocalisation par vidéo"
  - "Recherche de lieu"
  - "Google Lens"
tags:
  - security
  - osint
  - geolocation
  - forensics
  - ctf
related: "[[binwalk]]"
---
# OSINT : géolocalisation via images et vidéos

Sources : [[Polytech/S6/CN/TP/Recherches_lieu_via images_et_videos|Recherches lieu via images et vidéos]] · [[Polytech/S6/CN/TP/TP|TP CN]]

## Techniques pour les **images**
- **Google Lens** : très puissant pour identifier un lieu.
- Regarder les **détails** de l'image avec [[binwalk]] ou [[media]] (métadonnées, coordonnées GPS…).

>[!tip] Exemple
>[[Polytech/S6/CN/TP/Image1/trouve|Image1]] : 34 Rue des Ursulines, Tourcoing — les coordonnées étaient dans les **informations de l'image** (métadonnées).

## Techniques pour les **vidéos**
- Prendre des **captures d'écran** sur les images clés, puis les scanner avec **Google Lens** pour trouver un lien.
- Sinon, utiliser **Gemini** pour trouver des indices dans les images.