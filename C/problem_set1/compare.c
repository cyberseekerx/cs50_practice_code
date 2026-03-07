#include <stdio.h>
#include <cs50.h> 

int main(void)
{
  int x = get_int("input x value");
  int y = get_int("intput y value");

  if (x < y)
  {
      printf("y is greater than x\n");
  }
  else if (x > y)
  {
      printf("y is less than x");
  }
  else
  {
       printf("y is equal to x ");
       }
  
}
