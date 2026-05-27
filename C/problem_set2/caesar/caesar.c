#include <cs50.h>
#include <stdbool.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



char ascii_lower[] = "abcdefghijklmnopqrstuvwxyz";
char ascii_upper[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
int main(int argc,string argv[])

{	
	if (argc != 2 )
	{
		printf("Usage: %s key\n",argv[0]);
		return 1;
	}
	for (int i = 0, len = strlen(argv[1]);i < len; i++)
	{
		if(isalpha(argv[1][i]))
		{
		printf("Usage: %s key\n",argv[0]);
		return 1;
		}
	}


	int j = atoi(argv[1]);
	int ci;
	string text = get_string("plaintext: ");
	printf("ciphertext: ");
	for (int i = 0, len = strlen(text); i < len; i++)
	{
		if (isalpha(text[i]) && isupper(text[i]))
		{
			 ci = ((text[i]-'A') + j) % 26;
			printf("%c",ascii_upper[ci]);
		}
      		else if (isalpha(text[i]) && islower(text[i]))
		{
			 ci = ((text[i]-'a') + j) % 26;
			printf("%c",ascii_lower[ci]);
		}
     		else
      		{
			printf("%c",text[i]);
		}
	}
	printf("\n");
	return 0;

}
