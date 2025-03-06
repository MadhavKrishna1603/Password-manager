from tkinter import *
from tkinter import messagebox
import random
import  pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters =[random.choice(letters) for _ in range(nr_letters)]
    password_symbols =[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers =[random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0,END)
    pass_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="oops!",message="Please dont leave any feild empty")
    else:
        is_okay = messagebox.askokcancel(title=website,message=f"These are your details \nEmail : {email}\npassword: {password}\nAre you ok to save ?")

        if is_okay:
            with open("data.txt",mode="a") as file:
                file.write(f"{website} | {email} | {password} \n")
            web_entry.delete(0,END)
            pass_entry.delete(0,END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200,width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0,sticky=EW)

label_website = Label(text="Website:",highlightthickness=0)
label_website.grid(row=1,column=0,sticky=EW)

label_email = Label(text= "Email/Username:",highlightthickness=0)
label_email.grid(row=2,column=0,sticky=EW)

label_password = Label(text="Password:",highlightthickness=0)
label_password.grid(row=3,column=0,sticky=EW)

website_user_entry = web_entry = Entry(width=35,highlightthickness=0)
web_entry.grid(row=1,column=1,columnspan=2,sticky=EW)
web_entry.focus()

email_user_entry = email_entry = Entry(width=35,highlightthickness=0)
email_entry.grid(row=2,column=1,columnspan=2,sticky=EW)

pass_user_entry = pass_entry = Entry(width=21,highlightthickness=0)
pass_entry.grid(row=3,column=1,sticky=EW)

gen_pass = Button(text="Generate Password",highlightthickness=0,command=generate_password)
gen_pass.grid(row=3,column=2,sticky=EW)

add = Button(width=36,text="Add",highlightthickness=0,command = save)
add.grid(row=4,column=1,columnspan=2,sticky=EW)






window.mainloop()
