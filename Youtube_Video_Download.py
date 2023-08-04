
from tkinter import *
from pytube import YouTube
print(dir(YouTube))



#open
root = Tk()
root.geometry('500x300')

root.title("Youtube Video downloader")




def Downloader():     
    url = YouTube(str(yut_input.get()))
    video = url.streams.first()
    video.download()
    yut_input.insert(0,url)  
   


label_title=Label(text="Youtube Video Downloader",borderwidth=6,relief=SUNKEN, bg="skyblue", font=("Arial", 20, "bold"))
label_title.pack(pady=30)



L1=Label(root, text = 'Paste Link Here:', font = 'arial 15 bold')
L1.pack()


yut_input=Entry(root,font='arial 15')
yut_input.pack(pady=10)




btn=Button(root,text='Download',bg='pink',font=("Arial", 15, "bold"),command=Downloader)
btn.pack()



#close
root.mainloop()








