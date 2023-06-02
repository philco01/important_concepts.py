class Car:
    manufacturer = ' '
    model = " "
    year = 0
    price = 0.0
    has_abs = False

    def __init__(self, manufacturer, model, year, price, has_abs):   # constructor
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.price = price
        self.has_abs = has_abs

    def show_details(self):
        print("Manufacturer:" + self.manufacturer)
        print("Model:" + self.model)
        print("Year:" + str(self.year))
        print("Price:" + str(self.price))
        print("Has Abs:" + str(self.has_abs))

    def print_abs(self):
        if self.has_abs==True:
            print("good car")
        else:
            print("bad car")
