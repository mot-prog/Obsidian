```c
int fscanf(FILE *restrict stream, const char *restrict format, ...);
```
* Works as a `scanf` but for a `FILE*`. 
* Can not skip parts in the `FILE*`.
* Returns the number of elements read successfully.