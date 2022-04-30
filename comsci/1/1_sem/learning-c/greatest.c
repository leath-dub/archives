#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, b, c;

    printf("first-int : ");
    scanf("\n%d", &a);
    printf("second-int: ");
    scanf("\n%d", &b);
    printf("third-int : ");
    scanf("\n%d", &c);

    printf("%d", ((abs(a - b) + abs(b - c)) + a + b + c) / 3);

    return 0;
}
