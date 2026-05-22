#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
	int letter = 0;
	int word = 0;
	int sen = 0;
	printf("hi mom\n");
	// take user input
	string text = get_string("Text: ");
	for (int i = 0, len = strlen(text); i < len; i++) {
		if (isblank(text[i])) {
			word++;
		}
		if (isalpha(text[i])) {
			letter++;
		}
		if (text[i] == '.' || text[i] == '?' || text[i] == '!') {
			sen++;
		}
	}
	printf("letter:%i\nword:%i\nsentence:%i", letter, word, sen);
}
