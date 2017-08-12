import csv
import string

print("Welcome to World Star Airlines! We thank you for choosing us for your travels. Please choose a country to determine your trip.")
want = input("choose a country: ");

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)

# def binary_search(countries, want):
lowerBound = 0
upperBound = (length - 1)
midpoint = 16
# print(midpoint)
# print(length)

while lowerBound != upperBound:
    if want == countries[midpoint]:
        print ("get a plane ticket to " + want)
        break
    elif want > countries[midpoint]:
        lowerBound = (midpoint + 1)
        midpoint = ((lowerBound + upperBound)// 2)
    elif want < countries[midpoint]:
        upperBound = (midpoint - 1)
        midpoint = ((lowerBound + upperBound) // 2)
    elif want == countries[midpoint]:
        print ("go get a plane ticket to " + want)
        break
if lowerBound == upperBound:
    # print (midpoint)
    print ("no plane tickets available to " + want)
