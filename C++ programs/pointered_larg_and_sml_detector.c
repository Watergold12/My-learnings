#include <stdio.h>

void findMinMax(int *arr, int size, int *min, int *max)
{
    if (size <= 0)
    {
        printf("Array is empty. \n");
        return 0;
    }

    *min = *max = *arr;

    for (int i = 1; i < size; i++)
    {
        if (*(arr + i) < *min)
        {
            *min = *(arr + i);
        }
        else if (*(arr + i) > *max)
        {
            *max = *(arr + i);
        }
    }
}

int main()
{
    int size;
    printf("Enter the size of the array: \n");
    scanf("%d", &size);

    if (size <= 0)
    {
        printf("Invalid size of an array. \n");
        return 1;
    }

    int arr[size];
    printf("Enter %d elements of the array: \n");
    for (int i = 0; i < size; i++)
    {
        scanf("%d", &arr[i]);
    }
    int min, max;
    findMinMax(arr, size, &min, &max);

    printf("Array elements: ");
    for (int i = 0; i < size; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");

    printf("Smallest element: %d\n", min);
    printf("Largest element: %d\n", max);

    return 0;
}