#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{

	int ASCII_ALPHA_UPPER[] = {65, 66, 67, 68, 69, 70, 71, 72, 73,
				   74, 75, 76, 77, 78, 79, 80, 81, 82,
				   83, 84, 85, 86, 87, 88, 89, 90};

	for (int i = 0,
		 len = sizeof(ASCII_ALPHA_UPPER) / sizeof(ASCII_ALPHA_UPPER[i]);
	     i < len; i++) {
		printf("%c ", ASCII_ALPHA_UPPER[i]);
		// printf("%c ", ASCII_ALPHA_UPPER[i] + 32);
	}
}
