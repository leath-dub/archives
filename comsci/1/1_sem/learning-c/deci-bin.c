#include <stdio.h>

int main()
{
    int num;
    int pwr = 1;
    int result = 0;

    scanf("%d", &num);

    while(num > 0)
    {
       result = result + (num % 2 * pwr);
       num = num / 2;
       pwr = pwr * 10;
    }

    printf("%d\n", result);
    return 0;
}
    
