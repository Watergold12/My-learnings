#include <stdio.h>

int main()
{
    int pin = 1234, enteredPin, choice;
    float balance = 1000.0, amount;

    printf("Enter your PIN: ");
    scanf("%d", &enteredPin);
    if (enteredPin != pin)
    {
        printf("Incorrect PIN.\n");
        return 1;
    }

    do
    {
        printf("\nATM Menu:\n");
        printf("1. Deposit\n");
        printf("2. Withdraw\n");
        printf("3. Check Balance\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            printf("Enter amount to deposit: ");
            scanf("%f", &amount);
            balance += amount;
            printf("Deposited: %.2f\n", amount);
            break;
        case 2:
            printf("Enter amount to withdraw: ");
            scanf("%f", &amount);
            if (amount <= balance)
            {
                balance -= amount;
                printf("Withdrawn: %.2f\n", amount);
            }
            else
            {
                printf("Insufficient balance.\n");
            }
            break;
        case 3:
            printf("Current balance: %.2f\n", balance);
            break;
        case 4:
            printf("Exiting...\n");
            break;
        default:
            printf("Invalid choice. Try again.\n");
        }
    } while (choice != 4);

    return 0;
}