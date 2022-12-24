from tkinter import Toplevel, Text, Button

import student_scope
from student_scope import *
from sqlConnectors import check_password,register_teacher


container = mainWindow()
infof = userInfoFrame(container)
marksf = markFrame(container)
classInfo = ClassInfo(container)

def register_new_teacher():
    a = RegisterWindow()
    a.mainloop()

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

        self.userT =Entry(self,width=30,font=("Merriweather",20))
        self.passT=Entry(self,width=30,font=("Merriweather",20))
        self.mainT=Entry(self,width=30,font=("Merriweather",20))
        self.classT=Entry(self,width=30,font=("Merriweather",20))
        self.uniqueT=Entry(self,width=30,font=("Merriweather",20))
        self.registerbutt = Button(self,text="Register new teacher",
                                   command=lambda: self.register_user(self.userT.get(),
                                                                      self.passT.get(),
                                                                      self.mainT.get(),
                                                                      self.classT.get(),
                                                                      self.uniqueT.get()))

        self.place_stuff()
    def register_user(self,user,pas,mail,clas,unid):
        try:
            register_teacher(user,pas,mail,clas,unid)
            messagebox.showinfo("Success!",f"A new teacher {user} has been registered!")
            self.destroy()
        except:
            messagebox.showerror("Teacher Add Error","Registration failed\nPlease try again.")



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

class topLevel(Toplevel):
    @staticmethod
    def __place_widgets(bgimg, topic):
        bgimg.place(x=0, y=0)
        topic.place(x=10, y=10)

    def get_in_front(self, root):
        self.wm_transient(root)

    def __init__(self, root):
        super().__init__(root)
        self.style = ThemedStyle()
        self.geometry('500x375')
        self.login_icon = PhotoImage(file="images/login_icon.png")
        self.login_background = PhotoImage(file="images/login_background_edited.png")
        self.title("Student Mark Processing - Login")
        self.iconphoto(False, self.login_icon)
        self.bgimg = Label(self, image=self.login_background)
        self.topic = Label(self, text="Student mark processing program 2022", font=("Ubuntu", 20)
                           , borderwidth=3, relief=GROOVE)
        self.__place_widgets(self.bgimg, self.topic)

    def set_theme(self, th: str):
        self.style.theme_use(th)


login_page = topLevel(container)


class InfoFrame(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.style = ThemedStyle()
        self.idlabel = Label(self, text="Username :", font=("lora", 15), borderwidth=2, relief=SUNKEN)
        self.passlabel = Label(self, text="Password :", font=("lora", 15), borderwidth=2, relief=SUNKEN)
        self.incorrectlabel = Label(self, text="     ", font=("lora", 15),
                                    foreground="#f54242",
                                    background="#d4d4d2")
        self.idbox = Text(self, height=1, width=15, font=("lora", 15))
        self.passbox = Text(self, height=1, width=15, font=("lora", 15))
        self.loginbutt = Button(self, text="Login", command=self.check_correct_login)
        self.registerbutt = Button(self,text="Register",command=register_new_teacher)
        self.__place_widgets()

    def check_correct_login(self):
        session = check_password(self.idbox.get(0.0, END).strip(), self.passbox.get(0.0, END).strip())
        if session[1] == True:
            login_page.destroy()
            container.remove_standby()
            infof.place(x=0, y=0)
            marksf.place(x=190, y=0)
            infof.teacherID = session[0]
            infof.update_info(session[2])
            student_scope.CLASS_IN_USE=session[2]
            marksf.show_Tests()
            classInfo.place(x=600, y=0)
            classInfo.place_text(session[2])
            container.change_theme("breeze")
            infof.selectButton.config(command=lambda: classInfo.update_class_info(infof.classSelect.get()))
        else:
            self.incorrectlabel.config(text="Incorrect username/password!")

    def get_focus(self):
        self.idbox.focus_set()

    def __place_widgets(self):
        self.idlabel.grid(row=0, column=0, sticky=W)
        self.passlabel.grid(row=1, column=0, sticky=W)
        self.idbox.grid(row=0, column=1, sticky=W)
        self.passbox.grid(row=1, column=1, sticky=W)
        self.incorrectlabel.grid(row=2, column=0, columnspan=2)
        self.loginbutt.grid(row=4, column=0, sticky=E)
        self.registerbutt.grid(row=4,column=1,sticky=W)
        self.place(x=120, y=140)


login_frame = InfoFrame(login_page)
login_frame.get_focus()
login_frame.style.theme_use("elegance")

container.mainloop()
