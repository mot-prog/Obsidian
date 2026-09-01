```c
Char* *fgets(char s[restrict .size], int size, FILE *restrict stream)
```
Lit au plus `size-1` caractères depuis `stream` et les place dans `s`. La lecture s'arrête après `EOF` ou un  `\n`. Si un `\n` est lu, il est placé dans `s`. Un octet NULL final `\0` est placé après le dernier caractère dans `s`

Utilisé dans [[Polytech/S6/SD/TP/TP|TP]]
