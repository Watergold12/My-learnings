#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int myAge, reqAge;
    const int voteAge = 18;
    cout << "Program to find your eligibility for voting: " << endl;
    cout << "Enter your current age: ";
    cin >> myAge;

    // code for voting age detection
    if (myAge >= voteAge)
    {
        cout << "Old enough to vote buddy!";
    }
    else
    {
        reqAge = voteAge - myAge;
        cout << "Nah buddy!! You have " << reqAge << " more year(s) to go.";
    };
}