from tkinter import Label,Tk
import time

win = Tk()
win.title("Digital Clock")
win.geometry("420x150")
win.resizable(1,1)

font = ("Boulder", 69, 'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25

label = Label(win, font = font, bg = background, fg = foreground, borderwidth = border_width)
label.grid(row=0,column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text = time_live)
    label.after(200, digital_clock)

digital_clock()
win.mainloop()