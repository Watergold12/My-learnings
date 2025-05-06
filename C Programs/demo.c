#include <stdio.h>

int main()
{
    FILE *filePointer = fopen("demo.txt", "w");

    if (filePointer == NULL)
    {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(filePointer, "Hello, My name is Vishal");
    fclose(filePointer);

    filePointer = fopen("demo.txt", "r"); // Reuse the existing filePointer variable

    if (filePointer == NULL)
    {
        printf("Error opening file!\n");
        return 1;
    }

    char buffer[100];
    while (fscanf(filePointer, "%s", buffer) != EOF) // Check for end of file
    {
        printf("%s ", buffer); // Add a space between words
    }

    fclose(filePointer);

    return 0;
}