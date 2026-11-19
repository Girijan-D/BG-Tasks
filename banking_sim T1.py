
balance = 5000
pin = 1234

entered_pin = int(input("Enter your PIN: "))

match entered_pin == pin:
    case True:
        print("\nLogin Successful!")

        while True:
            print("\n----- BANKING SYSTEM -----")
            print("1. Cash Deposit")
            print("2. Cash Withdrawal")
            print("3. Balance Enquiry")
            print("4. Transaction History")
            print("5. Exit")

            choice = int(input("Enter your choice: "))
 
            match choice:
                case 1:
                    amount = float(input("Enter deposit amount: "))
                    match amount > 0:
                        case True:
                            balance += amount
                            with open("transactions.txt", "a") as file:
                                file.write(f"Deposited: Rs.{amount}\n")
                            print("Amount deposited successfully!")
                        case False:
                            print("Invalid amount!")

                case 2:
                    amount = float(input("Enter withdrawal amount: "))
                    match amount > 0 and amount <= balance:
                        case True:
                            balance -= amount
                            with open("transactions.txt", "a") as file:
                                file.write(f"Withdrawn: Rs.{amount}\n")
                            print("Please collect your cash.")
                        case False:
                            print("Invalid amount or insufficient balance!")

                case 3:
                    print("Available Balance:", balance)

                case 4:
                    print("\n----- TRANSACTION HISTORY -----")
                    try:
                        with open("transactions.txt", "r") as file:
                            print(file.read())
                    except FileNotFoundError:
                        print("No transactions yet!")

                case 5:
                    print("Thank you for using our banking system!")
                    break

                case _:
                    print("Invalid choice!")

    case False:
        print("Incorrect PIN! Access Denied.")
