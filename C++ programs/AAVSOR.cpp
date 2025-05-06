#include <iostream>
#include <conio.h>
#include <iomanip>

using namespace std;

class sorting
{
private:
    int m[100], n, j;

public:
    void getdata();
    void sort();
    void display();
};

void sorting ::getdata()
{
    cout << "How many elements? ";
    cin >> n;
    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++)
    {
        cin >> m[i];
    }
}

void sorting ::display()
{
    cout << "The array after sorting is ";
    for (int i = 0; i < n; i++)
    {
        cout << setw(2) << m[i];
    }
}

void sorting ::sort()
{
    int temp;
    for (int i = 1; i < n; i++)
    {
        j = i;
        while (j >= 1)
        {
            if (m[j] < m[j - 1])
            {
                temp = m[i];
                m[j] = m[j - 1];
                m[j - 1] = temp;
            }
            j--;
        }
    }
}

int main()
{
    sorting S;
    S.getdata();
    S.sort();
    S.display();
    return 0;
}