#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
typedef struct
{
	string name;
	int votes;
} candidate;

candidate get_candidate(void);
int main(void)
{
	candidate new_candidate = get_candidate();
	printf("name");
	string title;
	for (int i = 0,len = strlen(new_candidate.name); i < len; i++)
	{
		if ( i  == 0 )
		title += toupper(new_candidate.name[i]);
		else {

			title += new_candidate[i];
		}
	}
	printf("%s\n",title);
	printf("\n");
	printf("candidate is named %s and has %i votes\n",new_candidate.name,new_candidate.votes);
}
 
candidate get_candidate(void)
{
	candidate new_candidate;
	new_candidate.name = get_string("Name: ");
	new_candidate.votes = get_int("votes: ");
	return new_candidate;
	
}  
