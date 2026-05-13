#include <cs50.h>
#include <stdio.h>

float mult_two_float(float x, float y);
int main(void)
{
	float z;
#define MAX_LOOP 100
	int p = 1;
	for (float i = 1, j = i + 1; i < MAX_LOOP; i++, p++) {
		z = mult_two_float(i, j);
		printf("%i,%.3f\n", p, z);
	}
}
float mult_two_float(float x, float y) { return x * y; }
