# Banking program python

# features ("example on program contents " not necessary)

# 1.Show Balance
# 2. Deposit
# 3.Withdraw

def show_balance(balance):
    print(f"your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    print("*********************************")

    if amount < 0:
        print("*********************************")
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    print("*********************************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("*********************************")

    if amount > balance:
        print("*********************************")
        print("Insufficient funds")
        print("*********************************")
        return 0
    elif amount < 0:
        print("*********************************")
        print("Amount must be greater than zero ")
        print("*********************************")
        return 0
    else:
        return amount

def main():
    balance = 0           # global value (balance and is_running) continuos from here and
    is_running = True      #global values (balance and is_running) will  applied from here

    while is_running:
        print("*********************************")
        print("Banking Program")
        print("*********************************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*********************************")

        choice = input("Enter your choice (1:4) : ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*********************************")
            print("That is not a valid choice")
            print("*********************************")

    print("*********************************")
    print("Thank you have a nice day !")
    print("*********************************")
if __name__ == '__main__':
    main()