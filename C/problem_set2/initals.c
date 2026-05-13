#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
	printf("%i\n",argc);
	for (int i = 1; i < argc; i++)
	{
		if (argv[i][0] >= 'a' && argv[i][0] <= 'z')
		{
			printf("%c",argv[i][0]-32);
		}
		else {
			printf("%c",argv[i][0]);
		}
	}
}
