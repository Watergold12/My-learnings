#include <iostream>

using namespace std;

// Function to draw a tree with a given height
void drawTree(int height)
{
    for (int i = 1; i <= height; ++i)
    {
        // Print spaces
        for (int j = 1; j <= height - i; ++j)
        {
            cout << " ";
        }
        // Print stars
        for (int j = 1; j <= 2 * i - 1; ++j)
        {
            cout << "*";
        }
        cout << endl;
    }

    // Draw the trunk
    for (int i = 1; i <= height / 3; ++i)
    {
        for (int j = 1; j <= height - 1; ++j)
        {
            cout << " ";
        }
        if (height > 9)
        {
            cout << "***" << endl; // Draw 3 asterisks if height > 9
        }
        else if (height > 5)
        {
            cout << "**" << endl; // Draw 2 asterisks if height > 5
        }
        else
        {
            cout << "*" << endl; // Draw 1 asterisk if height <= 5
        }
    }
}

int main()
{
    int treeHeight;
    cout << "Enter the height of the tree: ";
    cin >> treeHeight;

    drawTree(treeHeight);

    return 0;
}
