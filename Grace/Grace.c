#include <stdio.h>
/* Grace Quine */
#define NAME "Grace_kid.c"
#define MODE "w+"
#define FT_MAIN(X) int main(void){FILE* fd=fopen(NAME, MODE);const char *s="#include <stdio.h>%c/* Grace Quine */%c#define NAME %cGrace_kid.c%c%c#define MODE %cw+%c%c#define FT_MAIN(X) int main(void){FILE* fd=fopen(NAME, MODE);const char *s=%c%s%c;fprintf(fd,s,10,10,34,34,10,34,34,10,34,s,34,10,10);fclose(fd);}%cFT_MAIN(NAME);%c";fprintf(fd,s,10,10,34,34,10,34,34,10,34,s,34,10,10);fclose(fd);}
FT_MAIN(NAME);
