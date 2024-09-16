class Gadget:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}$")
    def apply_discount(self, discount):
        result = self.price - (self.price * discount / 100)
        self.price = round(result)
class Smartphone(Gadget):
    def __init__(self, brand, model, price, camera_resolution):
        super().__init__(brand, model, price)
        self.camera_resolution = camera_resolution
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}$")
        print(f"Camera resolution: {self.camera_resolution}")
class Laptop(Gadget):
    def __init__(self, brand, model, price, RAM_size):
        super().__init__(brand, model, price)
        self.RAM_size = RAM_size
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}$")
        print(f"RAM size: {self.RAM_size}")
class Tablet(Gadget):
    def __init__(self, brand, model, price, Battery_life):
        super().__init__(brand, model, price)
        self.Battery_life = Battery_life
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}$")
        print(f"Battery life: {self.Battery_life}H")

Poco_x3_pro = Smartphone("Poco", "X3", 200, "50MP")
Asus_tuf_dash_f15 = Laptop("Asus", "TUF", 19000, "16GB")
Samsung_Galaxy_tab = Tablet("Samsung", "Galaxy", 500, "24")
Poco_x3_pro.display_info()
Poco_x3_pro.apply_discount(50)
Poco_x3_pro.display_info()




