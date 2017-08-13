import random

# if using python 3.6 change to input
# if using python 2.7 change to raw_input

print("Would you like to use a random name, food, or haiku generator?")
user_input = raw_input()

#NAME GENERATOR
if user_input == "name":
    names = ["Nancy", "Zoe", "Saloni", "Stephanie", "Jess", "Abby", "Laura", "Grace", "Tania", "Iman", "Allie", "Jackie", "Annie", "Manal", "Layla", "Jessica", "Litsy", "Batool", "Kamronique"]
    print(random.choice(names))
    # result = list(enumerate(names))
    # print(result)

#MENU GENERATOR
if user_input == "food":
    sides = ["fries", "mac n' cheese", "baked potato", "cole slaw"]
    main = ["pizza", "hamburger", "cheeseburger", "steak"]
    drink = ["milkshake", "smoothie", "bubble tea", "soda", "water"]
    print(random.choice(sides))
    print(random.choice(main))
    print(random.choice(drink))

#HAIKU GENERATOR
if user_input == "haiku":
    first = ["the simplest penguin", "and it's quite easy", "like the great cookie", "to write a haiku", ]
    second = ["knows that every jouney starts", "to sound very sage and wise", "we must have honor and strength", "you just need to write three line", ]
    third = ["with a single step", "speaking with haiku", "and chocolate chips", "of 5, 7, 5", ]
    print(random.choice(first))
    print(random.choice(second))
    print(random.choice(third))
