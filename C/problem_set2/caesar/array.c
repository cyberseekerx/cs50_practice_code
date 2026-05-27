#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
	char ascii_upper[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	char letters[] = "BARFOO";
	//int key = get_int("key: value")
	int key = 23;
	for (int i = 0 ,len = strlen(letters); i < len; i++)
	{
		int encrypt = ((letters[i] - 65) + key) % 26;
		//printf("%i ",encrypt);
		printf("letters:%c; %c\n",letters[i],ascii_upper[encrypt]);
	}
	
}
