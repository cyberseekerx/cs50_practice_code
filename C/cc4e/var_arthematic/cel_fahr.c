#include <stdio.h>
#define LOWER 0;
#define UPPER 300
#define STEP 20

int main()
{
  float cel , fahr;

  cel = LOWER;
  printf(" celceius fahriet\n");
  while(cel <= UPPER){
    fahr = (5.0/9.0) * (cel+32);
    printf("%4.0f\t%10.4f\n",cel,fahr);
    cel = cel + STEP;

  }
  

}
