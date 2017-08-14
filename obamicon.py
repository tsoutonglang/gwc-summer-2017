from PIL import Image

# Import image.
print("choose a picture")
color = input()+".jpg"
my_image = Image.open("img/"+color) #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
print("chose a color scheme: rap monster, jin, suga, jhope, jimin, v, jungkook, or murica")
color = input()

if color == "rap monster":
    darkRed = (48, 3, 18)
    red = (168, 43, 94)
    shadow = (148, 205, 193)
    cream = (217, 245, 241)
    for pixels in image_list:
        if pixels[0] + pixels[1] + pixels[2] < 182:
            recolored.append(darkRed)
        elif pixels[0] + pixels[1] + pixels[2] > 182 and pixels[0] + pixels[1] + pixels[2] < 364:
            recolored.append(red)
        elif pixels[0] + pixels[1] + pixels[2] > 364 and pixels[0] + pixels[1] + pixels[2] < 546:
            recolored.append(shadow)
        else:
            recolored.append(cream)
if color == "jin":
    gray = (60, 66, 85)
    turquoise = (21, 156, 152)
    pink = (251, 151, 163)
    lightPink = (255, 224, 228)
    for pixels in image_list:
        if pixels[0] + pixels[1] + pixels[2] < 182:
            recolored.append(gray)
        elif pixels[0] + pixels[1] + pixels[2] > 182 and pixels[0] + pixels[1] + pixels[2] < 364:
            recolored.append(turquoise)
        elif pixels[0] + pixels[1] + pixels[2] > 364 and pixels[0] + pixels[1] + pixels[2] < 546:
            recolored.append(pink)
        else:
            recolored.append(lightPink)
if color == "suga":
    black = (41, 37, 44)
    gold = (128, 91, 75)
    yellow = (189, 169, 129)
    cream = (209, 231, 216)
    for pixels in image_list:
        if pixels[0] + pixels[1] + pixels[2] < 182:
            recolored.append(black)
        elif pixels[0] + pixels[1] + pixels[2] > 182 and pixels[0] + pixels[1] + pixels[2] < 364:
            recolored.append(gold)
        elif pixels[0] + pixels[1] + pixels[2] > 364 and pixels[0] + pixels[1] + pixels[2] < 546:
            recolored.append(yellow)
        else:
            recolored.append(cream)
if color == "jhope":
    black = (22, 44, 48)
    orange = (187, 128, 71)
    shadow = (201, 182, 137)
    highlight = (225, 234, 226) #SVT DANCE BREAK
    for pixels in image_list:
        if pixels[0] + pixels[1] + pixels[2] < 182:
            recolored.append(black)
        elif pixels[0] + pixels[1] + pixels[2] > 182 and pixels[0] + pixels[1] + pixels[2] < 364:
            recolored.append(orange)
        elif pixels[0] + pixels[1] + pixels[2] > 364 and pixels[0] + pixels[1] + pixels[2] < 546:
            recolored.append(shadow)
        else:
            recolored.append(highlight)
if color == "jimin":
    darkPurple = (37, 29, 43)
    red = (164, 34, 49)
    lightPurple = (152, 144, 152)
    green = (205, 220, 210)
    for pixels in image_list:
        if pixels[0] + pixels[1] + pixels[2] < 182:
            recolored.append(darkPurple)
        elif pixels[0] + pixels[1] + pixels[2] > 182 and pixels[0] + pixels[1] + pixels[2] < 364:
            recolored.append(red)
        elif pixels[0] + pixels[1] + pixels[2] > 364 and pixels[0] + pixels[1] + pixels[2] < 546:
            recolored.append(lightPurple)
        else:
            recolored.append(green)
if color == "v":
    darkPurple = (45, 14, 40)
    purple = (122, 71, 169)
    yellow = (215, 185, 148)
    white = (226, 210, 196)
    for pixels in image_list:
        if pixels[0] + pixels[1] + pixels[2] < 182:
            recolored.append(darkPurple)
        elif pixels[0] + pixels[1] + pixels[2] > 182 and pixels[0] + pixels[1] + pixels[2] < 364:
            recolored.append(purple)
        elif pixels[0] + pixels[1] + pixels[2] > 364 and pixels[0] + pixels[1] + pixels[2] < 546:
            recolored.append(yellow)
        else:
            recolored.append(white)
if color == "jungkook":
    darkBlue = (5, 0, 26)
    blue = (41, 72, 122)
    lightBlue = (179, 222, 234)
    white = (244, 252, 252)
    for pixels in image_list:
        if pixels[0] + pixels[1] + pixels[2] < 182:
            recolored.append(darkBlue)
        elif pixels[0] + pixels[1] + pixels[2] > 182 and pixels[0] + pixels[1] + pixels[2] < 364:
            recolored.append(blue)
        elif pixels[0] + pixels[1] + pixels[2] > 364 and pixels[0] + pixels[1] + pixels[2] < 546:
            recolored.append(lightBlue)
        else:
            recolored.append(white)
if color == "murica":
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)
    for pixels in image_list:
        if pixels[0] + pixels[1] + pixels[2] < 182:
            recolored.append(darkBlue)
        elif pixels[0] + pixels[1] + pixels[2] > 182 and pixels[0] + pixels[1] + pixels[2] < 364:
            recolored.append(red)
        elif pixels[0] + pixels[1] + pixels[2] > 364 and pixels[0] + pixels[1] + pixels[2] < 546:
            recolored.append(lightBlue)
        else:
            recolored.append(yellow)

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
name = input()
new_image.save("recolored/"+name+".jpg", "jpeg")
