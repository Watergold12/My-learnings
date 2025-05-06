#include <iostream>
using namespace std;

int climbStairs(int n)
{
    if (n == 0 || n == 1)
    {
        return 1; // Base cases
    }
    int first = 1;
    int second = 2;
    for (int i = 3; i <= n; ++i)
    {
        int third = first + second;
        first = second;
        second = third;
    }
    return second;
}

int main()
{
    int n;
    cout << "Enter the number of steps: ";
    cin >> n;
    cout << "Distinct ways to climb " << n << " steps: " << climbStairs(n) << endl;
    return 0;
}
