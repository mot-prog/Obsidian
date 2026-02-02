```c
int fprintf(FILE *restrict stream, const char *restrict format, ...);
```
* Works as a `printf` but for a `FILE*`. 
* Predefined values of type `FILE*`:
	1. `stdin` : standard input;
	2. `stdout` : standard output;
	3. `stderr`: standard error;
