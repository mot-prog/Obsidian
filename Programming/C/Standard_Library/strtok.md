---
tags: [programming, c, stdlib]
---
```c
#include <string.h>  
char *strtok(char *_Nullable restrict str, const char *restrict delim);
```

>[!example] 
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, world! This is a test.";
    char *token;

    // First call: extract the first token using comma, space, and exclamation as delimiters
    token = strtok(str, ", !");

    // Loop through remaining tokens
    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, ", !");
    }

    return 0;
}   
```

```
Hello
world
This
is
a
test   
```