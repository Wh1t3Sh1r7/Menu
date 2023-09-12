class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_menu(self):
        print("Menu:")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item.name} - {item.price:.2f} USD")
            print(f"   {item.description}")
            print()

def main():
    menu = Menu()

    item1 = MenuItem("Burger", "A delicious burger with cheese and veggies.", 5.99)
    item2 = MenuItem("Pizza", "A classic pizza with your choice of toppings.", 8.99)
    item3 = MenuItem("Pasta", "Pasta with marinara sauce and garlic bread.", 6.99)

    menu.add_item(item1)
    menu.add_item(item2)
    menu.add_item(item3)

    while True:
        print("Welcome to the Online Menu!")
        menu.display_menu()
        choice = input("Enter the number of the item you want to order (or 'q' to quit): ")

        if choice == 'q':
            break

        try:
            choice = int(choice)
            if 1 <= choice <= len(menu.items):
                selected_item = menu.items[choice - 1]
                print(f"You selected: {selected_item.name} - {selected_item.price:.2f} USD")
            else:
                print("Invalid choice. Please enter a valid item number.")
        except ValueError:
            print("Invalid input. Please enter a valid item number or 'q' to quit.")

if __name__ == "__main__":
    main()
