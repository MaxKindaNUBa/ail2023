from tkinter import *
import colorutils

container = Tk()
container.geometry("800x800")
def rgb_to_hex(percent):
    r,g,b=0,0,0
    if percent>=50:
        g=255
        r=b=4.5*(100-percent)
    else:
        r=255
        g=b=4.5*percent

    return colorutils.Color((r,g,b)).hex

def packButtons(lenght,width):
    l=0;b=0
    condition = 1
    while condition:
        if (l+80) <= lenght and (b+80) <= width:
            Button(container, text=f"{condition}\nMarks",bg=rgb_to_hex(condition)).place(x=l,y=b,width=80,height=80)
            l += 80
            condition += 1
        elif (l+80) >= lenght and (b+80) <= width:
            if b+160 <=width:
                l = 0
                b += 80
                Button(container, text=f"{condition}\nMarks",bg=rgb_to_hex(condition)).place(x=l, y=b,width=80,height=80)

            else:
                print(f"Placed {condition-1} buttons !")
                condition=0




packButtons(800,800)
container.mainloop()
