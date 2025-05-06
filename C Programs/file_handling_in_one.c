#include <stdio.h>

int main()
{
    // Open the file in write mode
    FILE *filePointer = fopen("example.txt", "w");

    if (filePointer == NULL)
    {
        printf("Error opening file!\n");
        return 1;
    }

    // Write data to the file
    fprintf(filePointer, "Hello, World!\n");
    fclose(filePointer); // Close the file after writing

    // Open the file in read mode
    filePointer = fopen("example.txt", "r");

    if (filePointer == NULL)
    {
        printf("Error opening file!\n");
        return 1;
    }

    // Read data from the file
    char buffer[100];
    while (fscanf(filePointer, "%s", buffer) != EOF)
    {
        printf("%s", buffer);
    }

    fclose(filePointer); // Close the file after reading

    return 0;
}
