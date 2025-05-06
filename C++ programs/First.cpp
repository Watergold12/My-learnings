#include <iostream>
#include <iomanip>
using namespace std;

class Calculate
{
private:
    int x, y, area;

public:
    void getdata();
    void calc();
};

void Calculate ::getdata()
{
    cout << "Calculating the area of the rectangle:" << endl;
    cout << "Enter the length: ";
    cin >> x;
    cout << "Enter the width: ";
    cin >> y;
}

void Calculate ::calc()
{
    area = x * y;
    cout << "Area of rectangle with length = " << x << " and width = " << y << " is = " << area;
}

int main()
{
    Calculate c;
    c.getdata();
    c.calc();
    return 0;
}