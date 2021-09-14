import tkinter as tk
from tkinter import Canvas
from tkinter import *
from typing import Any

myWindow=tk.Tk()
myWindow.title("Archery Board")
myWindow.geometry('700x700')
myWindow.resizable(False,False)

def arrow_coordinates(event):

    my_label_x['text']=str(event.x)+","+str(event.y)


def motion_coordinates(event):
    my_motion_x['text']=str(event.x)+","+str(event.y)

myCanvas=Canvas(myWindow,bd=5,bg='blue',width='320',height='320')
myCanvas.pack(padx=25,pady=25)

my_label_x=Label(relief="solid",font="Times 22 bold",bg="white",fg="black")
myCanvas.bind('<Button-1>',arrow_coordinates)
myCanvas.grid(row=0,column=0)
my_label_x.grid(row=1,column=0)

my_motion_x=Label(relief="solid",font="Times 22 bold",bg="white",fg="black")
myCanvas.bind('<Motion>',motion_coordinates)
myCanvas.grid(row=0,column=0)
my_motion_x.grid(row=2,column=0)

def Board(myCanvas):    
    x = 10
    y = 440
    Colour = ["white","white",'black','black',"blue","blue","red","red","yellow","yellow","yellow"]    
    for n in range (10):        
        myCanvas.create_oval(x,x,y,y,fill = Colour[n])        
        x+=20
        y-=20     
    myCanvas.create_oval(70,70,380,380,width=1,outline = "white")
    myCanvas.create_oval(210,210,240,240,fill='yellow',dash = (1,3))
    myCanvas.create_line(220,225,230,225,width=1)
    myCanvas.create_line(225,220,225,230,width=1)
        
def Numbers(myCanvas):
    x = 250
    for n in range (10,0,-1):   
        myCanvas.create_text(x,225,text = n,fill="grey")
        x+=20  

myCanvas=Canvas(myWindow,bd=5,bg='grey',width = 450 ,height = 450)
myCanvas.pack(padx=25,pady=25)
Board(myCanvas)
Numbers(myCanvas)

myWindow.mainloop()