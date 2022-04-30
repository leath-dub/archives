#include <stdio.h>

int main()
{
    double a, b, c, d, result;

    printf("Weight- item1:");
    scanf("\n%lf", &a);
    printf("No. of item1:");
    scanf("\n%lf", &b);
    printf("Weight- item2:");
    scanf("\n%lf", &c);
    printf("No. of item2:");
    scanf("\n%lf", &d);

    result = ((a * b + c * d) / (b + d));
    printf("%f\n", result);
    

    return 0;

}
