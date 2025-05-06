# Problem: Average Expenses for Each Semester
# John has a list of his monthly expenses from last year:
# monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]

monthly_spendings = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]

def monthly_average():
    first_semester_total = 0
    second_semester_total = 0

    for spn in monthly_spendings:
        if spn <= 2500:
            first_semester_total += spn
        else:
            second_semester_total += spn


    first_semester_avg = first_semester_total / 6
    second_semester_avg = second_semester_total / 6

    print(f"The first semester expense average of John is: {first_semester_avg}.")
    print(f"The second semester expense average of John is: {second_semester_avg}.")

monthly_average()