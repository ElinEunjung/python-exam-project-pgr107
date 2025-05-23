options = [         # creates a list with pre-defined options
    "1. Open a new account",
    "2. Deposit money into your account",
    "3. Withdraw money from your account",
    "4. Add interests to your account",
    "5. Get the current balance of your account",
    "6. Add new option",
    "7. Quit"
]
option_numbers = ["1", "2", "3", "4", "5", "6", "7"]


class Menu:
    """Class for controlling program flow"""
    def __init__(self):
        # I make a deep copy of global variables here
        self.options = options.copy()
        self.option_numbers = option_numbers.copy()

    def add_option(self):
        """function for adding an option to the menu
        Though app logic can't be implemented by just adding a text
        """
        option = input("\nWrite an option you would like to add: ")
        if not option.strip():
            # simple validation, do not allow empty input
            print("\nInvalid option. Please enter a valid option.")
            return None
        last_index = len(self.options) + 1

        # here I update list with numbers
        self.option_numbers.append(str(last_index))
        # and here list with full text gets updated
        option = str(last_index - 1) + ". "  + option
        self.options.insert(last_index - 2, option)
        self.options[-1] = f"{last_index}. Quit"
        print(f"New option {option} added successfully.")
        return last_index

    def get_input(self):
        """"function for getting user input"""
        self.print_menu()
        user_input = input("Enter your choice with number: ")
        if user_input in self.option_numbers:
            return int(user_input)
        else:
            # \033[91 makes print color red and \033[0m resets it back
            # Same for rest of code. Is used for wrong user inputs
            print("\033[91mInvalid input. Please enter number next time.\033[0m")
            return None

    def print_menu(self):
        for option in self.options:
            print(option)


class BankAccount:
    """Class responsible for managing bank accounts"""
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
                print(f"Interest was added, now {self}."
                      f"\nAfter 1 year you may earn: "
                      f"{(self.interest / 100 * self.balance):.2f}")
            else:
                print("\033[91mPlease enter a positive "
                      "interest rate next time.\033[0m")
        except ValueError:
            print("\033[91mPlease enter a number next time.\033[0m")

    def get_balance(self):
        return self.balance

    def __str__(self):
        interest = f" | Interest rate: {self.interest:.2f}%"\
            if self.interest > 0 else ""
        return f"account balance is: {self.balance:.2f}{interest}"


if __name__ == "__main__":
    """Only runs if this script is the main file, was added 
       to harmonize code with our common standards"""

    bank_account_1 = BankAccount()
    menu = Menu()
    user_choice = menu.get_input()
    exit_option = 7

    while user_choice != exit_option:
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
            print(f"Your current balance is: {bank_account_1.get_balance()}")
        elif user_choice == 6:
            new_exit_option = menu.add_option()
            if new_exit_option is not None:
                exit_option = new_exit_option
        else:
            print("\033[91mNew options logic is not implemented yet\033[0m")
        print()
        user_choice = menu.get_input()
    print("Exiting program")





