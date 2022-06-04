from tkinter import *
import random
container = Tk()
container.geometry("1000x500")


def packButtons(lenght,width):
    l=0;b=0
    condition = 1
    while condition:
        if (l+80) <= lenght and (b+80) <= width:
            Button(container, text=f"Button\n{condition}",bg=f"#{hex(random.randint(1118481, 16777215))[2:]}").place(x=l,y=b,width=80,height=80)
            l+=80
            condition+=1
        elif (l+80) >= lenght and (b+80) <= width:
            if b+160 <=width:
                l = 0
                b += 80
                condition +=1
                Button(container, text=f"Button\n{condition}", bg=f"#{hex(random.randint(1118481, 16777215))[2:]}").place(x=l, y=b,
                                                                                                              width=80,
                                                                                                              height=80)
            else:
                print(f"Placed {condition-1} buttons !")
                condition=0




packButtons(1000,500)
container.mainloop()
