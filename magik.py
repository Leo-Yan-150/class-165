from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root=Tk()
root.title("Planets for nerds")
root.geometry("500x500")
root.configure(background="lightblue")

mer = ImageTk.PhotoImage(Image.open("mercury.jpg"))
ven = ImageTk.PhotoImage(Image.open("venus.jpg"))
ear = ImageTk.PhotoImage(Image.open("earth.jpg"))

planet = Label(root, text="Planet: ", bg="lightblue")
name = Label(root,font=("courier",18,"bold"),bg="lightblue")
imag = Label(root, bg="gold2", highlightthickness = 5, borderwidth=2,relief=SOLID)
radius=Label(root,font=("castellar"), bg="lightblue")
info = Label(root,font=("courier",10,"bold"),bg="lightblue",wraplength=500)

planets = ["Mercury","Venus","Earth"]
selectedvar = StringVar()
dropdown = ttk.Combobox(root, values = planets, textvariable=selectedvar)

def plonet():
    planetss = selectedvar.get()
    if planetss == "Mercury":
        planet['text'] = "Mercury"
        imag['image'] = mer
        radius['text']="Gravity : 3.7 m/s² \n Radius : 2,439.7 km"
        info['text'] = "Mercury is the smallest planet in our solar system. It's just a little bigger than Earth's moon"
    elif planetss == "Venus":
        planet['text'] = "Venus"
        imag['image'] = ven
        radius['text']="Gravity : 8.87 m/s² \n Radius : 6,051.8 km"
        info['text'] = "Venus is the brightest object in the sky after the Sun and the Moon, and sometimes looks like a bright star in the morning or evening sky."
    elif planetss == "Earth":
        planet['text'] = "Earth"
        imag['image'] = ear
        radius['text']="Gravity : 9.807 m/s² \n Radius : 6,371 km"
        info['text'] = "Earth is the only place in the known universe confirmed to host life and it's the only one known for sure to have liquid water on its surface."
    else:
        info["text"] = "Please do not type stuff in the drop down or leave it blank, it is really not good for....yes."

dropdown.place(relx=0.5,rely=0.1, anchor=CENTER)

button = Button(root,text="Show Planet Info", command=plonet)
button.place(relx=0.5,rely=0.18,anchor=CENTER)

planet.place(relx=0.2,rely=0.1,anchor=CENTER)
name.place(relx=0.5,rely=0.25,anchor=CENTER)
imag.place(relx=0.5,rely=0.5,anchor=CENTER)
radius.place(relx=0.5,rely=0.8,anchor=CENTER)
info.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()