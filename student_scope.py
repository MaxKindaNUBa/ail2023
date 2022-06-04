from tkinter import Tk, PhotoImage
from tkinter.constants import *
from ttkthemes import ThemedStyle
from tkinter.ttk import Frame, Label, Entry


class mainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.style = ThemedStyle()
        self.geometry("800x400")
        self.title("Mark Processing 2022 - Student Portal")
        self.iconp = PhotoImage(file="login_icon.png")
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
        self.namet = Entry(self, width=19, font=("Merriweather", 12))
        self.mailt = Entry(self, width=19, font=("Merriweather", 12))
        self.logint = Entry(self, width=19, font=("Merriweather", 12))
        self.classt = Entry(self, width=19, font=("Merriweather", 12))
        self.sect = Entry(self, width=19, font=("Merriweather", 12))
        self.userimg = PhotoImage(file="user_icon.png")
        self.__set_text()
        self.__place_widgets()

    def __set_text(self):
        self.namet.insert(0, "Chandran Kumar")
        self.mailt.insert(0, "gubharan@gmail.com")
        self.logint.insert(0, "Login ID : 12961")
        self.classt.insert(0, "Class : 12")
        self.sect.insert(0, "Section : C")
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


class markWindow(Frame):
    def __init__(self, root):
        super().__init__(root, borderwidth=3, height=400, width=410, relief=RIDGE)
        self.topic_label = Label(self, text="Exams in batch year : 12-C 2022", font=("Ubuntu", 20), relief=GROOVE,
                                 borderwidth=3)
        self.__place_widgets()

    def __place_widgets(self):
        self.topic_label.place(x=2, y=0)
