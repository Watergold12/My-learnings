// Program for information regarding the exercises to be performed for bulking
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

class bulking
{
private:
    int choice;
    string myChoice;

public:
    void getdata();
    void display();
};

void bulking ::getdata()
{
    cout << "Program for bulking your body: \n";
    cout << "Enter the body part you want to bulk: (Body, legs or arms) ";
    cin >> myChoice;
}

void bulking ::display()
{
    if (myChoice == "Body")
    {
        cout << "Choose the option from the below given choices (1 or 2): \n1. Chest, \n2. Abdomen. \nYour choice:";
        cin >> choice;
        switch (choice)
        {
        case 1:
            cout << "You will have to practice 2 sets of Benchpress, Push-ups, Inclinde dumbbell press,\nDumbbell Flyss, Dumble benchpress, and Cable crossover. \nGood luck champ!!";
            break;

        case 2:
            cout << "You will have to practice 2 sets of Crunch, Bicycle crunch, Russian twist, Reverse Crunch,\nPlank, and V-ups.\nGood luck Champ!!";
            break;

        default:
            cout << "Invalid index entry!!";
            break;
        }
    }
    else
    {
        if (myChoice == "legs")
        {
            cout << "Choose the option from the below given choices (1 or 2): \n1. Calf muscle, \n2. Thighs. \nYour choice:";
            cin >> choice;
            switch (choice)
            {
            case 1:
                cout << "You will have to practice 2 sets of Calf raises, Standing calf Stretch, Single leg Calf raise, and Ankle stretch.\nGood luck Champ!!";
                break;

            case 2:
                cout << "You will have to practice 2 sets of Squat, Split squats, Sumo squat, lunge,\nQuad stretch, and Leg circles.\nGood Luck Champ!!";
                break;

            default:
                cout << "Invalid index entry!!";
                break;
            }
        }

        else
        {
            if (myChoice == "arms")
            {
                cout << "Choose the option from the below given choices (1 or 2): \n1. Triceps, \n2. Biceps, \n3. Forearm. \nYour choice:";
                cin >> choice;
                switch (choice)
                {
                case 1:
                    cout << "You will have to practice 2 sets of Push down, tricep dips, Diamond Push up, Push up,\nTricep dumble Kickback, and Bench Dip(Weighted).\nGood Luck Champ!!";
                    break;

                case 2:
                    cout << "You will have to practice 2 sets of Bicep curl, Hammer curl, Pull-up, Barbell curl,\nCheat curls, and Concentration curls.\nGood luck Champ!!";
                    break;

                case 3:
                    cout << "You will have to practice 2 sets of Reverse Barbell curl, Zottman curl, Reverse wrist curl, Farmer's Walk,\n Wrist curl, and Wrist exercises.\nGood luck Champ!!";
                    break;

                default:
                    cout << "Invalid index entry!!";
                    break;
                }
            }
            else
            {
                cout << "Invalid body-part entry!!WARNING!!";
            }
        }
    }
}

int main()
{
    bulking B;
    B.getdata();
    B.display();
    return 0;
}