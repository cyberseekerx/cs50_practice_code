#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text,int len);
int count_word(string text,int len);
int count_sen(string text, int len);
int assign_grade(int round_index);
int main(void)
{
	// take user input
	string text = get_string("Text: ");
	int len = strlen(text);
	int letter = count_letters(text, len);
	int word = count_word(text, len);
	int sen = count_sen(text,len);
	//cal index to rouna 
	float L = (float) letter / word * 100;
	float S = (float) sen / word * 100;
	float index = 0.0588 * L - 0.296 * S - 15.8;
	int round_index = round(index);
	assign_grade(round_index);
}
int count_letters(string text, int len )
{
	int count = 0;
	for (int i = 0; i < len; i++)
	{
		if(isalpha(text[i]))
		{
			count++;
		}
	}	
	return count;
}

int count_word(string text, int len)
{
	int count = 1;
	for (int i = 0; i < len; i++)
	{
		if (isblank(text[i]))
		{
			count++;
		}
	}
	return count;
}
int count_sen(string text, int len)
{
	int count = 0;
	for (int i = 0; i < len; i++)
	{
		if (text[i] =='.' || text[i] == '?' || text[i] == '!')
		{
			count ++;
		}
	}
	return count;
}

int assign_grade(int round_index)
{
	if (round_index < 1)
	{
		printf("Before Grade 1\n");
	}
	else if (round_index <= 16)
	{
		printf("Grade %i\n",round_index);
	}
	else
      {
      		printf("Grade 16+\n");
      }
	return 0;
}



