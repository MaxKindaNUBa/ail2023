from tkinter import Toplevel,PhotoImage
from tkinter.constants import *
from ttkthemes import ThemedStyle
from tkinter.ttk import Scrollbar,Treeview,Entry
from sqlConnectors import get_table,get_no_failed,get_date

def open_reportCard(toplevel_window,clas,test):
    level = markWindow(toplevel_window, clas, test)
    style = ThemedStyle()
    style.theme_use("breeze")
    level.mainloop()

class markWindow(Toplevel):
    def __init__(self,root,clas,exam):
        super().__init__(root)
        self.geometry("620x340")
        self.title("Report Card")
        self.iconp = PhotoImage(file="images/login_icon.png")
        self.iconphoto(False, self.iconp)
        self.clasinfo=Entry(self,width=20,font=("Merriweather",12))
        self.exdate = Entry(self, width=20, font=("Merriweather", 12))
        self.testname = Entry(self, width=20, font=("Merriweather", 12))
        self.failrate = Entry(self, width=20, font=("Merriweather", 12))
        self.clasinfo.insert(0,f"Class : {clas}")
        self.exdate.insert(0,f"Exam Date : {get_date(exam)}")
        self.testname.insert(0,f"Name : {exam.title()}")
        self.failrate.insert(0,f"No. Of Failed : {get_no_failed(clas,exam)}")
        self.clasinfo.config(state=DISABLED,foreground="black")
        self.testname.config(state=DISABLED,foreground="black")
        self.exdate.config(state=DISABLED,foreground="black")
        self.failrate.config(state=DISABLED,foreground="black")
        self.marktable= markTree(self,get_table(clas,exam))
        self.get_scrollbar()
        self.place_stuff()

    def get_scrollbar(self):
        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.marktable.yview)
        self.marktable.configure(yscroll=self.scrollbar.set)

    def place_stuff(self):
        self.marktable.place(x=10,y=10)
        self.scrollbar.place(x=600,y=10,height=265)
        self.clasinfo.place(x=10,y=270)
        self.testname.place(x=10,y=300)
        self.exdate.place(x=200,y=270)
        self.failrate.place(x=200,y=300)



class markTree(Treeview):
    def __init__(self,root,data):
        super().__init__(root,show="headings")
        self.columns=("Roll NO","Full Name","Core Sub","Phy","Chem","Mat","Eng","Core")
        self['columns']=self.columns
        self.column("Roll NO",width=80)
        self.column("Full Name",width=150)
        self.column("Core Sub",width=80)
        self.column("Phy",width=50)
        self.column("Chem",width=50)
        self.column("Mat",width=50)
        self.column("Eng",width=50)
        self.column("Core",width=50)
        for i in range(len(self.columns)):
            self.heading(self.columns[i],text=self.columns[i])
        self.data=data
        self.placemarks()

    def placemarks(self):
        for i in self.data:
            self.insert('',END,values=i)

