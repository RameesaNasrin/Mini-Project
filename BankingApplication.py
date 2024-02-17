
# MINI PROJECT

"""Write a Python program to replicate a Banking system. The following features are mandatory:
1.Account login
2.Amount Depositing
3.Amount Withdrawal
Other than the above features you can add any other also."""

print("\n**************WELCOME TO OUR BANKING APPLICATION**************")

account_balance = {"ACCOUNT BALANCE":1500}

#method to restrict user input

def _input(message, input_type=str):
    while True:
        try:
            return input_type(input(message))
        except:
            print("Invalid input.Try again.")

# Necessary variables
account_number=0
pin=0
choice = ""

# Dictionary to store user transactions
receipt_dict = {}

# Login method
def login():
    global account_number
    global pin
# Ask user to enter account number and pin number.
    if __name__ == "__main__":
        account_number= _input("\nPlease enter your account number:",int)
        pin = _input("Please enter account pin code:",int)

# Home page method
def home_page():
    global choice
    print("\n****************************")
    print("What do you want to do?")
    print(f"\t ACCOUNT BALANCE:${account_balance,['ACCOUNT BALANCE']}\n\t 1:Withdrawal(W)\n\t 2:Credit(C)\n\t 3:Transfer Money(TM)\n\t 4:Logout(LO)")
    print("*****************************")
    if __name__ == "__main__":
        choice =_input("Please select operation:",str).upper()

login()
while True:
    if account_number==123 and pin==123:
        home_page()
        withdrawal_money=0
        credit_money=0
        money_transfer=0
        if choice == "W":
            if __name__ == "__main__":
                withdrawal_money=_input("Enter the amount you want to withdraw:",float)
            # Check if account balance is less than the withdrawal money or not
            if withdrawal_money <= account_balance['ACCOUNT BALANCE']:
                account_balance['ACCOUNT BALANCE'] -= withdrawal_money
                print("*********TRANSACTION SUCCESSFUL*********")
            else:
                print("\n*********TRANSACTION ERROR***********")
        elif choice == "C":
            if __name__ == "__main__":
                credit_money = _input("Enter the amount you want to deposit:",float)
            account_balance['ACCOUNT BALANCE'] += credit_money
            print("\n*********TRANSACTION SUCCESSFUL*********")
        elif choice == "TM":
            print("\nNOTE:TRANSFER FEE FOR EACH TRANSACTION IS 0.03(3%)")
            if __name__ == "__main__":
                receipt_dict["BANK NAME"]=_input("BANK NAME:",str)
                receipt_dict["BANK BRANCH CODE"] = _input("BRANCH CODE:", str)
                receipt_dict["ACCOUNT HOLDER NAME"] = _input("ACCOUNT HOLDER NAME:", str)
                receipt_dict["RECIPIENT ACCOUNT NUMBER"] = _input("RECIPIENT ACCOUNT NUMBER:",int)
                receipt_dict["TRANSFER AMOUNT(in$)"] = _input("TRANSFER AMOUNT(in$):", float)
            receipt_dict["TRANSFER FEE"] = receipt_dict["TRANSFER AMOUNT(in$)"]*0.03 #3%
            receipt_dict["TOTAL DEBIT"] = receipt_dict["TRANSFER AMOUNT(in$)"]+receipt_dict["TRANSFER FEE"]
            # check if account balance is less than or greater than the transfer money
            if account_balance['ACCOUNT BALANCE']> receipt_dict["TOTAL DEBIT"]:
                account_balance['ACCOUNT BALANCE'] -= receipt_dict["TOTAL DEBIT"]
                print("\n*********TRANSACTION SUCCESSFUL*********")
            # Ask user if he/she want to print a reciept or not
                user_choice= input("Would you like to print a receipt or not?(y/n):").lower()
                if user_choice.startswith('y'):
                    print("\n\t*************TRANSACTION HISTORY************")
                    [print(f"\t{x}************{y}") for x,y in receipt_dict.items()]
                    print(f"\tREMAINING ACCOUNT BALANCE***********{account_balance['ACCOUNT BALANCE']}")
                else:
                    print("YOU DON'T WANT TO PRINT THE RECEIPT")
            else:
                print(("\n*********INSUFFICIENT BALANCE*********"))
        elif choice=="LO":
            print("\n LOGGING YOU OUT*********** GOODBYE!")
            break

    elif account_number == 123 and pin != 123:
        print("Pin is incorrect. Try again")
        login()
    elif account_number != 123 and pin == 123:
        print("Account number is incorrect. Try again")
        login()
    elif account_number != 123 and pin != 123:
        print("Account number and Pin is incorrect. Try again")
        login()


