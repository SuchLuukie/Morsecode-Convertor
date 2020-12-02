from alphabet import Alphabet
from visual import Visual
from tkinter import *
import winsound
from time import sleep

"""Options for screen size and where text starts to draw"""
canvasWidth = 1200
canvasHeight = 700

x = 40
y = 200

objectArray = []

"""Create canvas"""
root = Tk()
canvas = Canvas(root, width=canvasWidth, height=canvasHeight, bg="white")
canvas.pack()

#Declaring imports
alphabet = Alphabet()
visual = Visual(root, canvas)

def convertor():
	clearCanvas()
	global x, y, objectArray

	"""Retrieve all information from sliders and textbox"""
	hertz = slider1.get()
	letterSpacing = slider2.get()
	wordSpacing = slider3.get()
	speed = slider4.get()

	#Convert the input to a more usable datatype
	string = retrieve_input().lower()
	inputString = list(string)

	#Declare outputArray
	outputArray = []



	#Loop to create the visual dit/dahs
	for index in inputString:
		letter = alphabet.convert(index)

		#If a space or the max distance the string can take doesnt fit on the screen it skips to the next row
		if x + (visual.barSizeX * len(inputString)) >= canvasWidth or x + visual.wordGap >= canvasWidth:
			y += 40
			x = 40

		for l in letter:
			if l == ".":
				#Add object to object array and create the object
				objectArray.append(visual.createDit([x, y]))
				x += (visual.ellipseSize + visual.letterGap)
				
			elif l == "-":
				#Add object to object array and create the object
				objectArray.append(visual.createDah([x, y]))
				x += (visual.barSizeX + visual.letterGap)

			elif l == " ":
				x += visual.wordGap

		x += visual.barSizeX


	#Loop for sound for dit/dahs
	for index2 in inputString:
		letter2 = alphabet.convert(index2)

		for k in letter2:
			if k == ".":
				winsound.Beep(hertz, 100)
				
			elif k == "-":
				winsound.Beep(hertz, 330)

			elif k == " ":
				sleep(wordSpacing)
			
			sleep(speed)

		sleep(letterSpacing)


#Retrieve input from the textbox and return
def retrieve_input():
    inputValue = textBox.get("1.0","end-1c")
    return inputValue


#Clear the canvas of all object and reset x,y
def clearCanvas():
	global objectArray, x, y
	for item in objectArray:
		canvas.delete(item)

	x = 40
	y = 200

"""Button and textbox"""
textBox = Text(root, height=8, width=25)
textBox.place(x = 10, y = 10)

button = Button(root, height=1, width=10, text="Convert", command=lambda: convertor())
button.place(x = 10, y = 150)


"""All the sliders."""
slider1 = Scale(root, from_=0, to=2000, orient=HORIZONTAL, resolution=50, length=150)
slider1.place(x = 340, y = 10)
label1 = Label(root, text="Toonhoogte")
label1.place(x = 250, y = 28)

slider2 = Scale(root, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, length=150)
slider2.place(x = 340, y = 50)
label2 = Label(root, text="LetterSpaties")
label2.place(x = 250, y = 68)

slider3 = Scale(root, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, length=150)
slider3.place(x = 340, y = 90)
label3 = Label(root, text="WoordenSpaties")
label3.place(x = 250, y = 108)

slider4 = Scale(root, from_=0, to=1, orient=HORIZONTAL, resolution=0.01, length=150)
slider4.place(x = 340, y = 130)
label4 = Label(root, text="Snelheid")
label4.place(x = 250, y = 148)

#Screen geometry and the mainloop for visuals. (tkinter)
root.geometry("1200x700")
mainloop()