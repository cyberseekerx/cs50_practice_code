#include <stdio.h>
#include <cs50.h>

int Factorial(int n);
int main(void)
{
	int n = get_int("Factorial of: ");
	printf("%i\n",Factorial(n));
	for (int i = 2; i <= n;i++)
	{
		
		fact = fact * i;
	}
	printf("%i",fact);


}

int Factorial(int n)
{
	if ( n == 0 ) 
	{
		return 1;
	}
	return n * Factorial(n - 1);
}
