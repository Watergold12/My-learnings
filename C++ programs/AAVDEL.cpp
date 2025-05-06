#include <iostream>
#include <iomanip>
#include <conio.h>

using namespace std;

class deletion
{
private:
    int m[10], n, ele, p;

public:
    void getdata();
    void remove();
    void display();
};

void deletion::getdata()
{
    cout << "How many elements? ";
    cin >> n;
    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++)
        cin >> m[i];
    cout << "Enter the position (0 to " << n - 1 << "): ";
    cin >> p;
}

void deletion::remove()
{
    if (p > n - 1)
    {
        cout << p << " is an invalid position.";
        exit(0);
    }

    ele = m[p];
    for (int i = p + 1; i < n; i++)
    {
        m[n - 1] = m[i];
        n--;
    }

    cout << ele << " is successfully removed.";
}

void deletion ::display()
{
    cout << "The array after deletion is ";
    for (int i = 0; i < n; i++)
    {
        cout << setw(2) << m[i];
    }
}

int main()
{
    deletion D;
    D.getdata();
    D.remove();
    D.display();
    return 0;
}