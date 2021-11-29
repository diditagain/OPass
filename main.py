from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip

#Password Generator#

def generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]

    password_list += [choice(symbols) for _ in range(randint(2,4))]

    password_list += [choice(numbers) for _ in range(randint(2,4))]


    shuffle(password_list)


    password = "".join(password_list)

    print(f"Your password is: {password}")

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)



#Save Password

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    login_data = {website: {
        "email": email,
        "password": password
    }}
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        warning = messagebox.showerror(title="Error", message="Please fill all required fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered \n Email: {email} \n Password: {password}")

    if is_ok is True:
        try:
            with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(login_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(login_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)

#UI

window = Tk()
window.title("OPass Password Manager")
window.config(padx=60, pady=60)

canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)

main_frame = ttk.Frame()

#Website Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

#Email Label
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

#Password Label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Website Entry
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

#Email Entry
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "")
#Password Entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Generate Button

generate_button = Button(text="Generate Password", width=15, command=generator)
generate_button.grid(row=3, column=2)

#Add Button

add_button = Button(text="Add", width=37, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()