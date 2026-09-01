---
tags: [programming, c, stdlib]
---
```c
int sscanf(const char *restrict str, const char *restrict format, ...);
```

Lit `str`, suivant le format `format` et le stock dans des variables comme un `scanf`.


> [!EXAMPLE] [[Polytech/S6/SD/TP/TP|TP]]
> ```c
> void scan_season(char filename[], struct nba_season_t *s)
>{
>int size = 50000;
>char string[size];
>char date[11];
>char t1[4];
>char t2[4];
>int s1, s2, sf;
>FILE *nba;
>s->last = -1;
>nba = fopen(filename, "r");
>if (nba != NULL)
>{
>	while (fgets(string, size, nba) != NULL)
>	{
>	sscanf(string, "%[^,],%[^,],%[^,],%d,%d,%d", date, t1, t2, &s1, &s2, &sf);
>	struct nba_game_t game;
>	struct date_t structdate;
>	sscanf(date, "%d-%d-%d", &structdate.day, &structdate.month, &structdate.year);
>	game.date = structdate;
>	strcpy(game.team1, t1);
>	strcpy(game.team2, t2);
>	game.score1 = s1;
>	game.score2 = s2;
>	game.total_rating = sf;
>
>	add_game(game, s);
>	}
>}
>else
>	printf("Can't open the file %s", filename);
>}
>```

> [!SUCCESS] `sscanf(string, "%[^,],%[^,],%[^,],%d,%d,%d", date, t1, t2, &s1, &s2, &sf);`
>Prend chaque éléments séparés par une `,` et les stocke dans la variable respective. Ces variables ont la bonnes taille initialement.

>[!success] `sscanf(date, "%d-%d-%d", &structdate.day, &structdate.month, &structdate.year);`
>Fait la même chose avec une date mais cette fois ci avec le charctère `-`.

>[!info] `%[^,]`
>Lit tout les caractères jusqu'à une `,`.

