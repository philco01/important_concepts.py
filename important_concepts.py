# ----lists----

# cars = ["toyota", "Getz", "fiat"]
# cars.append("mazda")
# print(cars)

# cars.insert(1, "Mitsubishi")
# print(cars)
# print(cars.index("Mitsubishi"))  # return location of mitsubishi
# print(cars.pop())  # pop out last element in list
# cars.remove("toyota")
# cars.insert(len(cars), "Mazda")
# cars.insert(0, "Toyota")
# cars.sort()  # make sorting by abc

# ----Set----
# a list that cant have duplicate elements
# like list can contain different elements

# cars = {"Toyota", "Mazda", "Fiat"}
# print(len(cars))
# cars.remove("Fiat")
# cars.remove("Fiat") # raise en error while not find
# cars.discard("Fiat")  # not raise en error
# cars.pop()
# cars.clear()  # returns empty set
# del cars  - deletes set totally
# cars_new = {"Mitsubishi", "BMW"}
# print(cars_new)
# cars_full = cars.union(cars_new)
# print(cars_full)  # its like an un ordered list
# cars.difference(cars_new)  # returns what exists in cars but not in cars_new

# ----Tuple----
# like a list but read only , immutable
# nums = (1, 2, 3)

# ----Dictionaries----
# dictionaries is a collection of items - data structure
# salary = {"Administration": 8000, "IT": 10000, "Support": 11000, "QA": 14000, "Automation": 18000}
# print(type(salary))
# print(salary.get("QA"))  # is similar to salary["QA"]
# list inside dictionary
# salary_with_list = {"Administration": 8000, "IT": 10000, "Support": 11000, "QA": [14000, 10000, 12000],
#                     "Automation": 18000}
# print(salary_with_list["QA"][1])
# print(salary_with_list["QA"].index(10000))
# nested dictionary
# emp = {"CEO": "Moshe", "VPRND": "David", "RND": {"QA": "Yoni", "DEV": "Chaim"}, "DBA": "Shlomo"}
# print(emp.get("RND").get("QA"))
# emp["Team Leader"] = "Yael"
# del emp["VPRND"]

# ----Input----
name = input("What is your name")
print("hello " + name)
