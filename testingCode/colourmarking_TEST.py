from tkinter import *
from tkinter.ttk import Combobox
from sqlConnectors import get_classes
window=Tk()
window.geometry("500x500")
classSelect = Combobox(window,width=18,font=("Merriweather", 12))
classes = get_classes()
classSelect["values"] = classes
classSelect.current(0)

def printt():
    print(classSelect.get())
but = Button(window,text="Select Class",command=printt)

classSelect.pack()
but.pack()

window.mainloop()
'''
print(colorutils.Color(hex="#19ff19").rgb)
print(colorutils.Color((255,100,100)).hex)
'''