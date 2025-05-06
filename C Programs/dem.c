#include <stdio.h>

int main()
{
    FILE *filePointer = fopen("demo.txt", "r"); // Open the file in read mode

    if (filePointer == NULL)
    {
        printf("Unable to open file.\n");
        return 1;
    }

    int buffer;
    while (fscanf(filePointer, "%d", &buffer) != EOF) // Check for end of file and read into an integer variable
    {
        printf("%d ", buffer); // Print the value with a space
    }

    fclose(filePointer);

    return 0;
}
