#include <iostream>
#include <iomanip>
#include <conio.h>

using namespace std;

class frequency
{
private:
    int n, m[10], ele, i, freq;

public:
    void getdata();
    void findfreq();
    void display();
};

void frequency ::getdata()
{
    cout << "Enter the size of the array: ";
    cin >> n;
    cout << "Enter " << n << " elements into the array: ";
    for (int i = 0; i < n; i++)
        cin >> m[i];
    cout << "Enter the search element: ";
    cin >> ele;
}

void frequency ::findfreq()
{
    freq = 0;
    for (int i = 0; i < n; i++)
        if (ele == m[i])
            freq++;
}

void frequency ::display()
{
    if (freq > 0)
    {
        cout << "Frequency of " << ele << " is " << freq;
    }
    else
    {
        cout << ele << " does not exist.";
    }
}

int main()
{
    frequency F;
    F.getdata();
    F.findfreq();
    F.display();
    return 0;
}