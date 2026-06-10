#include <cs50.h>
#include <stdio.h>

 typedef struct {
   int x, y;
 } Point;

int main(void)
{
	Point co[2];
	co[0].x = get_int("what is the value of x ");
	co[0].y = get_int("what is the value of y ");
	printf("\n");
	for (int i = 0; i < 1; i++)
	{
		printf("add:%
	 
		printf("subtract: %i\n", co[i].x - co[i].y);
		printf("mult : %i\n", co[i].x * co[i].y);
	}
}
