print('''
██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝
      ''')

class VendingMachine:
    def __init__(self):
        # Define the menu with items, categories, and prices
        self.menu = {
              'A1': {'item': 'Soda', 'category': 'Beverage', 'price': 1.50, 'stock': 10},
    'A2': {'item': 'Chips', 'category': 'Snack', 'price': 2.00, 'stock': 15},
    'B1': {'item': 'Lays', 'category': 'Snack', 'price': 2.25, 'stock': 20},
    'B2': {'item': 'Pepsi', 'category': 'Beverage', 'price': 3.00, 'stock': 8},
    'C1': {'item': 'Coffee', 'category': 'Beverage', 'price': 5.25, 'stock': 10},
    'D1': {'item': 'Snickers', 'category': 'Chocolate', 'price': 3.00, 'stock': 18},
    'D2': {'item': "Doritos", 'category': 'Snack', 'price': 1.75, 'stock': 20},
    'E1': {'item': "Reese's", 'category': 'Chocolate', 'price': 2.75, 'stock': 15},
    'E2': {'item': 'Kitkat', 'category': 'Chocolate', 'price': 2.75, 'stock': 12},
    'F1': {'item': 'Pretzels', 'category': 'Snack', 'price': 1.25, 'stock': 15},
    'F2': {'item': 'Cheetos', 'category': 'Snack', 'price': 1.50, 'stock': 18},
    'S1': {'item': 'Oman Chips', 'category': 'Snack', 'price': 1.25, 'stock': 15},
    'S2': {'item': 'Water', 'category': 'Beverage', 'price': 1.00, 'stock': 20},
    'G1': {'item': 'Tea', 'category': 'Beverage', 'price': 2.75, 'stock': 15},
    'G2': {'item': 'Juice', 'category': 'Beverage', 'price': 4.50, 'stock': 18},
    'M1': {'item': 'Cookie', 'category': 'Snack', 'price': 1.00, 'stock': 20},
            
        }

        # Initialize money in the machine
        self.total_money = 0.0

    def display_menu(self):
        # Display the menu to the user
        print("Menu:")
        for code, details in self.menu.items():
            print(f"{code}. {details['item']} ({details['category']}) - ${details['price']} - Stock: {details['stock']}")

    def accept_money(self):
        # Allow the user to input money
        amount = float(input("Insert money: $"))
        self.total_money += amount
        return amount

    def select_item(self):
        # Allow the user to input a code to select an item
        code = input("Enter the code of the item you want: ")
        return self.menu.get(code)

    def dispense_item(self, item):
        # Dispense the selected item
        print(f"Dispensing {item['item']}")
        item['stock'] -= 1

    def return_change(self, amount, item_price):
        # Calculate and return change
        change = amount - item_price
        if change > 0:
            print(f"Change: ${change}")
        else:
            print("Exact amount inserted. No change.")

    def suggest_purchase(self, category):
        # Suggest a purchase based on the selected item's category
        suggestions = [details['item'] for code, details in self.menu.items() if details['category'] == category]
        if suggestions:
            print(f"Consider buying {', '.join(suggestions)} with your {category.lower()}.")
        else:
            print("No suggestions available for this category.")

    def operate(self):
        # Main method to operate the vending machine
        self.display_menu()
        item = self.select_item()

        if item:
            price = item['price']
            money_inserted = self.accept_money()

            if money_inserted >= price and item['stock'] > 0:
                self.dispense_item(item)
                self.return_change(money_inserted, price)

                # Ask if the user wants to buy additional items
                additional_purchase = input("Do you want to buy another item? (yes/no): ").lower()
                if additional_purchase == 'yes':
                    self.display_menu()
                    additional_item = self.select_item()
                    if additional_item and additional_item['stock'] > 0:
                        additional_price = additional_item['price']
                        additional_money_inserted = self.accept_money()
                        if additional_money_inserted >= additional_price:
                            self.dispense_item(additional_item)
                            self.return_change(additional_money_inserted, additional_price)
                        else:
                            print("Insufficient funds for additional item. No change returned.")
                    else:
                        print("Invalid code or out of stock for additional item.")

                # Suggest a purchase based on the selected item's category
                self.suggest_purchase(item['category'])

            elif item['stock'] == 0:
                print("Out of stock for the selected item.")
            else:
                print("Insufficient funds. Please insert more money.")

        else:
            print("Invalid code. Please try again.")


# Instantiate the vending machine
vending_machine = VendingMachine()

# Run the vending machine
vending_machine.operate()
