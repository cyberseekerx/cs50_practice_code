#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("height: ");
    }
    while (height <= 0 | height > 8);
    // print collums 
    for (int row = 0; row < height; row++)
    {   
        int c_row = row + 1;
        int spaces = height - c_row;
        for (spaces < 0; spaces--;)
        {
            printf(" ");
        }
        for (int j = 0; j <= row; j++)

        {   
            printf("#");
        }
        printf("\n");
    }
}
