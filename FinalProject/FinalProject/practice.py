import sys
import tkinter
import time
import random
import math
import numpy as np
from PIL import Image
from PIL import ImageTk
#from PIL import Image as PilImage
#from tkinter import *
from simpleimage import SimpleImage
from tkinter import messagebox as mb

CANVAS_WIDTH = 700
CANVAS_HEIGHT = 700

#SQUARE_SIZE = 80

def main():

    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'May the Force be with you!')
    print('Hello, world')

    image = ImageTk.PhotoImage(Image.open("images/yoda.png"))
    canvas.create_image(0, 300, anchor="nw", image=image)

    canvas.create_text(0, 150, anchor='w', font='Courier 40', text="Learn about Covid-19,\n      you shall!")
    canvas.create_image(0, 300, anchor="", image=image)

    canvas.mainloop()

def closewindow():
    print("Learn about covid, you shall!")


def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

def disp_message():
    print("May the Force be with you!")




if __name__ == '__main__':
    main()