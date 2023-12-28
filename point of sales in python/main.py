from pos import appTable
from pos import SalesData
from colorama import Fore
def main():
    pos_app = appTable()

    while True:
        print(Fore.LIGHTBLUE_EX+ "Welcome to the Point of Sale Application!")
        print(Fore.LIGHTWHITE_EX)
        print("1. Login")
        print(Fore.RED+"0. Exit")
        print(Fore.LIGHTWHITE_EX+ ' ')

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if pos_app.login(username, password):
                while True:
                    print("\nMain Menu:")
                    print("1. Assign Table")
                    print("2. Change customers")
                    print("3. Add to Order")
                    print("4. Prepare bill")
                    print("5. Complete Sale")
                    print("6. Cash up")
                    print(Fore.RED+"0. Log Out")
                    print(Fore.LIGHTWHITE_EX)

                    option = input("Enter your option: ")

                    if option == "1":
                        pos_app.assign_table()

                    elif option == "2":
                        pos_app.change_customers()

                    elif option == "3":
                        pos_app.add_to_order()

                    elif option == "4":
                        print("--------------------------------------------------------------")
                        pos_app.prepare_bill()
                        print("---------------------------------------------------------------")
                    elif option == "5":
                        pos_app.complete_sale()

                    elif option == "6":
                        pos_app.cash_up()

                    elif option == "0":
                        pos_app.logout()
                        break

                    else:
                        print(Fore.RED + "impossible option. Please try again."+ Fore.LIGHTWHITE_EX)

            else:
                print(Fore.RED + "Invalid username or password. Please try again."+ Fore.LIGHTWHITE_EX)

        elif choice == "0":
            break

        else:
            print(Fore.RED+ "Impossible option do better and try again.")
            print(Fore.LIGHTWHITE_EX)

if __name__ == "__main__":
    main()
