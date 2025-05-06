#include <stdio.h> //header file

int main() // main function
{
    int num1; // variable
    printf("Enter a number: ");
    scanf("%d", &num1); // value taken
    if (num1 == 4)      // if statement
    {
        if (num1%2 == 0)
        {
            printf("It is even number.");
        }else{
            printf("It is odd number.");
        }   
    }
    else
    {
        printf("You didn't guess it try again!!"); // second argument
    }
}
