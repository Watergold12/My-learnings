class Airplane:
    def __init__(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seating = [['O' for _ in range(seats_per_row)] for _ in range(rows)]
        
    def display_seating(self):
        print("Current seating arrangement:")
        for row in range(self.rows):
            print(f"Row {row + 1}: {' '.join(self.seating[row])}")
        print()

    def reserve_seat(self, row, seat):
        if self.is_seat_valid(row, seat):
            if self.seating[row - 1][seat - 1] == 'O':
                self.seating[row - 1][seat - 1] = 'X'
                print(f"Seat {row}-{seat} reserved successfully.\n")
            else:
                print(f"Seat {row}-{seat} is already taken.\n")
        else:
            print("Invalid seat number. Please try again.\n")

    def cancel_reservation(self, row, seat):
        if self.is_seat_valid(row, seat):
            if self.seating[row - 1][seat - 1] == 'X':
                self.seating[row - 1][seat - 1] = 'O'
                print(f"Reservation for seat {row}-{seat} canceled successfully.\n")
            else:
                print(f"Seat {row}-{seat} is not reserved.\n")
        else:
            print("Invalid seat number. Please try again.\n")
        
    def is_seat_valid(self, row, seat):
        return 1 <= row <= self.rows and 1 <= seat <= self.seats_per_row


def main():
    airplane = Airplane(10, 4)  # Example: 10 rows, 4 seats per row
    
    while True:
        print("*" * 35)
        print("Airplane Reservation System".center(35))
        print("*" * 35)
        print("1. Display seating")
        print("2. Reserve a seat")
        print("3. Cancel reservation")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            airplane.display_seating()
        elif choice == '2':
            row = int(input("Enter row number: "))
            seat = int(input("Enter seat number: "))
            airplane.reserve_seat(row, seat)
        elif choice == '3':
            row = int(input("Enter row number: "))
            seat = int(input("Enter seat number: "))
            airplane.cancel_reservation(row, seat)
        elif choice == '4':
            print("Exiting the system. See you soon!!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
