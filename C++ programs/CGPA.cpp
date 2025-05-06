#include <iostream>
#include <vector>
using namespace std;

class CGPA
{
private:
    int a;
    vector<string> subjectGrades; // Store subject grades
    double totalGradePoints = 0;
    double CGPA = 0;

public:
    void datainput();
    void calculation();
    void show();
};

void CGPA::datainput() // Input class
{
    cout << "Enter the number of Subjects: ";
    cin >> a;

    for (int i = 0; i < a; i++)
    {
        string grade;
        cout << "Enter your subject Grade (A/B/C/D/E): ";
        cin >> grade;
        subjectGrades.push_back(grade); // Store subject grades
    }
}

void CGPA::calculation() // Calculation class
{
    for (const string &grade : subjectGrades)
    {
        switch (grade[0]) // Compare the first character of the grade
        {
        case 'A':
            totalGradePoints += 4.0;
            break;
        case 'B':
            totalGradePoints += 3.0;
            break;
        case 'C':
            totalGradePoints += 2.0;
            break;
        case 'D':
            totalGradePoints += 1.0;
            break;
        case 'E':
            totalGradePoints += 0.0;
            break;
        default:
            cout << "Invalid grade: " << grade << endl;
            break;
        }
    }

    CGPA = totalGradePoints / a;
}

void CGPA::show() // class display
{
    cout << "Total Grade Points = " << totalGradePoints << endl;
    cout << "CGPA = " << CGPA << endl;
}

int main()
{
    CGPA C;
    C.datainput();
    C.calculation();
    C.show();

    return 0;
}
