from tkinter import Toplevel, Text, Button,Label,Tk,messagebox
import student_scope
from tkinter.constants import *
from sqlConnectors import check_password,register_teacher


class RegisterWindow(Tk):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.title("Register a new teacher")
        self.geometry("590x260")
        self.titleL= Label(self,text="Add a new teacher!",font=("Merriweather",20),borderwidth=3,relief=RIDGE)

        self.useridL= Label(self,text="User ID : ",font=("Merriweather",20))
        self.passL = Label(self,text="Password:",font=("Merriweather",20))
        self.mainL =Label(self,text="Mail ID:",font=("Merriweather",20))
        self.classL =Label(self,text="Class : ",font=("Merriweather",20))
        self.uniqueL = Label(self,text="Unique ID:",font=("Merriweather",20))

        self.userT =Text(self,width=30,height=1,font=("Merriweather",20))
        self.passT=Text(self,width=30,height=1,font=("Merriweather",20))
        self.mainT=Text(self,width=30,height=1,font=("Merriweather",20))
        self.classT=Text(self,width=30,height=1,font=("Merriweather",20))
        self.uniqueT=Text(self,width=30,height=1,font=("Merriweather",20))
        self.registerbutt = Button(self,text="Register new teacher",
                                   command=lambda: self.register_user(self.userT.get(),self.passT.get(0.0,END),self.mainT.get(0.0,END),self.classT.get(0.0,END),self.uniqueT.get(0.0,END)))

        self.place_stuff()
    def register_user(self,user,pas,mail,clas,unid):
        register_teacher(user,pas,mail,clas,unid)
        messagebox.showinfo("Success!",f"A new teacher {user} has been registered!")
        self.destroy()



    def place_stuff(self):
        self.titleL.grid(row=0,column=0,columnspan=2)

        self.useridL.grid(row=1,column=0)
        self.passL.grid(row=2,column=0)
        self.mainL.grid(row=3,column=0)
        self.classL.grid(row=4,column=0)
        self.uniqueL.grid(row=5,column=0)

        self.userT.grid(row=1, column=1)
        self.passT.grid(row=2, column=1)
        self.mainT.grid(row=3, column=1)
        self.classT.grid(row=4, column=1)
        self.uniqueT.grid(row=5, column=1)
        self.registerbutt.grid(row=6,column=0,columnspan=2,sticky=NSEW)


RegisterWindow().mainloop()
