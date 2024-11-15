import os
import time
class Finance():

    def add_balance() -> None:
        """
        os.system('cls')  # Clear the screen
        print("Enter the amount to deposit:")
        deposit_amount = float(input())
        current_balance = Finance.get_balance()
        new_balance = current_balance + deposit_amount
        Finance.set_balance(new_balance)
        print(f"New balance: ${new_balance}")
        """

        os.system('cls')
        try:
            add_choice: int = int(input("Enter the amount to deposit (or type 'exit' to exit): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            # time.sleep(0.5)
            Finance.balance_information()
        
        with open('balance.txt', 'a') as f:
            f.write(str(add_choice))

    def view_information() -> None:
        """
        os.system('cls')  # Clear the screen
        current_balance = Finance.get_balance()
        print(f"Current balance: ${current_balance}")
        total_expenses = Finance.get_total_expenses()
        print(f"Total expenses: ${total_expenses}")
        """

        os.system('cls')

        with open('balance.txt', 'r') as f:
            f.read()
        
        

    def balance_information() -> None:
        """
        This function will display the current balance and total expenses.
        """
        os.system('cls')  # Clear the screen
        print("""
        -------------------
        O P T I O N S
        -------------------

        [1] View Balance
        [2] Deposit
        [3] Withdraw(remove)
        
        """)

        balance_choice = int(input("Enter Choice(use int: )"))

        if balance_choice == 1:
            Finance.view_information()
        elif balance_choice == 2:
            Finance.add_balance()
        elif balance_choice == 3:
            Finance.remove_balance()
        else:
            print("Invalid choice. Please try again.")

    def menu_screen() -> None:
        """
        This functino will display the menu screen at the begginig of the application:
        this will ajorly be something of no 
        """
        os.system('cls')  # Clear the screen

        
        print(""" 
            ''''''''''''''''''''''''''''''''''''''''
                F I N A N C E   T R A C K E R
            ''''''''''''''''''''''''''''''''''''''''
              CHOOISE THE FOLLOWING:

              [1] Balance Information
              [2] Expenditure And Stuatus
              [3] Investments, Progress
              [4] Inflation, Adjustments, etc
              [5] Exit
                    """)
        choice = int(input("Enter your choice: "))

        if choice == 1:
            Finance.balance_information()
        elif choice == 2:
            Finance.expenditure_status()
        elif choice == 3:
            Finance.invetments()
        elif choice == 4:
            Finance.inflation()
        elif choice == 5:
            print("Exiting...")
        else:
            print("Invalid choice. Please try again.")



def main() -> None:
    """
    The main code and application is wriiten in this app
    """

    Finance.menu_screen()

if __name__ == '__main__':
    main()