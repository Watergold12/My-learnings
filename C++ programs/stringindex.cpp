#include <iostream>
#include <string>

int main()
{
    std::string str;
    std::cout << "Enter a string: ";
    std::cin >> str;

    int index;
    std::cout << "Enter the index (0 to " << str.length() - 1 << "): ";
    std::cin >> index;

    if (index >= 0 && index < str.length())
    {
        std::cout << "Character at index " << index << ": " << str[index] << std::endl;
    }
    else
    {
        std::cout << "Invalid index." << std::endl;
    }

    return 0;
}
