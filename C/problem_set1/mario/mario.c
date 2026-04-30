#include <cs50.h>
#include <stdio.h>

int two_spaces(int spaces);
int printf_spaces(int height, int row);
int printf_row(int bricks);

#define BLANK 2
int main(void)
{   
    int height;
    do
    {  
        height = get_int("Height: ");
       
    }
    while (height <= 0 | height > 60);
  
    
    
    for (int row = 0; row < height; row++)
    {
        printf_spaces(height,row);
        printf_row(row);
       two_spaces(BLANK);
        printf_row(row);
        printf("\n");


    }
}
int printf_row(int bricks)
{
    for (int i = 0; i <= bricks; i++)
    {
        printf("#");
    }


}
int printf_spaces(int height, int row)
{
    int c_row = row + 1;
    int spaces = height - c_row;
    for (spaces <= height; spaces --;) 
    printf(" ");

}
int two_spaces(int i)
{
    for (int b = 0;b < i; b++)
        printf(" ");

}
