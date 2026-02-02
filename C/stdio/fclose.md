```c
int fclose(FILE *stream);
```
* Close a file when not used anymore.
* Closing the file deallocates memory assigned to handle the file.
* File to close specified as a `FILE*`. 