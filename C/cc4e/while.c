#include <stdio.h>
#include <cs50.h>

int main(void){
  int n;
  int i;
  do 
  {
    n = get_int("what is the value of n(as in what how many loops do you want) ");
  }
  while (n < 0);

  for (i = 0; i < n; i++)
  {
    printf("meow\n");

  }
  printf("%i",i);
}
