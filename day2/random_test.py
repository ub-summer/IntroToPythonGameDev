import random

for i in range(100):
    x = random.randint(1, 100)
    if x == 100 or x == 1:
        print("x == " + str(x))


my_list = [2, 3, 5, 7, 11, 13]

for value in my_list:
    print(value)


my_dictionary = {"player": "Steve", "hp": 10,
                 "max_hp": 10}

print(my_dictionary["hp"])


grocery_list = ["milk", "eggs", "bread"]
grocery_dict = {"milk": 1, "eggs": 12, "bread": 2}