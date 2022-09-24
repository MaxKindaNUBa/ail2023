from tkinter import Tk, PhotoImage
from tkinter.constants import *
from ttkthemes import ThemedStyle
from tkinter.ttk import Frame, Label, Entry,Button

import sqlConnectors
from sqlConnectors import session_info

class mainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.style = ThemedStyle()
        self.geometry("800x400")
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
        self.classt = Entry(self, width=19, font=("Merriweather", 12))
        self.sect = Entry(self, width=19, font=("Merriweather", 12))
        self.userimg = PhotoImage(file="images/user_icon.png")
        self.__set_text()
        self.__place_widgets()

    def __set_text(self):
        print(self.teacherID)
        self.namet.insert(0, "Not to be seen")
        self.mailt.insert(0, "Not to be seen")
        self.logint.insert(0, "Not to be seen")
        self.classt.insert(0, "Not to be seen")
        self.sect.insert(0, "Not to be seen")

    def update_info(self):
        info = session_info(self.teacherID)
        clas,n,sec=info[2].partition("-")
        self.namet.delete(0,END)
        self.mailt.delete(0,END)
        self.logint.delete(0,END)
        self.classt.delete(0,END)
        self.sect.delete(0,END)
        self.namet.insert(0, info[0])
        self.mailt.insert(0, info[1])
        self.logint.insert(0, f"UniqueID : {info[3]}")
        self.classt.insert(0, f"Class : {clas}")
        self.sect.insert(0, f"Section: {sec}")
        self.namet.config(state=DISABLED)
        self.mailt.config(state=DISABLED)
        self.logint.config(state=DISABLED)
        self.classt.config(state=DISABLED)
        self.sect.config(state=DISABLED)

    def __place_widgets(self):
        Label(self, image=self.userimg, width=10).place(x=34, y=0)
        self.namet.place(x=0, y=126)
        self.mailt.place(x=0, y=156)
        self.logint.place(x=0, y=186)
        self.classt.place(x=0, y=330)
        self.sect.place(x=0, y=360)


class markFrame(Frame):
    def __init__(self, root):
        super().__init__(root, borderwidth=3, height=400, width=410, relief=RIDGE)
        self.topic_label = Label(self,font=("Ubuntu", 20), relief=GROOVE,
                                 borderwidth=3)
        self.__place_widgets()

    def show_Tests(self):
        l = 0
        b = 40
        testList=sqlConnectors.get_tests()
        condition = 0
        while condition < len(testList):
            if (l + 80) <= 400 and (b + 80) <= 400:
                Button(self, text=testList[condition]).place(x=l, y=b, width=80,height=80)
                l += 80
                condition += 1
            elif (l + 80) >= 400 and (b + 80) <= 400:
                if b + 160 <= 400:
                    l = 0
                    b += 80
                    Button(self, text=testList[condition]).place(x=l, y=b, width=80,height=80)

                else:
                    print(f"Placed {condition} buttons !")
                    condition = 0
    def set_title(self,cl):
        self.topic_label.config(text=f"Exams in batch year : {cl} 2022")
        self.topic_label.config(state=DISABLED)

    def __place_widgets(self):
        self.topic_label.place(x=2, y=0)
