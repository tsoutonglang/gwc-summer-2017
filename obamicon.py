from PIL import Image

# obama patriotic colors
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)
# #jin wings colors
# gray = (60, 66, 85)
# turquoise = (21, 156, 152)
# pink = (251, 151, 163)
# red = (203, 66, 111)
#jimin wings colors
# darkPurple = (37, 29, 43)
# red = (164, 34, 49)
# lightPurple = (152, 144, 152)
# green = (205, 220, 210)
# #suga wings colors
# black = (41, 37, 44)
# gold = (128, 91, 75)
# yellow = (189, 169, 129)
# cream = (209, 231, 216)
#rap monster colors
# darkRed = (48, 3, 18)
# red = (168, 43, 94)
# shadow = (148, 205, 193)
# cream = (217, 245, 241)
#jungkook colors


# Import image.
my_image = Image.open("img/jungkook.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
for pixels in image_list:
    #print(pixels)
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
# new_image.save("obamiconJin.jpg", "jpeg")
new_image.save("recolored/obamiconJungkook.jpg", "jpeg")
