>string editor

![[Pasted image 20260330164547.png]]
`valeur = \1` signifie qu'on affiche "valeur = " la première parenthèse qui précède la commande. En l’occurrence ici i'l n'y en a qu'une. 

```bash
echo Ceci est un poids de 456 KG | sed -e 's/^[^0-9]*\([0-9][0-9]*\)\(.*\).*/valeur = \1\n le reste = \2/'
```

>[!remarque]
>On peut changer le caractère `/` après le `s` pour ne pas s'embêter avec les `\`. On peut utiliser un caractère peut utilisé comme `#`.  Cf [[tp1]]

