from colorama import Fore
class SalesData:
    def __init__(self):
        self.total_sales = 0

    def add_sale(self, amount):
        self.total_sales += amount

    def calculate_total(self):
        return self.total_sales

    def clear_total(self):
        self.total_sales = 0


class appTable:
    def __init__(self):
        self.logged_in = False
        self.waiter = None
        self.tables = {}
        self.stock = {}
        self.stock_prices = {}
        self.sales_data = SalesData()

    def login(self, username, password):
        with open("Login.txt", "r") as file:
            for line in file:
                saved_username, stored_password = line.strip().split(",")
                if username == saved_username and password == stored_password:
                    self.logged_in = True
                    self.waiter = username
                    return True
        return False

    def assign_table(self):
        if self.logged_in:
            if len(self.tables) >= 6:
                print(Fore.RED + "All tables are already assigned .It is physically impossible to assign more tables.")
            else:
                print(" all available tables:")
                for i in range(1, 7):
                    if i not in self.tables:
                        print(f"Table {i}")


                while True:
                    try:
                        table_number = int(input("enter the table number to assign (1-6): "))

                        if table_number in self.tables:
                            print("the table is already assigned to a waiter better choose another table")
                        elif table_number < 1 or table_number > 6:
                            print(Fore.RED + " table number wrong please enter a valid table number (1-6)" +Fore.LIGHTWHITE_EX)
                        else:
                            while True:
                                customers = input(Fore.LIGHTWHITE_EX + f"Do you actually want to add customers to the table?("+Fore.GREEN+"yes"+Fore.LIGHTWHITE_EX+"/"+ Fore.RED +"no"+Fore.LIGHTWHITE_EX+"): ")



                                if customers.lower() == "yes":
                                    while True:
                                        try:
                                            num_customers = int(input("enter the number of customers: "))
                                            self.tables[table_number] = {"waiter": self.waiter, "customers": num_customers}
                                            break
                                        except ValueError:
                                            print(Fore.RED+"oops that the wrong button please enter a valid number."+Fore.LIGHTWHITE_EX)
                                    break
                                elif customers.lower() == "no":
                                    self.tables[table_number] = {"waiter": self.waiter, "customers": 0}
                                    break
                                else:
                                    print(Fore.RED+ "Oospi wrong input Please enter "+Fore.GREEN+ "'yes'"+ Fore.LIGHTWHITE_EX+ " or" +Fore.RED + "'no'"+  Fore.LIGHTWHITE_EX)

                            print(f"Table {table_number} assigned to {self.waiter}.")
                            break
                    except ValueError:
                        print(Fore.RED+"Invalid input. Please enter a valid table number (1-6)."+ Fore.LIGHTWHITE_EX)
        else:
            print(Fore.RED+ "Please log in first."+ Fore.LIGHTWHITE_EX)

    def change_customers(self):
        if self.logged_in:
            assigned_tables = [table for table, info in self.tables.items() if info["waiter"] == self.waiter]
            if not assigned_tables:
                print("you are not assigned to a single physical table.")
                return

            print(f"Tables assigned to {self.waiter}:")
            for table in assigned_tables:
                print(f"Table {table}")

            while True:
                try:
                    table_number = int(input("Enter the table number to change customers ("+ Fore.RED+"0 to go back"+Fore.LIGHTWHITE_EX+"): "))

                    if table_number == 0:
                        return

                    if table_number not in self.tables:
                        print(Fore.RED+f"impossible table number {Fore.MAGENTA}please enter a table you are assigned to ({self.waiter})."+ Fore.LIGHTWHITE_EX)
                    elif self.tables[table_number]["waiter"] != self.waiter:
                        print("You can only change the number of customers for your assigned tables. Please choose assigned table.")
                    else:
                        while True:
                            try:
                                num_customers = int(input("enter the number of customers: "))
                                self.tables[table_number]["customers"] = num_customers
                                print(f"Number of customers for table {table_number} changed to {num_customers}.")
                                break
                            except ValueError:
                                print("imposible choice please enter a valid number.")
                        break
                except ValueError:
                    print("choice cannot be processed please enter a valid table number.")
        else:
            print("Please log in first.")

    def display_menu(self):
        with open("Stock.txt", "r") as file:
            for line in file:
                item_number, item_name, item_price = line.strip().split(",")
                self.stock[int(item_number)] = item_name
                self.stock_prices[int(item_number)] = float(item_price)

        print(Fore.BLUE+"\nMenu:"+Fore.LIGHTWHITE_EX)
        for item, name in self.stock.items():
            print(f"{item}. {name} - R{self.stock_prices[item]}")

    def add_to_order(self):
        if self.logged_in:
            print(f"Tables assigned to {self.waiter}:")
            assigned_tables = [table for table, info in self.tables.items() if info["waiter"] == self.waiter]
            if not assigned_tables:
                print("there are currenctly no tables assigned to you")
                return
            for table in assigned_tables:
                print(f"Table {table}")


            while True:
                table_number = input("Enter the table number to change customers ("+ Fore.RED+"0 to go back"+Fore.LIGHTWHITE_EX+"): ")
                if not table_number.isdigit():
                    print("please enter a valid table number.")
                    continue

                table_number = int(table_number)
                if table_number == 0:
                    return

                if table_number not in assigned_tables:
                    print("you can only add items to the order for your assigned tables. Please choose another table.")
                    continue

                if "order" not in self.tables[table_number]:
                    self.tables[table_number]["order"] = []

                while True:
                    self.display_menu()



                    item_number = input("Enter the item number to order (1-12): ")
                    if not item_number.isdigit() or int(item_number) < 1 or int(item_number) > 12:
                        print(Fore.RED + "there is no item number as such. Please try again.")
                        continue
                    item_number = int(item_number)
                    quantity = int(input("Enter the quantity of your choosinh: "))
                    self.tables[table_number]["order"].append((item_number, quantity))


                    another_item = input("Do you want to order another item? ("+Fore.GREEN+ "yes"+Fore.LIGHTWHITE_EX+"/"+Fore.RED+"no"+Fore.LIGHTWHITE_EX+"): ")
                    if another_item.lower() == "no":
                        break

                print(Fore.GREEN+ "items has been successfully added to your order." + Fore.LIGHTWHITE_EX)
                break
        else:
            print("please do the log in first.")

    def prepare_bill(self):
        if self.logged_in:
            print(f"Tables assigned to {self.waiter}:")
            assigned_tables = [table for table, info in self.tables.items() if info["waiter"] == self.waiter]
            if not assigned_tables:
                print(Fore.RED+"You don't have any assigned tables."+Fore.LIGHTWHITE_EX)
                return

            for table in assigned_tables:
                print(f"Table {table}")

            while True:
                table_number = input("pleasse the table number to prepare the bill ("+Fore.RED+"0 to go back"+Fore.LIGHTWHITE_EX+"): ")
                if not table_number.isdigit():
                    print(Fore.RED+"Please enter a valid table number."+Fore.LIGHTWHITE_EX)
                    continue

                table_number = int(table_number)
                if table_number == 0:
                    return

                if table_number not in assigned_tables:
                    print("You can only prepare the bill for your assigned tables. ")
                    continue

                table_info = self.tables[table_number]
                if table_info["waiter"] == self.waiter:
                    if "order" in table_info:
                        pay_total = 0
                        print(f"\nPAYMENT details for table {table_number}:")
                        print(f"Waiter: {table_info['waiter']}")
                        print("Items Purchased:")
                        print()
                        for item, quantity in table_info["order"]:
                            price = self.stock_prices[item]
                            item_total = price * quantity
                            print(
                                f"Item: {self.stock[item]}\t Quantity: {quantity}\t Price: R{price}\t Total: R{item_total}")
                            pay_total += item_total

                        print(f"\nTotal payment for table {table_number}: R{pay_total}")

                        self.print_bill(table_number)
                        del table_info["order"]
                        del table_info["waiter"]
                        del table_info["customers"]
                        print(f"The waiter who gladly helped was {self.waiter}")
                        print("the reciept is prepared.")
                    else:
                        print("No items in the order. Please add items to the order first.")
                else:
                    print(Fore.RED+"you can only prepare the reciept for your assigned tables"+Fore.LIGHTWHITE_EX)
        else:
            print(Fore.RED+"You need to log in first."+Fore.LIGHTWHITE_EX)

    def complete_sale(self):
        if self.logged_in:
            print(f"Tables assigned to {self.waiter}:")
            assigned_tables = [table for table, info in self.tables.items() if info["waiter"] == self.waiter]
            if not assigned_tables:
                print(Fore.RED+"CLEARLY you don't have any assigned tables. Please be assigned to a table first."+Fore.LIGHTWHITE_EX)
                return

            for table in assigned_tables:
                print(f"Table {table}")

            while True:
                try:
                    table_number = int(input("pleasse the table number to prepare the bill ("+Fore.RED+"0 to go back"+Fore.LIGHTWHITE_EX+"): "))
                    if table_number == 0:
                        return

                    if table_number not in assigned_tables:
                        print(Fore.RED+"You can only complete the sale for your assigned tables"+Fore.GREEN+" It would be wise to choose another table."+ Fore.LIGHTWHITE_EX)
                    else:
                        if "order" in self.tables[table_number]:
                            bill_total = 0
                            for item, quantity in self.tables[table_number]["order"]:
                                price = self.stock_prices[item]
                                bill_total += price * quantity

                            if bill_total > 0:
                                self.sales_data.add_sale(bill_total)
                                self.print_bill(table_number)
                                del self.tables[table_number]["order"]
                                del self.tables[table_number]["waiter"]
                                del self.tables[table_number]["customers"]
                                print(Fore.GREEN+"Sale completed successfully ."+ Fore.LIGHTWHITE_EX)
                            else:
                                print(Fore.RED+"there aint no items in the order. Please add items to the order first."+Fore.LIGHTWHITE_EX)
                        else:
                            print(Fore.RED+"THERE is literally no items in the order. Please add items to the order first."+ Fore.LIGHTWHITE_EX)
                        break
                except ValueError:
                    print(Fore.RED+ "input inserted is wrong do better enter a valid table number."+Fore.LIGHTWHITE_EX)
        else:
            print(Fore.RED+"You need to log in first."+ Fore.LIGHTWHITE_EX)

    def cash_up(self):
        if self.logged_in:
            total_income = self.sales_data.calculate_total()
            print("Total income from all sales: ${}".format(total_income))
            clear_total = input("Do you want to clear the daily total? ("+Fore.GREEN+"yes/"+Fore.RED+"no"+Fore.LIGHTWHITE_EX+"): ")
            if clear_total.lower() == "yes":
                self.sales_data.clear_total()
                print("Daily total cleared.")
        else:
            print(Fore.RED+"You need to log in first."+ Fore.LIGHTWHITE_EX)

    def logout(self):
        self.logged_in = False
        self.waiter = None
        print(Fore.GREEN+ "Logged out successfully."+ Fore.LIGHTWHITE_EX)



    def print_bill(self, table_number):
        filename = input("what is the a filename to save the bill: ")
        with open(filename, "w") as file:
            file.write(f"Table {table_number} - Waiter: {self.waiter}\n")
            file.write("Items ordered:\n")
            for item, quantity in self.tables[table_number]["order"]:
                file.write(f"{self.stock[item]} x {quantity}\n")
