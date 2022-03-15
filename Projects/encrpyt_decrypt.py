from tkinter import messagebox, simpledialog, Tk

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letter = []
    for i in range(0, len(message)):
        if is_even(i):
            even_letter.append(message[i])
    return even_letter


def get_odd_letters(message):
    odd_letter = []
    for i in range(0, len(message)):
        if not is_even(i):
            odd_letter.append(message[i])
    return odd_letter

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for i in range(0,int(len(message)/2)):
        letter_list.append(odd_letters[i])
        letter_list.append(even_letters[i])
    new_message = ''.join(letter_list)
    return new_message

def get_task():
    task = simpledialog.askstring("Task", "Encrypt or Decrypt?")
    return task

def get_message():
    message = simpledialog.askstring("Message", "Enter message:")
    return message

root = Tk()
while True: 
    task = get_task()
    if task == 'Encrypt':
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo("Cipher text of the secret message is: ", encrypted)

    elif task == 'Decrypt':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo("Plain message is: ", decrypted)

    else:
        break

root.mainloop()