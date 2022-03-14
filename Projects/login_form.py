from tkinter import *
from functools import partial

def validateLogin(username, password):
    print("Username: " , username.get())
    print("Password: " , password.get())
    return

#Window
win = Tk()
win.geometry("500x250")
win.title("Login Form")

#username label and entry box
usernameLabel = Label(win, text="Username: ").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(win, textvariable=username).grid(row=0, column=1)

#password label and entry box
passwordLabel = Label(win, text="Password: ").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(win, textvariable=password, show="*").grid(row=1, column=1)


validateLogin = partial(validateLogin, username, password)

#Login button
loginButton = Button(win, text="Login", command=validateLogin).grid(row=4, column=0)

win.mainloop()