#include <stdio.h>
#include <cs50.h>

int main()
{
  int max_loop = get_int("amount of loops ");
  int loop_count;
  
  int x = get_int("value of x");
  int y = get_int("value of y");

  for(loop_count = 1;max_loop >= loop_count;loop_count++)
    printf("%i\n",loop_count);

}