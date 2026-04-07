#include <stdio.h>
#include <cs50.h>

int main(void)
{   int count;
    int amount;
    do 
    {
        amount = get_int("Changed owed: ");

    }
    while (amount < 0);
    for (count = 0; amount > 0; count ++)
    {
    if (amount >= 25){
        amount -= 25;
    }
    else if (amount >= 10)
    {
        amount -= 10;
    }
    else if (amount >= 5)
    {
        amount -= 5;
        }
    else 
    {
            amount --;
        }
    }
    printf("%d",count);
}
