ingredients = {
    "creamy peanut butter": "- one jar",
    "strawberry jelly": "- one jar",
    "bread": "- two slices",
    "one": "knife"
}

instructions = {
    "ONE": "- spread peanut butter on one slice of bread with the knife",
    "TWO": "- on the other slice, use the knife to spread jelly",
    "THREE": "- with the peanut butter and jelly facing each other, combine the two slices",
    "FOUR": "- eat the sandwich, become the sandwich"
}

print ("PEANUT BUTTER AND JELLY SANDWICH")
print("you will need:")
for ingredient, amount in ingredients.items():
    print(ingredient, amount)
for instruction, amount in instructions.items():
    print(instruction, amount)
