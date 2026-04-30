#include <cs50.h>
#include <stdio.h>

float avarage(int length, int numbers[]);

int main()
{
  const int N = 3;
  int scores[N];
  for (int i = 0; i < N; i++)
    do
       { 
        scores[i] = get_int("scores: ");
       }
       while(scores[i] < 0);
  printf("Avarage: %f\n", avarage(N, scores));
}

float avarage(int length, int numbers[])
{ 
  int sum = 0;
  for (int i = 0; i < length; i++)
  {
      sum += numbers[i];
  }
  return sum/(float)length;
}
