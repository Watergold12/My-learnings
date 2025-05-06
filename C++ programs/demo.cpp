#include <iostream>
#include <iomanip>

using namespace std;

class myClass
{
private:
    int sal;

public:
    void getdata();
    void display();
};

void myClass::getdata()
{
    cout << "Enter value of your salary: ";
    cin >> sal;
}

void myClass::display()
{
    cout << "Your salary is: " << sal << endl;
}

int main()
{
    myClass obj;
    obj.getdata();
    obj.display();
    return 0;
}
