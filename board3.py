import tkinter as tk
from tkinter import *
from typing import Any

x=0
myWindow=tk.Tk()
myWindow.title("Draw Line")
myWindow.geometry('1750x1000')
myWindow.resizable(True,True)

myCanvas = Canvas(myWindow,bd=5,bg='grey',width=1675,height=925)
myCanvas.pack(padx=25,pady=25)

def arrow_coordinates(event):

    my_label_x['text']=str(event.x)+","+str(event.y)


def motion_coordinates(event):
    my_motion_x['text']=str(event.x)+","+str(event.y)

my_label_x=Label(relief="solid",font="Times 22 bold",bg="white",fg="black")
myCanvas.bind('<Button-1>',arrow_coordinates)
my_label_x.place(x=600,y=50,height=50,width=125)

my_motion_x=Label(relief="solid",font="Times 22 bold",bg="white",fg="black")
myCanvas.bind('<Motion>',motion_coordinates)
my_motion_x.place(x=720,y=50,height=50,width=125)

def Board(myCanvas):    
    x1 = 1150
    y1 = 200
    x2 = 1370
    y2 = 500
    Colour = ["white","white",'black','black',"blue","blue","red","red","yellow","yellow","yellow"]    
    for n in range (10):        
        myCanvas.create_oval(x1,y1,x2,y2,fill = Colour[n])        
        x1+=10
        y1+=10
        x2-=10
        y2-=10
    myCanvas.create_oval(1180,230,1340,470,width=1,outline = "white")
    myCanvas.create_oval(1250,300,1270,400,fill='yellow',dash = (1,3))
    myCanvas.create_line(1255,350,1265,350,width=1)
    myCanvas.create_line(1260,345,1260,355,width=1)

def Numbers(myCanvas):
    x = 1275
    for n in range (10,0,-1):   
        myCanvas.create_text(x,350,text = n,fill="orange",font = ("times",9))
        x+=10 

Board(myCanvas)
Numbers(myCanvas)
myWindow.mainloop()
myCanvas.create_text()