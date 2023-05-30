# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

root= Tk()
root.title("shapes_canvas")
root.geometry("900x900")

canvas = Canvas(root, width=990, height=490, bg="white", highlightbackground="gray" )
canvas.pack()

label= Label(root, text="choose color")
label.place(relx=0.6, rely=0.9, anchor=CENTER)

fillcolor=["blue", "red", "green", "yellow", "orange"]
color_dropdown= ttk.Combobox(root, state="readonly", values=fillcolor, width=10)
color_dropdown.place(relx=0.8, rely=0.9, anchor=CENTER)

startx= Label(root, text="startx")
startx.place(relx=0.1, rely=0.85, anchor=CENTER)

coord_value= [10,50,100,200,300,400,500,600,800,900]
startx_point= ttk.Combobox(root, state="readonly", values=coord_value, width=10)
startx_point.place(relx=0.2, rely=0.85, anchor=CENTER)

starty= Label(root, text="starty")
starty.place(relx=0.3, rely=0.85, anchor=CENTER)

starty_point= ttk.Combobox(root, state="readonly", values=coord_value, width=10)
starty_point.place(relx=0.4, rely=0.85, anchor=CENTER)

endx= Label(root, text="endx")
endx.place(relx=0.5, rely=0.85, anchor=CENTER)

endx_point= ttk.Combobox(root, state="readonly", values=coord_value, width=10)
endx_point.place(relx=0.6, rely=0.85, anchor=CENTER)

endy= Label(root, text="endy")
endy.place(relx=0.7, rely=0.85, anchor=CENTER)

endy_point= ttk.Combobox(root, state="readonly", values=coord_value, width=10)
endy_point.place(relx=0.8, rely=0.85, anchor=CENTER)

def circle(event):
    oldx= startx_point.get()
    oldy= starty_point.get()
    newx= endx_point.get()
    newy= endx_point.get()
    keypress='c'
    draw(keypress, oldx, oldy, newx, newy)
    
def rectangle(event):
    oldx= startx_point.get()
    oldy= starty_point.get()
    newx= endx_point.get()
    newy= endx_point.get()
    keypress='r'
    draw(keypress, oldx, oldy, newx, newy)
    
def line(event):
    oldx= startx_point.get()
    oldy= starty_point.get()
    newx= endx_point.get()
    newy= endx_point.get()
    keypress='l'
    draw(keypress, oldx, oldy, newx, newy)
    
def draw(keypress, oldx, oldy, newx, newy):
    color= color_dropdown.get()
    if (keypress=="c"):
        canvas.create_oval(oldx, oldy, newx, newy, width=3, fill=color)
    if(keypress=="r"):
        canvas.create_rectangle(oldx, oldy, newx, newy, width=3, fill=color)
    if( keypress=="l"):
        canvas.create_line(oldx, oldy, newx, newy, width=3, fill=color)
        
root.bind("<c>", circle)
root.bind("<r>", rectangle)
root.bind("<l>", line)
    
root.mainloop()