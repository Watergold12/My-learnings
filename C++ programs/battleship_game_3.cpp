#include <iostream>
#include <vector>
#include <ctime>
using namespace std;

const int BOARD_SIZE = 20;
const char EMPTY_CELL = '.';
const char HIT_CELL = 'X';

struct Ship
{
    char symbol;
    int size;
    int hitpoints;
};

// Initialize the game board
vector<vector<char>> board(BOARD_SIZE, vector<char>(BOARD_SIZE, EMPTY_CELL));

// Place a ship on the board
void placeShip(vector<vector<char>> &board, int row, int col, const Ship &ship, bool vertical)
{
    for (int i = 0; i < ship.size; ++i)
    {
        if (vertical)
        {
            board[row + i][col] = ship.symbol;
        }
        else
        {
            board[row][col + i] = ship.symbol;
        }
    }
}

// Display the game board
void displayBoard(const vector<vector<char>> &board)
{
    cout << "  ";
    for (int col = 0; col < BOARD_SIZE; ++col)
    {
        cout << col << " ";
    }
    cout << "\n";
    for (int row = 0; row < BOARD_SIZE; ++row)
    {
        cout << row << " ";
        for (int col = 0; col < BOARD_SIZE; ++col)
        {
            cout << board[row][col] << " ";
        }
        cout << "\n";
    }
}

// Initialize ships
vector<Ship> ships = {
    {'S', 2, 2}, // Small ship
    {'M', 3, 3}, // Medium ship
    {'L', 4, 4}  // Large ship
};

// Randomly place ships on the board
void placeRandomShips(vector<vector<char>> &board)
{
    srand(time(nullptr));
    for (const Ship &ship : ships)
    {
        bool vertical = rand() % 2 == 0;
        int row = rand() % (BOARD_SIZE - ship.size + 1);
        int col = rand() % (BOARD_SIZE - ship.size + 1);
        placeShip(board, row, col, ship, vertical);
    }
}

int main()
{
    placeRandomShips(board);

    cout << "Welcome to Battleship!\n";
    displayBoard(board);

    // Your game logic (player turns, AI turns, etc.) goes here

    return 0;
}
