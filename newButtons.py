from tkinter import Tk, PhotoImage, Listbox, messagebox
from tkinter.constants import *
from ttkthemes import ThemedStyle
from tkinter.ttk import Frame, Label, Entry, Button, Separator, Combobox, Scrollbar
from testHandler import Test
from sqlConnectors import session_info, get_classes, getStudentStats, get_tests, get_student_list, get_code, addExam, \
    add_student, get_info, modify_marks, delete_marks
from reportCard import open_reportCard


class ModifyMarks(Tk):
    def __init__(self):
        super(ModifyMarks, self).__init__()

        self.style = ThemedStyle()
        self.style.theme_use("breeze")
        self.title("Modify existing student's marks")
        self.geometry("600x400")

        self.titleL = Label(self, text="Modify existing student's marks", font=("Merriweather", 30), borderwidth=3,
                            relief=RIDGE)

        self.rolle = Entry(self, font=("Merriweather", 20), width=20)

        self.phyL = Label(self, text="Physics marks :", font=("Merriweather", 20))
        self.chemL = Label(self, text="Chemistry marks :", font=("Merriweather", 20))
        self.mathL = Label(self, text="Maths marks :", font=("Merriweather", 20))
        self.engL = Label(self, text="English marks :", font=("Merriweather", 20))
        self.coreL = Label(self, text="Csc/Eg/Bio marks :", font=("Merriweather", 20))

        a = get_tests()
        self.examsList = Combobox(self, values=a, state="readonly", width=20, font=("merriweather", 18))
        self.examsList.bind("<<ComboboxSelected>>", self.exam_is)
        self.examsList.current(0)
        self.exam = get_code(a[0])

        self.phye = Entry(self, font=("Merriweather", 20), width=20)
        self.cheme = Entry(self, font=("Merriweather", 20), width=20)
        self.mathe = Entry(self, font=("Merriweather", 20), width=20)
        self.enge = Entry(self, font=("Merriweather", 20), width=20)
        self.coree = Entry(self, font=("Merriweather", 20), width=20)

        self.modifyb = Button(self, text="Modify marks", command=self.change_marks)
        self.selectb = Button(self, text="Select roll", command=self.get_info)
        self.place_stuff()

    def exam_is(self, a):
        self.exam = get_code(self.examsList.get())

    def place_stuff(self):
        self.titleL.grid(row=0, column=0, padx=0.1, pady=0.1, columnspan=2)
        self.rolle.grid(row=1, column=0)
        self.selectb.grid(row=1, column=1, sticky=NSEW)

        self.phyL.grid(row=2, column=0)
        self.chemL.grid(row=3, column=0)
        self.mathL.grid(row=4, column=0)
        self.engL.grid(row=5, column=0)
        self.coreL.grid(row=6, column=0)

        self.phye.grid(row=2, column=1)
        self.cheme.grid(row=3, column=1)
        self.mathe.grid(row=4, column=1)
        self.enge.grid(row=5, column=1)
        self.coree.grid(row=6, column=1)

        self.examsList.grid(row=7, column=0, sticky="NSEW")
        self.modifyb.grid(row=7, column=1, sticky="NSEW")

    def change_marks(self):
        try:
            modify_marks(self.exam, self.rolle.get(), self.phye.get(), self.cheme.get(), self.mathe.get(),
                         self.enge.get(), self.coree.get())
            messagebox.showinfo("Modified successully", "New marks have been updated successfully in the database")
        except:
            messagebox.showerror("Modify error", "New marks has not been updated please check for mistakes")

    def get_info(self):
        try:
            a = get_info(self.exam, self.rolle.get())

            self.phye.delete(0, END)
            self.cheme.delete(0, END)
            self.mathe.delete(0, END)
            self.enge.delete(0, END)
            self.coree.delete(0, END)

            self.phye.insert(0, a[1])
            self.cheme.insert(0, a[2])
            self.mathe.insert(0, a[3])
            self.enge.insert(0, a[4])
            self.coree.insert(0, a[5])
        except:
            messagebox.showerror("Invalid Roll number/exam",
                                 "Either the roll number is invalid or the chosen exam does not have the roll number")


class StudentAdd(Tk):
    def __init__(self):
        super(StudentAdd, self).__init__()
        self.title("Adding student's marks to an exam")
        self.geometry("600x300")

        self.style = ThemedStyle()
        self.style.theme_use("breeze")

        self.titleL = Label(self, text="Add a student's marks into exam", font=("Merriweather", 20), borderwidth=3,
                            relief=RIDGE)
        self.rollL = Label(self, text="Roll No:", font=("Merriweather", 20))

        self.phyL = Label(self, text="Physics marks :", font=("Merriweather", 20))
        self.chemL = Label(self, text="Chemistry marks:", font=("Merriweather", 20))
        self.mathL = Label(self, text="Maths marks: ", font=("Merriweather", 20))
        self.engL = Label(self, text="English marks: ", font=("Merriweather", 20))
        self.coreL = Label(self, text="Csc/Eg/Bio marks: ", font=("Merriweather", 20))
        a = get_tests()
        self.examsList = Combobox(self, values=a, state="readonly", width=20)
        self.examsList.bind("<<ComboboxSelected>>", self.exam_is)
        self.examsList.current(0)
        self.exam = get_code(a[0])

        self.addbutt = Button(self, text="Add student's marks ", width=20, command=self.add_std)
        self.rollT = Entry(self, font=("Merriweather", 20), width=20)
        self.phyT = Entry(self, font=("Merriweather", 20), width=20)
        self.chemT = Entry(self, font=("Merriweather", 20), width=20)
        self.mathT = Entry(self, font=("Merriweather", 20), width=20)
        self.engT = Entry(self, font=("Merriweather", 20), width=20)
        self.coreT = Entry(self, font=("Merriweather", 20), width=20)
        self.place_stuff()

    def add_std(self):
        try:
            add_student(self.exam,
                        self.rollT.get(),
                        self.phyT.get(),
                        self.chemT.get(),
                        self.mathT.get(),
                        self.engT.get(),
                        self.coreT.get())
            messagebox.showinfo("Successfully added!", "Student has been \nsuccessfully added")
        except:
            messagebox.showerror("Student add unseccessfull", "Student addition unsuccessfull\nPlease try again")

    def exam_is(self, eventobject):
        self.exam = get_code(self.examsList.get())

    def place_stuff(self):
        self.titleL.grid(row=0, column=0, columnspan=2)
        self.rollL.grid(row=1, column=0)
        self.rollT.grid(row=1, column=1)
        self.phyL.grid(row=2, column=0)
        self.phyT.grid(row=2, column=1)
        self.chemL.grid(row=3, column=0)
        self.chemT.grid(row=3, column=1)
        self.mathL.grid(row=4, column=0)
        self.mathT.grid(row=4, column=1)
        self.engL.grid(row=5, column=0)
        self.engT.grid(row=5, column=1)
        self.coreL.grid(row=6, column=0)
        self.coreT.grid(row=6, column=1)
        self.addbutt.grid(row=7, column=0, sticky="NSE")
        self.examsList.grid(row=7, column=1, sticky="NSW")


class StudentDelete(Tk):
    def __init__(self):
        super(StudentDelete, self).__init__()
        self.title("Delete student marks")
        self.geometry("600x150")

        self.titleL = Label(self, text="Delete student marks from exam", font=("Merriweather", 20), borderwidth=3,
                            relief=RIDGE)

        a = get_tests()
        self.examsList = Combobox(self, values=a, state="readonly", width=20, font=("merriweather", 20))
        self.examsList.bind("<<ComboboxSelected>>", self.exam_is)
        self.examsList.current(0)
        self.exam = get_code(a[0])

        self.rollL = Label(self, text="Roll No:", font=("Merriweather", 20))
        self.rollT = Entry(self, font=("Merriweather", 20), width=20)
        self.delbut = Button(self, text="Delete marks", command=self.deletee)
        self.place_stuff()

    def deletee(self):
        try:
            delete_marks(get_code(self.exam), self.rollT.get())
            messagebox.showinfo("Delete success", "Student marks has been deleted successfully")
        except Exception as e:
            print(e)
            messagebox.showerror("Delete error", "Student marks has not been deleted.Check for the proper roll number")

    def place_stuff(self):
        self.titleL.grid(row=0, column=0, columnspan=2)
        self.rollL.grid(row=1, column=0)
        self.rollT.grid(row=1, column=1)
        self.examsList.grid(row=2, column=0)
        self.delbut.grid(row=2, column=1, sticky="NSEW")

    def exam_is(self, a):
        self.exam = self.examsList.get()
