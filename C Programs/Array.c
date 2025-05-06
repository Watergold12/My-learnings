// 1d & 2d array
#include <stdio.h>
#include <stdlib.h>

int main()
{
    // int arr[5] = {56, 49, 55, 85, 67};
    int drr[2][3] = {
        {56, 26, 36},  
        {52, 22, 32}
    };
    // printf( "%d " , arr[0]);
    // printf( "%d " , arr[3]);
    printf( "%d " , drr[0][2]);
    printf( "%d " , drr[1][1]);
    return 0;
}
