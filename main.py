from tkinter import *
from tkinter import messagebox
import random

FONT =("Arial", 8, "bold")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generate():
    my_password = []
    string_password = ""
    for item in range(4):
        letter_input = random.choice(letters)
        my_password.append(letter_input)
        number_input = random.choice(numbers)
        my_password.append(number_input)
        symbol_input = random.choice(symbols)
        my_password.append(symbol_input)
    random.shuffle(my_password)
    for char in my_password:
        string_password += char
    print(string_password)
    space_password.insert(0, string_password)







# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():


    if len(website_entry.get()) == 0 or len(space_password.get())==0 or len(user_entry.get())==0:
        messagebox.showinfo(title="Hey yooo", message="Don't forget to fill all blanks !!!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are all details: \nEmail:{user_entry.get()}\nPassword:{space_password.get()}")
        if is_ok:
            file_name = open("data.txt", "a")
            file_name.write(f"{website_entry.get()} | {user_entry.get()} | {space_password.get()}"+"\n")
            file_name.close()
            website_entry.delete(0, END)
            space_password.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50,)

# Canvas
my_canvas = Canvas(width=200, height= 200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")

# Image
my_canvas.create_image(90, 100, image= logo_img)
my_canvas.grid(row=0, column=1)

name_website = Label(text="Website: ")
name_website.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.get()

name_user = Label(text="Email/Username:")
name_user.grid(row=2, column=0)

user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
user_entry.insert(0, user_entry.get())

name_password = Label(text="Password:")
name_password.grid(row=3, column=0)

space_password = Entry(width=21)
space_password.grid(row=3, column=1, sticky="EW")

gen_button = Button(text="Generate", highlightthickness=0, command=password_generate,)
gen_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")





window.mainloop()