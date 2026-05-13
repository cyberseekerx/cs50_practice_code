#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
	string text = get_string("Input: ");
	for (int  = 0, len = strlen(text) ; i < len - 1; i++)
	{
		if (text[i] > text[i + 1])
		{
			printf("no\n");
			return 0;
		}
	}
	printf("Yes\n");
	return 1;

	
}
