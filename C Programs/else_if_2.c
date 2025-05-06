#include <stdio.h> //header file

int main() // main function
{
    int num1; // variable
    printf("Enter a number: ");
    scanf("%d", &num1); // value taken
    if (num1 == 3)      // if statement
    {
        printf("You guessed it correct!!");
    }
    else
    {
        printf("You've guessed it wrong!! But ");
        if (num1 % 2 == 0)
        {
            printf("It is even number.");
        }
        else
        {
            printf("It is odd number.");
        }
    }
}