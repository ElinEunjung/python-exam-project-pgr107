options = [         # creates a list with pre-defined options
    "1. Open a new account",
    "2. Deposit money into your account",
    "3. Withdraw money from your account",
    "4. Add interests to your account",
    "5. Get the current balance of your account",
    "6. Quit"
]

class Menu:
    """Class for controlling the program flow"""
    def __init__(self):
        self.options = options

    def add_option(self):
        self.print_menu()
        option = input("\nWrite an option you would like to add: ")
        option = str(len(self.options)+1) + ". "  + option
        self.options.append(option)
        print(f"New option {option} added successfully, updated menu:\n ")
        self.print_menu()

    def get_input(self):
        self.print_menu()
        user_input = input("Enter your choice with number: ")
        if user_input in {"1", "2", "3", "4", "5", "6"}:
            return int(user_input)
        else:
            print("Invalid input. Please enter number next time.")
            return None

    def print_menu(self):
        for option in self.options:
            print(option)

class BankAccount:
    """Entity responsible for managing bank accounts"""
    def __init__(self, balance = 0.0, interest = 0.0):
        self.balance = balance
        self.interest = interest

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("\033[91mPlease enter a positive number.\033[0m")
            else:
                self.balance += amount
                print(f"Your balance was updated, now: {self.balance}")
        except ValueError:
            print("\033[91mPlease enter a number next time.\033[0m")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("\033[91mPlease enter a positive number.\033[0m")
            else:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Your balance was updated, now: {self.balance}")
                else:
                    print("\033[91mNot enough funds in account to withdraw "
                          "that amount.\033[0m")
        except ValueError:
            print("\033[91mPlease enter a number next time.\033[0m")

    def add_interests(self):
        try:
            interest = float(input("Add interest rate, "
                                   "use numbers like 2.50: "))
            if interest > 0:
                self.interest = interest
                print(f"Interest was added, after 1 year you may earn: "
                      f"{self.interest / 100 * self.balance}")
            else:
                print("\033[91mPlease enter a positive "
                      "interest rate next time.\033[0m")
        except ValueError:
            print("\033[91mPlease enter a number next time.\033[0m")

    def get_balance(self):
        return self.balance

    def __str__(self):
        interest = f" | Interest rate: {self.interest}%"\
            if self.interest > 0 else ""
        return f"Account balance: {self.balance}{interest}"


if __name__ == "__main__":
    """Only runs if this script is the main file, was added 
       to harmonize code with our common standards"""

    bank_account_1 = BankAccount()
    menu = Menu()
    user_choice = menu.get_input()

    while user_choice != 6:
        if user_choice is None:
            print("\033[91mPlease enter a valid option.\033[0m")
        elif user_choice == 1:
            print("Opened a new account")
        elif user_choice == 2:
            bank_account_1.deposit()
        elif user_choice == 3:
            bank_account_1.withdraw()
        elif user_choice == 4:
            bank_account_1.add_interests()
        elif user_choice == 5:
            print(bank_account_1.get_balance())
        print()
        user_choice = menu.get_input()
    print("Exiting program")

    # Here I am calling method add_option() to check its functionality
    menu.add_option()





