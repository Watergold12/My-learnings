#include <iostream>

using namespace std;

class Solution
{
public:
    int climbStairs(int n)
    {
        int dp[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; i++)
        {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
};

int main()
{
    int n;
    cout << "Enter the number of steps: ";
    cin >> n;
    Solution obj;
    cout << "There are " << obj.climbStairs(n) << " ways to climb to the top." << endl;
    return 0;
}