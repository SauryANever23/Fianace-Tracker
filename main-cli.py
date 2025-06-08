import os
import time
import sys

class Finance():

    def brk():
        print("\a")
        input("\n\npress enter to continue \n")

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

        os.system('clear')
        try:
            add_choice: int = int(input("Enter the amount to deposit (or type 'exit' to exit): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            # time.sleep(0.5)
            Finance.balance_information()
        
        with open('balance.txt', 'r') as f:
            b1 = f.read()
        b2 = int(b1) + int(add_choice)

        with open('balance.txt', 'w') as r:
            r.write(str(b2))

    def view_information() -> str:
        """
        os.system('cls')  # Clear the screen
        current_balance = Finance.get_balance()
        print(f"Current balance: ${current_balance}")
        total_expenses = Finance.get_total_expenses()
        print(f"Total expenses: ${total_expenses}")
        """

        os.system('clear')
        try:
            with open('balance.txt', 'r') as f:
                balance = f.read()
                return balance
        except:
            print("File not found")
        
        

    def balance_information() -> None:
        """
        This function will display the current balance and total expenses.
        """
        os.system('clear')  # Clear the screen
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
            balance = Finance.view_information()
            print(f"amount: NRs. {balance}")
            Finance.brk()
        elif balance_choice == 2:
            Finance.add_balance()
            Finance.brk()
        elif balance_choice == 3:
            Finance.remove_balance()
            Finance.brk()
        else:
            print("Invalid choice. Please try again.")
            Finance.brk()

    def menu_screen() -> None:
        """
        This functino will display the menu screen at the begginig of the application:
        this will ajorly be something of no 
        """
        os.system('clear')  # Clear the screen
        
        while True: 
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
            choice = int(input("Enter choice: "))

            if choice == 1:
                Finance.balance_information()
            elif choice == 2:
                Finance.expenditure_status()
            elif choice == 3:
                Finance.invetments()
            elif choice == 4:
                Finance.inflation()
            elif choice == 5:
                sys.exit()
                break
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
