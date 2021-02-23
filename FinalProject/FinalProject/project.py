import sys
import tkinter
import time
import random
import math
import numpy as np
from PIL import ImageTk
from PIL import Image
from simpleimage import SimpleImage
from tkinter import messagebox as mb

CANVAS_WIDTH = 700
CANVAS_HEIGHT = 700

#SQUARE_SIZE = 80

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'May the Force be with you!')
    #button = make_button()
    #print('Hello, world')

    image = ImageTk.PhotoImage(Image.open("images/yoda.png"))
    canvas.create_image(0, 300, anchor="nw", image=image)

    """
    parent = tkinter.Tk()
    parent.overrideredirect(1)
    parent.iconbitmap("PythonIcon.ico")
    parent.withdraw()
    """
    #button.mainloop()
    canvas.mainloop()


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

#def disp_message():
    #print("May the Force be with you!")

#def make_button():
    #master = tkinter.Tk()
    #button = tkinter.Button(master, text='Learn something, you shall!', command=disp_message)
    #button.pack()
    #return button


if __name__ == '__main__':
    main()