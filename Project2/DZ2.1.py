class Client:
    def __init__(self, name, email):
        self.orders = []
        self.name = name
        self.email = email
    def add_order(self, *args):
        for order in args:
            self.orders.append(order)
            print("New order added succesfully!")
    def show_orders(self):
        if self.orders != []:
            print("All orders of that customer")
            print("---------------------------")
            for order in self.orders:
                order.show_info()

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        print(self.name)
        print(f"{self.price}$")
        print("---------------------------")


class TotalOrder:
    def __init__(self, customer):
        self.customer = customer
        self.itemList = []
    def add_item(self, item):
        self.itemList.append(item)
        print(f"Added to {item} order succesfully!")
    def get_total(self):
        total_value = sum(item.price for item in self.itemList)
        print(total_value)
    def show_info(self):
        total_value = sum(item.price for item in self.itemList)
        print(f"Client: {self.customer.name}")
        print(f"Items: ")
        for iList in self.itemList:
            print(f"{iList.name}/{iList.price}")
        print(f"Total price: {total_value}")












jim = Client("jim", "nan")
order1 = TotalOrder(jim)
Bread = Item("Bread", 20)
Milk = Item("Milk", 13)
Egg = Item("Egg", 3)
jim.add_order(order1)
order1.add_item(Egg)
order1.add_item(Bread)
order1.add_item(Milk)
order1.get_total()
jim.show_orders()





