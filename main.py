from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = "abcdefghifklmnopqrstuvwxyz!@#$%^&*()0123456789"
    letters_list = list(letters)
    password = ""
    for _ in range(0, 21):
        password += random.choice(letters_list)
    print(password)
    password_text.delete("1.0", END)
    password_text.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website_string = website_text.get("1.0", END).strip()
    email_string = email_text.get("1.0", END).strip()
    password_string = password_text.get("1.0", END).strip()
    print(website_string)
    if website_string == "" or email_string == "" or password_string == "":
        messagebox.showerror(title="Missing", message="Incomplete Form")
    else:
        is_ok = messagebox.askokcancel(title=website_string, message=f"These are the details: \n Website:"
                                                                     f" {website_string}\n Email/Login: "
                                                                     f"{email_string}\n Password: "
                                                                     f"{password_string}\n Ok to save? ")
        if is_ok:
            with open("password.txt", mode="a") as file:
                file.write(f"{website_string} | {email_string} | {password_string}\n")
            messagebox.showinfo(title="Success", message="Data Saved")
            password_text.delete("1.0", END)
            email_text.delete("1.0", END)
            website_text.delete("1.0", END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass")

window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
# canvas.config(padx=20, pady=20)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=1, column=2)

# Labels
website_label = Label(text="Website:")
# website_label.config(width=35 )
website_label.grid(row=2, column=1)

email_label = Label(text="Email/Username:")
# email_label.config(width=35 )
email_label.grid(row=3, column=1)

password_label = Label(text="Password:")
# email_label.config(width=35 )
password_label.grid(row=4, column=1)

# Text
website_text = Text(height=1, width=35, relief="solid", bd=1)
# Puts cursor in textbox.
# website_text.config()
# website_text.focus()
# Adds some text to begin with.
website_text.insert(END, "")
# Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
website_text.grid(row=2, column=2, columnspan=2)

email_text = Text(height=1, width=35, relief="solid", bd=1)
# Puts cursor in textbox.
# email_text.focus()
# Adds some text to begin with.
email_text.insert(END, "")
# Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
email_text.grid(row=3, column=2, columnspan=2)

password_text = Text(height=1, width=21, relief="solid", bd=1)
# Puts cursor in textbox.
# password_text.focus()
# Adds some text to begin with.
password_text.insert(END, "")
# Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
password_text.grid(row=4, column=2)

# Buttons
generate_button = Button(text="Generate Password", command=generate)
generate_button.config()
generate_button.grid(row=4, column=3)

add_button = Button(text="Add", width=36, command=add)
add_button.config()
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()
