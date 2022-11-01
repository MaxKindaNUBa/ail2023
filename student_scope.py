from tkinter import Tk, PhotoImage, Listbox, Button
from tkinter.constants import *
from ttkthemes import ThemedStyle
from tkinter.ttk import Frame, Label, Entry, Button, Separator, Combobox, Scrollbar
from testHandler import Test
from sqlConnectors import session_info, get_classes, getStudentStats, get_tests, get_student_list, get_code
from reportCard import open_reportCard

CLASS_IN_USE = ''


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
    def __init__(self, root):
        super().__init__(root, borderwidth=3, height=400, width=410, relief=RIDGE)
        self.topic_label = Label(self, text=" Examinations in this year : 2022", font=("Merriweather", 20),
                                 relief=GROOVE,
                                 borderwidth=3)
        self.window = root
        self.__place_widgets()
        self.style = ThemedStyle()

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
                temp = Button(self, text=testList[condition])
                temp.config(command=lambda button=temp: self.__getName__(button))
                temp.place(x=l, y=b, width=100, height=80)
                l += 100
                condition += 1
            elif (l + 100) >= 401 and (b + 80) <= 400:
                if b + 200 <= 400:
                    l = 1
                    b += 80
                    temp = Button(self, text=testList[condition])
                    temp.config(command=lambda button=temp: self.__getName__(button))
                    temp.place(x=l, y=b, width=100, height=80)
                else:
                    print(f"Placed {condition} buttons !")

                    condition = 0

    def __place_widgets(self):
        self.topic_label.place(x=2, y=0)
