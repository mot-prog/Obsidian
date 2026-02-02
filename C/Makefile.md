```Makefile
run:build/main
	./build/main

build/%.o: %.c | build
	gcc -Wall -Wextra -c -o $@ $<

build/main: build/nba_season.o build/main.o | build
	gcc $^ -o $@

build/main.o: nba_season.h

build:
	mkdir -p build

.PHONY: run
```

Cré un fichier `build` si il n'existe pas ([[Mkdir -p]]). Range tout les `.0` et le `main`.
On le retrouve dans [[Polytech/S6/SD/TP/TP|TP]].

