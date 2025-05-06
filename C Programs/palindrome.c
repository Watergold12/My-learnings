#include <stdio.h>

int isPalindrome(int n)
{
    int org = n, rev, rem;

    while (n != 0)
    {
        rem = n % 10;
        rev = rev * 10 + rem;
        n /= 10;
    }

    return org == rev;
}

int main()
{
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);

    if (isPalindrome(number))
    {
        printf("%d is a palindrome number.", number);
    }
    else
    {
        printf("%d is not a palindrome number.", number);
    }
    return 0;
}