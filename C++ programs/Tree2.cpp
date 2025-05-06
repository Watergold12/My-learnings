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
}

int main()
{
    int treeHeight;
    cout << "Enter the height of the tree: ";
    cin >> treeHeight;

    drawTree(treeHeight);

    return 0;
}
