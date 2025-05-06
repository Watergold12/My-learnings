#include <stdio.h>

int main()
{
    FILE *filePointer = fopen("demo.txt", "r");

    if (filePointer == NULL)
    {
        printf("Unable to open file.\n");
        return 1;
    }

    int buffer[100];
    while (fscanf(filePointer, "%d", buffer) != EOF)
    {
        printf("%n", buffer);
    }

    fclose(filePointer);

    return 0;
}