from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip

#Search website
def search_website():
    site = website_entry.get()
    try:
        with open("data.json", "r") as search_data:
            websites = json.load(search_data)
    except FileNotFoundError:
        messagebox.showerror(title="No Data File", text="You haven't saved any passwords yet.")
    else:
        if site in websites:
            login_info = websites[site]
            email = login_info["email"]
            password = login_info["password"]
            prompt = messagebox.showinfo(title="Login Info", message=f"For {site}, \n Email: {email} \n Password: {password}")
        else:
            message = messagebox.Message("Login info about this website has not been found.")


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

    def write_data(input_data):
            with open("data.json", "w") as data_file:
                json.dump(input_data, data_file, indent=4)

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        warning = messagebox.showerror(title="Error", message="Please fill all required fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered \n Email: {email} \n Password: {password}")

    if is_ok is True:
        try:
            with open("data.json", "r") as data_file:
                    data = json.load(data_file)
        except FileNotFoundError:
            write_data(login_data)
        else:
            data.update(login_data)
            write_data(data)
        finally:
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
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

#Email Entry
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "")
#Password Entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Generate Button

generate_button = Button(text="Generate Password", width=13, command=generator)
generate_button.grid(row=3, column=2)

#Search Button

search_button = Button(text="Search", width=13, command=search_website)
search_button.grid(row=1, column=2)

#Add Button

add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()