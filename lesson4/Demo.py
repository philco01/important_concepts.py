class Demo:
    # my_list = []

    def __init__(self, mlist):
        self.my_list = mlist

    def handle_numbers(self):
        print("min number is ", self.min_number())
        print("max number is", self.max_number())
        print("average number is ", int(self.average_number()))

    def min_number(self):
        min_number = self.my_list[0]
        for num in self.my_list:
            if num < min_number:
                min_number = num
        return min_number

    def max_number(self):
        max_number = self.my_list[0]
        for num in self.my_list:
            if num > max_number:
                max_number = num
        return max_number

    def average_number(self):
        ave = self.my_list[0]
        for num in self.my_list:
            ave += num
        return ave / len(self.my_list)
