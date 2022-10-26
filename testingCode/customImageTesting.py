import tkinter as tk
from PIL import Image,ImageTk
from urllib.request import urlopen

root=tk.Tk()
imageurl="https://picsum.photos/id/237/200/300"

u=urlopen(imageurl)
raw_data=u.read()
u.close()

photo=ImageTk.PhotoImage(data=raw_data)
label=tk.Label(image=photo)
label.pack()

root.mainloop()
