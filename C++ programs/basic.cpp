#include <iostream>

using namespace std;

class myClass
{
private:
    int a;
    int number[];

public:
    void function();
    void display();
};

void myClass::function()
{
    int a;
    cout << "Enter the number of elements: ";
    cin >> a;
    int number[a];

    cout << "Enter " << a << " numbers: ";
    for (int i = 0; i < a; i++)
    {
        cin >> number[i];
    }
}

void myClass::display()
{
    cout << "The numbers are: ";
    for (int i = 0; i < a; i++)
    {
        cout << number[i];
    }
    cout << endl;
}

int main()
{
    myClass obj;
    obj.function();
    obj.display();
    return 0;
}