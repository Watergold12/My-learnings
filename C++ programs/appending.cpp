#include <iostream>
using namespace std;

class append
{
private:
    string firstName, lastName, fullName;

public:
    void getdata();
    void putdata();
};

void append ::getdata()
{
    cout << "Program for checking append command:" << endl;
    cout << "Enter the First Name: ";
    cin >> firstName;
    cout << "Enter the Last Name: ";
    cin >> lastName;
}

void append ::putdata()
{
    fullName = firstName.append(lastName);
    cout << "Fullname: " << fullName;
}

int main()
{
    append A;
    A.getdata();
    A.putdata();
}