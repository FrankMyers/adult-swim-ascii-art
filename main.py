#import the required image processing and graphics libraries
from PIL import Image as image
import pygame

#initilize pygame :/
pygame.init()

#define the size of the pixelated image later on
width = 120
height = 100

#define font for pygame, and color of font
font = pygame.font.SysFont("Arial", 7)
color = (255,255,255)

#define variable that will hold the ascii art
string = ""

#open this image and convert it to greyscale
img = image.open("as.png", "r").convert("LA")

#resize the image to make it pixelated
img = img.resize((width,height),resample=image.BILINEAR)

temp = -1

for pixel in img.getdata():
    temp += 1
    #if the pixel we are on is a factor of the width create a new row
    if temp % width == 0:
        string += " \n"
    #add a white pixel if the pixel is white
    if pixel == (255,255):
        string += "■"
    #add a black pixel if the pixel is black
    else:
        string += "   "

#print the results
print(string)

#split our sring into rows in which we can display later
string = string.split('\n')

#create our window surface
root = pygame.display.set_mode((width*7, height*7))

#a temp variable to store the y postitions of the rows in the for loop
temp = -1

#render each row and display them on "root" aka our window
for item in string:
    #iterate the y values
    temp += 1
    #render the text for displaying
    text = font.render(item, 1, color)
    #display the text to the window
    root.blit(text, (root.get_width()/2-text.get_width()/2, temp*7))

#the main loop for the window to display the art
while 1:
    #if the x button is pressed close the window and end the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #update the screen. i dont want to add another comment about the number of lines becase it would increase the number of lines so a double comment will have to do. nice.
    pygame.display.update()