#include <iostream>
#include <ctime>
using namespace std;

// Function to display the game board
void displayBoard(const bool ships[4][4])
{
    cout << "  0 1 2 3\n";
    for (int row = 0; row < 4; ++row)
    {
        cout << row << " ";
        for (int col = 0; col < 4; ++col)
        {
            if (ships[row][col])
                cout << "S "; // Ship
            else
                cout << ". "; // Empty
        }
        cout << "\n";
    }
}

// Function for ship placement by a player
void placeShips(bool ships[4][4])
{
    cout << "Enter ship coordinates (row and column) for each ship (total 4 ships):\n";
    for (int i = 0; i < 4; ++i)
    {
        int row, col;
        cout << "Ship " << (i + 1) << ": ";
        cin >> row >> col;
        ships[row][col] = true;
    }
}

int main()
{
    srand(time(nullptr));
    bool player1Ships[4][4] = {}; // Player 1's board
    bool player2Ships[4][4] = {}; // Player 2's board

    cout << "Player 1, place your ships:\n";
    placeShips(player1Ships);

    cout << "Player 2, place your ships:\n";
    placeShips(player2Ships);

    int currentPlayer = 1;
    int hits = 0;
    int numberOfTurns = 0;

    while (hits < 4)
    {
        cout << "Player " << currentPlayer << ", it's your turn!\n";
        displayBoard(currentPlayer == 1 ? player2Ships : player1Ships);

        int row, column;
        cout << "Choose a row number between 0 and 3: ";
        cin >> row;
        cout << "Choose a column number between 0 and 3: ";
        cin >> column;

        bool(&opponentShips)[4][4] = (currentPlayer == 1) ? player2Ships : player1Ships;

        if (row < 0 || row >= 4 || column < 0 || column >= 4)
        {
            cout << "Invalid coordinates. Try again.\n";
            continue;
        }

        if (opponentShips[row][column])
        {
            opponentShips[row][column] = false;
            hits++;
            cout << "Hit! " << (4 - hits) << " left.\n\n";
        }
        else
        {
            cout << "Miss\n\n";
        }

        numberOfTurns++;
        currentPlayer = 3 - currentPlayer; // Switch players (1 -> 2, 2 -> 1)
    }

    cout << "Player " << (3 - currentPlayer) << " wins!\n";
    cout << "Total turns played: " << numberOfTurns << "\n";

    return 0;
}
