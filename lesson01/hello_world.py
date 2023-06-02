print("hello world", end="")  # means print both lines no new line
print("it is a fucked up day")

a = 1
print(id(a))  # address of variable in memory

a = None
print(type(a))  # prints type of given variable

# example:
# a,b,c =1,2,"Moshe"  - equals to a=1 b=2 c="Moshe'
# a=true b=1 -> print(a+b) -> 2
text = "hello world"
text.
print(text.upper())  # to upper all letters
print(len(text))  # length of string
# print(text.replace('hello', 'shit'))
print(text[1:4])  # prints substring includes from 1 but not include 4
print(text[:2])  # will print he
# no concatenation in python , in order to make concat use type cast
my_list = ["Moshe", "David",
           "Yoni"]  # lists like arrays in java, every ruly for strings are relevant for lists (functions)
print(my_list.insert(3, "yael"))
# find and index returns locations of var , index returns error if not found
# find will return -1  if not find value
my_list.pop(1)  # deletes var at given location
# my_list.remove('David')  # remove david
my_set = {"moshe", "david", "moshe"}  # set cannot contain duplicates

print(my_set)
countries = {1: "russia", 2: "canada", 3: "brazil"}  # dictionaries - key value pairs
print(countries.get(2)) # its like countries[2]

nums = (1, 2, 3)  # Tuple its a list but cant be altered - immutable
name = input("what is your name ")
