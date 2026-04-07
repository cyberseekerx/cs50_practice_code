#include <stdio.h>

int main()
{
  int c;
  printf("Enter name");
  c = getchar();
  printf("\nhello, ");
  while(c != EOF){
    putchar(c);
    c = getchar();
  } 

}
