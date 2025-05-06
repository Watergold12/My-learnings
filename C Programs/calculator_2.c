#include <stdio.h>

int main()
{
    int choice;
    float num1, num2, result;

    while (1)
    {
        // Display menu
        printf("\nSimple Calculator\n");
        printf("1. Addition\n");
        printf("2. Subtraction\n");
        printf("3. Multiplication\n");
        printf("4. Division\n");
        printf("5. Square\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1: // Addition
            printf("Enter two numbers: ");
            scanf("%f %f", &num1, &num2);
            result = num1 + num2;
            printf("Result: %.2f\n", result);
            break;

        case 2: // Subtraction
            printf("Enter two numbers: ");
            scanf("%f %f", &num1, &num2);
            result = num1 - num2;
            printf("Result: %.2f\n", result);
            break;

        case 3: // Multiplication
            printf("Enter two numbers: ");
            scanf("%f %f", &num1, &num2);
            result = num1 * num2;
            printf("Result: %.2f\n", result);
            break;

        case 4: // Division
            printf("Enter two numbers: ");
            scanf("%f %f", &num1, &num2);
            if (num2 != 0)
            {
                result = num1 / num2;
                printf("Result: %.2f\n", result);
            }
            else
            {
                printf("Error: Division by zero!\n");
            }
            break;

        case 5: // Square
            printf("Enter a number: ");
            scanf("%f", &num1);
            result = num1 * num1;
            printf("Square of %.2f is %.2f\n", num1, result);
            break;

        case 6: // Exit
            printf("Exiting...\n");
            return 0;

        default:
            printf("Invalid choice, try again.\n");
        }
    }

    return 0;
}