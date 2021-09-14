import tkinter as tk
from tkinter import *
from typing import Any


def arrow_coordinates(event):

    my_label_x['text']=str(event.x)+","+str(event.y)


def motion_coordinates(event):
    my_motion_x['text']=str(event.x)+","+str(event.y)

myWindow=tk.Tk()
myWindow.title("mouse")
myWindow.geometry('420x420')
myWindow.resizable(False,False)

myCanvas=Canvas(myWindow,bd=5,bg='blue',width='320',height='320')
myCanvas.pack(padx=25,pady=25)

my_label_x=Label(relief="solid",font="Times 22 bold",bg="white",fg="black")
myCanvas.bind('<Button-1>',arrow_coordinates)
myCanvas.place(x=0,y=0,height=320,width=320)
my_label_x.place(x=100,y=330,height=50,width=100)

my_motion_x=Label(relief="solid",font="Times 22 bold",bg="white",fg="black")
myCanvas.bind('<Motion>',motion_coordinates)
myCanvas.place(x=0,y=0,height=320,width=320)
my_motion_x.place(x=200,y=330,height=50,width=100)

myWindow.mainloop()