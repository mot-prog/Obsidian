```c
int putc(int c, FILE *stream);
```
Write a character.
Is equivalent to [[fputc]] except that it may be implemented as a macro which evaluates `stream` more than once.

Associated to :
[[fputc]]
[[fputs]]
[[puts]]
[[fputs]]
[[putchar]]
