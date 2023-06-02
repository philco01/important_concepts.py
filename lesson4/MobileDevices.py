class MobileDevice:
    screen_height = 0
    screen_width = 0
    model = " "
    os = " "
    version = 0
    has_flash = False
    price = 0.0

    def __init__(self, width, height, model, os, version, has_flash, price):
        if width and height >= 0:
            self.screen_width = width
            self.screen_height = height
        else:
            print("cant calculate negative numbers")
        self.model = model
        self.os = os
        self.version = version
        self.has_flash = has_flash
        self.price = price

    def print_parameters(self):
        print("the model is:" + str(self.screen_width))
        print("the model is:" + str(self.screen_height))
        print("the model is:" + self.model)
        print("the operating system is:" + self.os)
        print("the version is:" + str(self.version))
        print("the flash is:" + str(self.has_flash))
        print("the price is:" + str(self.price))

    def calculate_area(self):
        print(self.screen_height * self.screen_width)

    def picture_quality(self):
        if self.has_flash:
            print("good quality")
        else:
            print("bad quality")
