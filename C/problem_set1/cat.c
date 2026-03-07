#include <stdio.h>
#include <cs50.h>

void meow(void);

int main(void)
{
  for(int i = 0; i < 3; i++)
  {
    meow();
  }
}













void meow(int n)
{
  for (int i = 0; i < n; i++)
  printf("meow\n");
}

