#include <stdio.h>
#include <cs50.h>


int fib(int n);
int main(void)
{
	int num = get_int("fib: ");
	printf("%i",fib(num));
}

int fib(int n)
{
	if (n == 0)
	{
		return 0;
	}
	if (n == 1)
	{
		return 1;
	}
	f = fib(n-1) + fib(n -2)
	printf("%i")
	return fib(n-1) + fib(n -2);
}
