#include <stdio.h>  //header file
#include <stdlib.h> //header file

int main() // main function
{
    int i; // variable
    printf("Enter a number: ");
    scanf("%d", &i); // Value taken
    while (i <= 10)
    {
        printf("%d ", i);
        i++;
    }
}