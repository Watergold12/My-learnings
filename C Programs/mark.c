#include <stdio.h>
#include <stdlib.h>

int main()
{
    float phys, math, chem, cs, eng;
    float average, total, percent;

    printf("Enter Physics, Chemistry, Maths, CS and English marks: ");
    scanf("%f %f %f %f %f", &phys, & math, &chem, &cs, &eng);

    total = phys + math + chem + cs + eng;
    average = total/5;
    percent = (total/500) * 100;

    printf("Total: %.2f \n", total);
    printf("Average: %.2f \n", average);
    printf("Percent: %.2f \n", percent);

    return 0;
}