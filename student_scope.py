from tkinter import Tk, PhotoImage, Listbox, Button,messagebox
from tkinter.constants import *
from ttkthemes import ThemedStyle
from tkinter.ttk import Frame, Label, Entry, Button, Separator, Combobox, Scrollbar
from testHandler import Test
from sqlConnectors import session_info, get_classes, getStudentStats, get_tests, get_student_list, get_code,addExam
from reportCard import open_reportCard

CLASS_IN_USE = ''


def add_an_exam():
    ExamAdder().mainloop()

class ExamAdder(Tk):
    def __init__(self):
        super(ExamAdder, self).__init__()
        self.style = ThemedStyle()
        self.style.theme_use("breeze")
        self.geometry('570x150')
        self.title("Add another exam")
        self.TitleLabel = Label(self,text="Add another exam to the database!!",font=("Merriweather",20),relief=RIDGE,borderwidth=3)
        self.nameText = Entry(self, font=("Merriweather",20), width=27)
        self.dateText= Entry(self,font=("Merriweather",20),width=27)
        self.nameL = Label(self,text="Exam Name : ",font=("Merriweather",20),width=10)
        self.dateL = Label(self,text="Exam Date : ",font=("Merriweather",20),width=10)
        self.addButton=Button(self,text="Add Exam",command=lambda: self.add_exam(self.nameText.get(),self.dateText.get()))
        self.place_stuff()
        return

    def add_exam(self,exname,exdate):
        try:
            addExam(exname,exdate)
            messagebox.showinfo("Success","Exam added successfully!")
            self.destroy()

            obj = markFrame.instances[0]
            obj.refresh_butons()
        except:
            messagebox.showwarning("Exam Add Error","Exam was not added successfully!")

    def place_stuff(self):
        self.TitleLabel.grid(row=0,column=0,columnspan=2)
        self.nameL.grid(row=1,column=0)
        self.nameText.grid(row=1,column=1)
        self.dateL.grid(row=2,column=0)
        self.dateText.grid(row=2,column=1)
        self.addButton.grid(row=3,column=0,columnspan=2,sticky=NSEW)

class ClassInfo(Frame):
    def __init__(self, root):
        super().__init__(root, borderwidth=2, height=400, width=224, relief=GROOVE)
        self.title = Label(self, text="Class Information", font=("Merriweather", 20), borderwidth=3, relief=GROOVE)

        self.tottest = Entry(self, width=19, font=("Merriweather", 12))

        self.testdate = Entry(self, width=19, font=("Merriweather", 12))
        self.classavg = Entry(self, width=19, font=("Merriweather", 12))
        self.nofail = Entry(self, width=19, font=("Merriweather", 12))
        self.stdslist = Listbox(self, width=19, font=("Merriweather", 12), activestyle=NONE)
        self.totstds = Listbox(self, width=19, font=("Merriweather", 12), activestyle=NONE)
        self.separator = Separator(self, orient='horizontal')
        self.separator.place(x=0, y=170, width=224, height=10)
        self.listscroll = Scrollbar(self)
        self.__set_text()
        self.title.place(x=0, y=0)

    def __set_text(self):
        self.tottest.insert(0, f"Tests : {len(get_tests())}")
        self.tottest.config(state=DISABLED)

    def update_class_info(self, clas):
        global CLASS_IN_USE
        CLASS_IN_USE = clas
        self.totstds.delete(0, END)
        for i in getStudentStats(clas):
            self.totstds.insert(0, i)
        self.stdslist.delete(0, END)
        for i in get_student_list(clas)[::-1]:
            self.stdslist.insert(0, i)

    def place_text(self, clas):
        for i in getStudentStats(clas):
            self.totstds.insert(0, i)
        for i in get_student_list(clas)[::-1]:
            self.stdslist.insert(0, i)
        self.totstds.place(x=0, y=40, width=220, height=80)
        self.tottest.place(x=0, y=125, width=220)

        self.stdslist.place(x=0, y=180, width=200, height=210)
        self.listscroll.place(x=190, y=180, width=34, height=210)
        self.stdslist.config(yscrollcommand=self.listscroll.set)
        self.listscroll.config(command=self.stdslist.yview)


class mainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.style = ThemedStyle()
        self.geometry("823x400")
        self.title("Mark Processing 2022 - Student Portal")
        self.iconp = PhotoImage(file="images/login_icon.png")
        self.iconphoto(False, self.iconp)
        self.loginphoto = Label(text="Please Login to see more in this Screen!", font=("Merriweather", 20),
                                background="#eb3434", borderwidth=5, relief=SUNKEN)
        self.__set_login_standby()

    def change_theme(self, th: str):
        self.style.theme_use(th)

    def __set_login_standby(self):
        self.loginphoto.pack(anchor=CENTER)

    def remove_standby(self):
        self.loginphoto.forget()
        self.loginphoto.destroy()


class userInfoFrame(Frame):
    def __init__(self, root):
        super().__init__(root, borderwidth=3, height=400, width=190, relief=RIDGE)
        self.teacherID = 0
        self.namet = Entry(self, width=19, font=("Merriweather", 12))
        self.mailt = Entry(self, width=19, font=("Merriweather", 12))
        self.logint = Entry(self, width=19, font=("Merriweather", 12))
        self.classSelectLabel = Entry(self, width=19, font=("Merriweather", 12))
        self.classSelect = Combobox(self, width=18, font=("Merriweather", 12), state="readonly")
        self.userimg = PhotoImage(file="images/user_icon.png")
        self.selectButton = Button(self, text="Select Class")
        self.__place_widgets()

    def update_info(self, clas):
        info = session_info(self.teacherID)
        self.namet.insert(0, info[0])
        self.mailt.insert(0, info[1])
        self.logint.insert(0, f"Unique ID : {info[2]}")
        self.classSelectLabel.insert(0, "Choose Class")
        classes = get_classes()
        self.classSelect["values"] = classes
        self.classSelect.current(classes.index(clas))
        self.namet.config(state=DISABLED)
        self.mailt.config(state=DISABLED)
        self.logint.config(state=DISABLED)
        self.classSelectLabel.config(state=DISABLED)

    def __place_widgets(self):
        Label(self, image=self.userimg, width=10).place(x=34, y=0)
        self.namet.place(x=0, y=126)
        self.mailt.place(x=0, y=156)
        self.logint.place(x=0, y=186)
        self.classSelectLabel.place(x=0, y=230)
        self.classSelect.place(x=0, y=264)
        self.selectButton.place(x=0, y=300, width=185)


class markFrame(Frame):
    instances=[]
    def __init__(self, root):
        super().__init__(root, borderwidth=3, height=400, width=410, relief=RIDGE)
        self.topic_label = Label(self, text=" Examinations in this year : 2022", font=("Merriweather", 20),
                                 relief=GROOVE,
                                 borderwidth=3)
        self.exambuttons = []
        self.examAddButton = Button(self,text="Add a new Examination",command=add_an_exam)
        self.window = root
        self.__place_widgets()
        self.style = ThemedStyle()

    def __new__(cls, *args, **kwargs):
        s=super(markFrame, cls).__new__(cls)
        markFrame.instances.append(s)
        return s

    def __getName__(self, button):
        exam = get_code(button.cget("text"))
        open_reportCard(self.window, CLASS_IN_USE, exam)
        print(button.cget("text"))

    def show_Tests(self):
        l = 1
        b = 40
        testObj = Test(self)
        testList = testObj.returnTests()
        condition = 0
        while condition < len(testList):
            if (l + 100) <= 401 and (b + 80) <= 400:
                temp = Button(self, text=testList[condition],name=testList[condition].lower())
                temp.config(command=lambda button=temp: self.__getName__(button))
                temp.place(x=l, y=b, width=100, height=80)
                self.exambuttons.append(temp)
                l += 100
                condition += 1
            elif (l + 100) >= 401 and (b + 80) <= 400:
                if b + 200 <= 400:
                    l = 1
                    b += 80
                    temp = Button(self, text=testList[condition])
                    temp.config(command=lambda button=temp: self.__getName__(button))
                    temp.place(x=l, y=b, width=100, height=80)
                    self.exambuttons.append(temp)
                else:
                    print(f"Placed {condition} buttons !")

                    condition = 0

    def refresh_butons(self):
        for i in self.exambuttons:
            i.destroy()
        self.show_Tests()

    def __place_widgets(self):
        self.examAddButton.place(x=2,y=350,height=40,width=410)
        self.topic_label.place(x=2, y=0)
