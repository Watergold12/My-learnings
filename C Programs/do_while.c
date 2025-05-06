#include <stdio.h>  //header file

int main() // main function
{
    int i, a; // variable
    printf("Enter a number: ");
    scanf("%d", &i); // Value taken
    a = i + i;
    do
    {
        printf("I am Vishal ");
        i++;
    }while (i <= 10);
}