# print("philip", end='')
# print("itkin", end='')
# print(36, end='')

# name = "philip"
# last_name = "itkin"
# age = 3
# print(name, last_name, age)

# exercise 1 : strings
# name = "Philip"
# second_name = "Itkin"
# age = 36
# age = str(age)
# print(name.upper())
# print(second_name.lower())
# print(name[1:])
# print(name[:len(name)-1])

# exercize 2 : strings
# word = "Python is a general purpose computer programming language"
# print(word.count("computer"))
# print(word.index("computer"))
# print(word.replace(' ', ''))

# exercize 3 : strings
# word = "Hello World"
# last_word = word.split(' ')
# print(last_word[1])

# yoni solution
# greet = "Hello World"
# index_of_space = greet.find(" ")
# print(greet[index_of_space + 1:])

# exercize 1 : lists
# countries = ["Italy", "Austria", "Ukraine", "USA", "Greece"]
# print(countries[0:3])
# temp = countries[0]
# countries[0] = countries[1]
# countries[1] = temp
# print(countries)
# countries.sort()
# print(countries)
# last_country = countries.pop(len(countries)-1)
# print(countries)
# middle = int(len(countries)/2)
# countries.insert(middle, "Zanzibar")
# print(countries)

# exercize dictionaries
# family = {"dad": "Aleksandr", "mom": "Viktorya", "grandmother": "Galina", "grandfather": "Nahum"}
# print(family)
# print(len(family))
# family["wife"] = "Hatuka"
# print(family)

# odd or even number after input
# year = int(input("Enter your birth year: "))
# print("Is your birth year a pair year ?",  year % 2 == 0)

# statements
# 1 exercize
# x = 10
# y = 20
# if x > y:
#     print("value x is bigger then y:" + str(x))
# elif x < y:
#     print("value y is bigger then x" + str(y))
# else:
#     print("they are equal")

# exercise 2
# nums = [2, 5, 9]
# nums[0] = 8
# if nums[0] > nums[1]:
#     print("first one is bigger")
# elif nums[1] > nums[0]:
#     print("second one is bigger")
# else:
#     print("they are equal")

# exercise 3

# for num in range(1, 11):
#     print(num)
# num = 1
# while num <= 10:
#     print(num, end='')
#     num += 1
# for num in range(30, 50):
#     if num % 2 == 0:
#         print(num)
# for num in range(20, 40):
#     if num % 2 != 0:
#         print(num)

# exercise 4
# countries = ["Austria", "Germany", "Canada", "Peru", "Israel"]
# for cntr in countries:
#     print(cntr, end=' ')


# country = 0
# while country < len(countries):
#     if countries[country] == "Israel":
#         print(countries[country])
#     country += 1

# for country in countries:
#     if country == "Israel":
#         print("Israel")

# for cntr in countries:
# if cntr != countries[3]:
#     continue
# else:
#     if countries[3] == "China":
#         print("yes , its there")
#     else:
#         print("its not there")
# yoni solution
# if countries[3] == "China":
#     print("Yes, it is there")
# else:
#     print("No, Sorry...")

# exercize 4 d
# print(len(countries[0]))

# exercise 5
# number = int(input("the number is"))
# if 0 < number <= 6:
#     print("go to kindergarten")
# elif number in range(7, 19):
#     print("go to school")
# elif number in range(19, 68):
#     print("go to work")
# elif number in range(68, 121):
#     print("collect pension")

# exercise 6
# profession = input("what is your profession")
# if profession == "Teacher":
#     print("your salary is 5000")
# elif profession == "Bank Teller":
#     print("your salary is 10000")
# elif profession == "QA":
#     print("your salary is 15000")
# elif profession == "Average Salary":
#     print("your salary is 9100")

# exercise 7
# ids = {12345: "Yoni", 45678: "Moshe", 54321: "David"}
#
# for nums in ids:
#     print("ID: " + str(nums))
# for val in ids.values():
#     print("Name: " + val)

# exercise 8
# my_set = {23, 45, 54, 35, 55, 15, 30}
# for num in my_set:
#     if num % 3 == 0 and num % 5 == 0:
#         print(num, end=' ')

# exercise 9
# my_list = ["h", "e", "l", "l", "o"]
# num = 0
# last = len(my_list) - 1
# reverse = []
# while num < len(my_list):
#     reverse.append(my_list[last])
#     last -= 1
#     num += 1
# print(reverse)
# word = ['o', 'l', 'l', 'e', 'h']
# while len(word) > 0:
#     print(word.pop(), end='')
# print()

# exercise 10
# numbers = [15, 2, 36, 20, 7]


# for num in my_list:
#     if my_list[0] > my_list[1]:
#         if my_list[0] > my_list[3]:
#             print(my_list[0])
#         else:
#             print(my_list[2])
#     else:
#         if my_list[1] > my_list[2]:
#             print(my_list[1])
#         else:
#             print(my_list[2])

# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print("The maximum value of the list:", max)

# sum = 0
# for num in numbers:
#     sum += num
# print(sum)

# exercise 11
# num = int(input("Enter a number: "))
# is_prime = True
# for i in range(2, int(num/2)+1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

# functions
# exercise 1
# def reverse_str(text):
# i = len(text) - 1
# new_text = ""
# while i >= 0:
#     new_text += text[i]
#     i -= 1
# print(new_text)
# exercise 2:
# def max_number(first, second, third):
#     if first > second and first > third:
#         return first
#     elif second > first and second > third:
#         return second
#     else:
#         return third

# exercise 3
# def unique_list(my_list):
#     my_set = {0}
#     for member in my_list:
#         my_set.add(member)
#     print(my_set)


# exercise 4
# def factorial(number):
#     if number > 0:
#         i = number - 1
#         while i > 0:
#             number *= i
#             i -= 1
#         print(number)
#     elif number == 0:
#         print(1)
#     else:
#         print("not positive number ")

# exercise errors
# def print_message(value):
#     try:
#         message = value + " - OK"
#         print("No problem, just print the message...")
#         print(message)
#     except TypeError:
#         print("You should know, there was a type error in your program, but I fixed it...")
#         message = str(value) + " - OK"
#         print(message)
text = "hello world"


def write_func(name):
    name = open(r"name.txt", "w")
    name.write(text)
    name.close()
    

write_func("fila_name")
