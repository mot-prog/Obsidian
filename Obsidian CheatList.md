# 📝 Aide-mémoire Obsidian & Markdown

Ce fichier recense les balises les plus utiles pour structurer tes cours d'ingénierie et de code.

---

## 1. Les Callouts (Encadrés)

La syntaxe de base est `> [!TAG] Titre`.
*Astuce : Ajoute un `-` ou un `+` après le tag (ex: `[!INFO]-`) pour rendre l'encadré repliable par défaut.*

### 🔵 Informatif (Bleu)

> [!INFO] Information
> Syntaxe : `> [!INFO] Titre`
> Utile pour les définitions ou le contexte global.

> [!NOTE] Note
> Syntaxe : `> [!NOTE] Titre`
> Similaire à info, souvent utilisé pour des remarques en marge.

### 🟢 Succès & Astuces (Vert)

> [!SUCCESS] Réussite / Validé
> Syntaxe : `> [!SUCCESS] Titre`
> Parfait pour afficher le résultat correct d'un code ou un test réussi.

> [!TIP] Astuce / Conseil
> Syntaxe : `> [!TIP] Titre`
> Utile pour les "Best Practices" ou les raccourcis.

> [!DONE] Fait / Terminé
> Syntaxe : `> [!DONE] Titre`
> Pour marquer une tâche ou un module complété.

### 🟡 Attention (Jaune/Orange)

> [!WARNING] Attention
> Syntaxe : `> [!WARNING] Titre`
> Pour les points de vigilance (ex: gestion mémoire manuelle).

> [!QUESTION] Question / À creuser
> Syntaxe : `> [!QUESTION] Titre`
> Utile pour noter une question à poser au prof ou à rechercher plus tard.

### 🔴 Danger & Erreurs (Rouge)

> [!ERROR] Erreur / Echec
> Syntaxe : `> [!ERROR] Titre` ou `> [!FAILURE]`
> Pour indiquer une sortie d'erreur ou un crash.

> [!BUG] Bug
> Syntaxe : `> [!BUG] Titre`
> Parfait pour signaler un comportement inattendu ou une faille connue.

> [!DANGER] Danger / Critique
> Syntaxe : `> [!DANGER] Titre`
> Pour les failles de sécurité critiques (Buffer Overflow, SegFault).

### 🟣 Exemples & Contenu (Violet/Gris)
Pour illustrer tes cours.

> [!EXAMPLE] Exemple
> Syntaxe : `> [!EXAMPLE] Titre`
> L'endroit idéal pour mettre tes snippets de code.

> [!QUOTE] Citation
> Syntaxe : `> [!QUOTE] Titre`
> Pour citer une documentation (ex: man pages).

---

## 2. Structure du Texte (Markdown Standard)

# Titre 1 
## Titre 2 
### Titre 3 
#### Titre 4 

**Texte en gras**
*Texte en italique*
~~Texte barré~~
==Texte surligné==
- Élément 1
- Élément 2
	- Sous-élément

1. étape 1
2. étape 2

- [ ] A faire
- [X] Fait 

```c
#include <stdio.h>
int main() {//exemple
    return 0;
}
```
```nasm 
section .text global _start
```
`code en ligne`
[Lien externe](https://lol.fandom.com/wiki/Faker)
![Lien interne](file:///home/manjaro_mot/T1_Faker_2026_LCK_Cup.webp)

#tags 

--- 

>[!tip] 

>[!done] 

>[!danger] 

>[! warning] 

>[!question]
>

>[!quote] 

>[!example] 

>[!info] 

>[!note] 

>[!bug] 

