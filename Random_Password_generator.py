from tkinter import *
#import string
#print(dir(string))
import random


##########     Password Generator     ##########

def password_generator():
    password_show.delete(0, END)
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower="abcdefghijklmnopqrstuvwxyz"
    numbers="1234567890"
    symbols="!@^&<>`~*$()?^"
    length=int(char_input.get())
    passwords="".join(random.sample(upper+lower+numbers+symbols,length))
    password_show.insert(0, passwords)

    


############## User Interface      ###############
window =Tk()
window.title("Passwotrd Generator")
window.config(padx=50, pady=50, bg="#383e56")


label_title=Label(text="Random Password Generator",borderwidth=10, relief="raised", bg="purple", fg="#c5d7bd", font=("Arial", 35, "bold"))
label_title.pack()



label_before_input = Label(text="I want a password with",bg="#383e56",fg="#c5d7bd",font=("Arial", 15, "bold"))
label_before_input.pack()





char_input = Entry(bg="white")
char_input.pack(pady=15)



label_after_input = Label(text="characters.", bg="#383e56", fg="#c5d7bd",font=("Arial", 15, "bold",))
label_after_input.pack()
#char_input.insert(0, "15")



########    Button    ########
generate_password_button = Button(text="Generate Password",bg="#fb743e",font=("Arial",15,"bold"),height=3,width=30,command=password_generator)
generate_password_button.pack()






################     password show    ##############
password_show = Entry(bg="yellow",font=("Arial", 15, "bold"), width=30)
password_show.pack(pady=30)




#close window Tk()
window.mainloop()

