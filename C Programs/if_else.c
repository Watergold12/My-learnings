#include <stdio.h> //header file

int main() // main function
{
    int num1; // variable
    printf("Enter a number: ");
    scanf("%d", &num1); // value taken
    if (num1 == 3)      // if statement
    {
        printf("You guessed it correct!!"); // Argument
    }
    else
    {
        printf("You didn't guess it try again!!"); // second argument
    }
}

// if(condition){
//     argument no. 1
// } else {
//      argument no. 2
// }