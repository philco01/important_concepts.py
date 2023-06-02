from lesson4.Car import Car

car1 = Car()
car1.manufacturer = "Fiat"
car1.model = '500'
car1.year = 2010
car1.price = 4999.99
car1.has_abs = False
car1.show_details()
car1.print_abs()


car2 = Car("Fiat", "200", 2010, 1111, False)
