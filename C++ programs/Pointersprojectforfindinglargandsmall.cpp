#include <stdio.h>

void findMinMax(int *arr, int size, int *min, int *max)
{
    if (size <= 0)
    {
        printf("Array is empty.\n");
        return;
    }

    *min = *max = *arr; // Initialize min and max with the first element of the array

    for (int i = 1; i < size; i++)
    {
        if (*(arr + i) < *min)
        {
            *min = *(arr + i); // Update min if a smaller element is found
        }
        else if (*(arr + i) > *max)
        {
            *max = *(arr + i); // Update max if a larger element is found
        }
    }
}

int main()
{
    int arr[] = {10, 5, 8, 20, 15};
    int size = sizeof(arr) / sizeof(arr[0]);
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
