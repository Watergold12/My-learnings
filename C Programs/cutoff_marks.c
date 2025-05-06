#include <stdio.h>

int main()
{
    int physics, chemistry, biology, math, total, student_type;
    float medical_cutoff, engineering_cutoff;

    // Input marks
    printf("Enter marks for Physics: ");
    scanf("%d", &physics);
    printf("Enter marks for Chemistry: ");
    scanf("%d", &chemistry);
    printf("Enter marks for Biology: ");
    scanf("%d", &biology);
    printf("Enter marks for Mathematics: ");
    scanf("%d", &math);

    // Calculate total marks
    total = physics + chemistry + biology + math;

    printf("Enter student type(1 for Medical or 2 for Engineering): ");
    scanf("%d", &student_type);
    // Calculate cutoffs
    medical_cutoff = (physics + chemistry) / 2.0 + biology;
    engineering_cutoff = (physics + chemistry) / 2.0 + math;

    // Output results
    printf("Total Marks: %d\n", total);
    if (student_type == 1)
    {
        printf("Medical Cutoff: %.2f\n", medical_cutoff);
    }
    else
    {
        printf("Engineering Cutoff: %.2f\n", engineering_cutoff);
    }

    return 0;
}
