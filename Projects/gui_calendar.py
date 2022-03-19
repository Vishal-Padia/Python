from tkinter import *
import calendar

def showCalendar():
    win = Tk()
    win.config(bg='grey')
    win.title("Calendar")
    win.geometry("550x600")
    year = int(year_field.get())
    win_content = calendar.calendar(year)
    calYear = Label(win,text=win_content, font = "Consolas 10 bold")
    calYear.grid(row=5, column=1, padx=20)
    win.mainloop()

if __name__ == '__main__':
    win = Tk()
    win.config(bg='grey')
    win.title("Calendar")
    win.geometry("250x140")
    cal = Label(win, text="Calendar", bg='grey', font=("times", 28 , "bold"))
    year = Label(win, text="Enter Year", bg='dark grey')
    year_field = Entry(win)
    button = Button(win, text='Show Calendar',fg='Black', bg='Blue', command=showCalendar)
    
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    win.mainloop()