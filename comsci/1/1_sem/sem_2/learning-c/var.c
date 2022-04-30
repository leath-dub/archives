#include <stdio.h>

extern int a, b;
extern int c;
int main ();

int arse();

int main()
{
    int a = arse();

}

int arse() {
    int c;
    int a, b;

    a = 10;
    b = 20;

    c = a + b;

    printf("restlt %d\n", c);

    return     c;

}

