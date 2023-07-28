
from tkinter import *
import pyttsx3
def fun5():
    t1.delete("0.0", END)
    engine = pyttsx3.init()
    speaker=str(e1.get())
    engine.say(speaker)
    engine.runAndWait()
    t1.insert("0.0",speaker)

y=Tk()
y.title("Text To Speech")
y.geometry("700x700")
y.configure(bg="lightpink")

l1=Label(y,text="Text To Speech",bg="red",font=("Times",35),borderwidth=40)
l1.pack(pady=14)


l2=Label(y,text="Type What U want to speak :",font=("Times",30),bg="red")
l2.pack(pady=15)


e1=Entry(y,bd=10,width=21,bg="yellow",fg="red",font=("Times",25))
e1.pack(pady=20)


b1=Button(y,text="Speak",bd=10,font=("Times",30),command=fun5)
b1.pack(pady=10)


t1=Text(height=10,width=40,font=("Times",25),bg="white",fg="red")
t1.pack()

y.mainloop()
