#include <iostream>
using namespace std;

class myClass
{
private:
    int a;
    int *number; // Pointer to dynamically allocated array

public:
    void function();
    void display();
    myClass();  // Constructor to initialize the pointer
    ~myClass(); // Destructor to release memory
};

myClass::myClass()
{
    a = 0;
    number = nullptr; // Initialize the pointer to nullptr
}

myClass::~myClass()
{
    delete[] number; // Release memory when the object is destroyed
}

void myClass::function()
{
    cout << "Enter the number of elements: ";
    cin >> a; // Read the number of elements

    // Allocate memory for the array
    number = new int[a];

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
        cout << number[i] << " ";
    }
    cout << endl; // Add a newline for better formatting
}

int main()
{
    myClass obj;
    obj.function(); // Call the function to input numbers
    obj.display();  // Call the function to display numbers
    return 0;
}
