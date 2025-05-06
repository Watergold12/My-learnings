#include <stdlib.h>
#include <iostream>
#include <iomanip>
#include <conio.h>

using namespace std;

class insertion
{
private:
    int n, m[10], ele, p;

public:
    void getdata();
    void insert();
    void display();
};

void insertion ::getdata()
{
    cout << "How many elements? ";
    cin >> n;
    cout << "Enter " << n << " number of elements: ";
    for (int i = 0; i < n; i++)
        cin >> m[i];
    cout << "Enter the element to be inserted: ";
    cin >> ele;
    cout << "Enter the position (0 to " << n - 1 << "): ";
    cin >> p;
}

void insertion ::insert()
{
    if (p > n)
    {
        cout << p << "is an invalid position.";
        exit(0);
    }

    for (int i = n - 1; i >= p; i--)
    {
        m[i + 1] = m[i];
        m[p] = ele;
        n++;
    }
    cout << ele << " is successfully inserted." << endl;
}

void insertion ::display()
{
    cout << "The array after the insertion is ";
    for (int i = 0; i < n; i++)
    {
        cout << setw(4) << m[i];
    }
}

int main()
{
    insertion I;
    I.getdata();
    I.insert();
    I.display();
    return 0;
}