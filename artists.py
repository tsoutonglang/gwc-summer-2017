class Artist:

    def __init__(self, name):
        self.name = name
        self.paintings = 0
        self.famous = []

    def num_painting(self, paintings):
        self.paintings = paintings

    def famous_work(self, famous):
        self.famous.append(famous)

#actual artists now

vanGough = Artist("Vincent Van Gough")
vanGough.num_painting(900)
vanGough.famous_work("The Starry Night")

marcusTo = Artist("Marcus To")
marcusTo.num_painting(65)
marcusTo.famous_work("the Red Robin series")

picasso = Artist("Picasso")
picasso.num_painting(50000)
picasso.famous_work("The Old Guitarist")

michelangelo = Artist("Michelangelo")
michelangelo.famous_work("The Creation of Adam")

rembrandt = Artist("Rembrandt")
# rembrandt.num_paintings()
rembrandt.famous_work("The Anatomy Lesson of Dr. Nicolaes Tulp")

print("welcome to the hall of artists. please choose a style:")
print("post impressionism, comic, cubism, renaissance, baroque?")
user_input = input()
if user_input == "post impressionism":
    print("Vincent Van Gough")
    print("paintings made:")
    print(vanGough.paintings)
    print("one most notable work:" + (str(vanGough.famous)))
elif user_input == "comic":
    print("Marcus To")
    print("paintings made:")
    print(marcusTo.paintings)
    print("one most notable work:" + (str(marcusTo.famous)))
elif user_input == "cubism":
    print("Pablo Picasso")
    print("paintings made:")
    print(picasso.paintings)
    print("one most notable work:" + (str(picasso.famous)))
elif user_input == "renaissance":
    print("Michelangelo")
    print("one most notable work:" + (str(michelangelo.famous)))
elif user_input == "baroque":
    print("Rembrandt")
    #print("paintings made:)
    #print(rembrandt.paintings)
    print("one most notable work:" + (str(rembrandt.famous)))
