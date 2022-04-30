#include <stdio.h>

// variable declaration:
extern char a, b, c;

int main()
{
    char a = 'x';
    char b = 'm';
    char c = 'l';

    printf("%c%c%c\n", c, b, a);

    return 0;

}
