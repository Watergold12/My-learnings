#include <stdio.h> //header file
#include <stdlib.h> //header file

int main() // main function
{
    int num1, i; // variable
    printf("Enter a number: ");
    scanf("%d", &num1); // Value taken
    for (i = 0; i < num1; i++) // for loop
    {
        printf("%d ", i);
    }
}
