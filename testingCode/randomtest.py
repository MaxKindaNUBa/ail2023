from tkinter import Tk, PhotoImage, Listbox,messagebox
from tkinter.constants import *
from ttkthemes import ThemedStyle
from tkinter.ttk import Frame, Label, Entry, Button, Separator, Combobox, Scrollbar
from testHandler import Test
from sqlConnectors import session_info, get_classes, getStudentStats, get_tests, get_student_list, get_code,addExam,add_student
from reportCard import open_reportCard

class StudentAdd(Tk):
    def __init__(self,exam):
        super(StudentAdd, self).__init__()
        self.title("Adding student's marks to an exam")
        self.geometry("600x400")
        self.style = ThemedStyle()
        self.style.theme_use("breeze")
        self.exam = exam
        self.titleL = Label(self,text="Add a student's marks into exam",font=("Merriweather",20),borderwidth=3,relief=RIDGE)
        self.rollL = Label(self,text="Roll No:",font=("Merriweather",20))

        self.phyL = Label(self,text="Physics marks :",font=("Merriweather",20))
        self.chemL = Label(self,text="Chemistry marks:",font=("Merriweather",20))
        self.mathL = Label(self,text="Maths marks: ",font=("Merriweather",20))
        self.engL = Label(self,text="English marks: ",font=("Merriweather",20))
        self.coreL = Label(self,text="Csc/Eg/Bio marks: ",font=("Merriweather",20))

        self.addbutt = Button(self,text="Add student's marks ",width=20,command=self.add_std)
        self.rollT=Entry(self,font=("Merriweather",20),width=20)
        self.phyT=Entry(self,font=("Merriweather",20),width=20)
        self.chemT=Entry(self,font=("Merriweather",20),width=20)
        self.mathT=Entry(self,font=("Merriweather",20),width=20)
        self.engT=Entry(self,font=("Merriweather",20),width=20)
        self.coreT = Entry(self,font=("Merriweather",20),width=20)
        self.place_stuff()

    def add_std(self):
        try:
            add_student(self.exam,
                        self.rollT.grid(),
                        self.phyT.get(),
                        self.chemT.get(),
                        self.mathT.get(),
                        self.engT.get(),
                        self.coreT.get())
            messagebox.showinfo("Successfully added!", "Student has been \nsuccessfully added")
        except:
            messagebox.showerror("Student add unseccessfull","Student addition unsuccessfull\nPlease try again")




    def place_stuff(self):
        self.titleL.place(x=80,y=10)
        self.rollL.place(x=10,y=40)
        #self.rollT.grid(row=1,column=1)
        self.phyL.place(x=10,y=70)
        #self.phyT.grid(row=2,column=1)
        self.chemL.place(x=10,y=100)
        #self.chemT.grid(row=3,column=1)
        self.mathL.place(x=10,y=10)
        #self.mathT.grid(row=4,column=1)
        self.engL.place(x=10,y=10)
        #self.engT.grid(row=5,column=1)
        self.coreL.place(x=10,y=10)
        #self.coreT.grid(row=6,column=1)
        self.addbutt.place(x=10,y=10)

a = StudentAdd("Midterm1")
a.mainloop()
