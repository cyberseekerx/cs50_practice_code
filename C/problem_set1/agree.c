#include <stdio.h>
#include <cs50.h>

int main(void)
{
  printf("do you agree? ");
  char c = get_char("Y/N ");

  if (c == 'y' || c =='Y')
  {
      printf("Agreed");
  }
  else 
{
      printf("Disagree");
  
}

