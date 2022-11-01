from tkinter import Toplevel,PhotoImage,Tk,LabelFrame,Frame
from tkinter.constants import *
from ttkthemes import ThemedStyle
from tkinter.ttk import Scrollbar,Treeview,Entry,Combobox,Button
from sqlConnectors import get_table,get_no_failed,get_date,get_marks
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

def open_reportCard(toplevel_window,clas,test):
    level = markWindow(toplevel_window, clas, test)
    style = ThemedStyle()
    style.theme_use("breeze")
    level.mainloop()

class markWindow(Toplevel):
    def __init__(self,root,clas,exam):
        super().__init__(root)
        self.clas=clas
        self.exam=exam
        self.geometry("1300x600")
        self.title("Report Card")
        self.selectionframe=self.get_frame()
        self.get_graph(self.exam,self.clas,"ALL")

        self.clasinfo=Entry(self,width=20,font=("Merriweather",12))
        self.exdate = Entry(self, width=20, font=("Merriweather", 12))
        self.testname = Entry(self, width=20, font=("Merriweather", 12))
        self.clasinfo.insert(0,f"Class : {clas}")
        self.exdate.insert(0,f"Exam Date : {get_date(exam)}")
        self.testname.insert(0,f"Name : {exam.title()}")
        self.clasinfo.config(state=DISABLED,foreground="black")
        self.testname.config(state=DISABLED,foreground="black")
        self.exdate.config(state=DISABLED,foreground="black")
        self.marktable= markTree(self,get_table(clas,exam))
        self.get_scrollbar()
        self.place_stuff()

    def get_graph(self,exam,clas,graph="MD",subject="ALL"):
        try:
            self.graphFrame.place_forget()
            self.graphFrame.destroy
        except:
            pass

        self.graphFrame = Frame(self)
        self.graphFrame.place(x=650, y=10)

        subject=''
        if self.box1.get()=="All Subjects":
            subject="ALL"
        else:
            subject=self.box1.get()

        obj=Graphs(exam,clas)

        if graph=="MD":
            self.currGraph=obj.getMarkDistribution(self.graphFrame,subject)
            self.currGraph[0].pack()
        else:
            self.currGraph=obj.getFailureRate(self.graphFrame,subject)
            self.currGraph[0].pack()

    def get_frame(self):
        a = LabelFrame(self, text="Graph Option", font=("Arial", 13))
        FailBut = Button(a, text="Show Failure Rate", width=24,command=lambda: self.get_graph(self.exam,self.clas,"F"))
        DistBut = Button(a, text="Show Mark Distribution", width=24,command=lambda: self.get_graph(self.exam,self.clas,"MD"))
        self.box1 = Combobox(a,width=20, font=("Merriweather", 12), state="readonly")
        self.box1["values"] = ["All Subjects", "English", "Maths", "Chemistry", "Physics", "Elective"]
        self.box1.current(0)
        FailBut.grid(row=0, column=0)
        DistBut.grid(row=1, column=0)
        self.box1.grid(row=0, column=1)
        return a

    def get_scrollbar(self):
        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.marktable.yview)
        self.marktable.configure(yscroll=self.scrollbar.set)

    def place_stuff(self):
        self.marktable.place(x=10,y=10)
        self.scrollbar.place(x=600,y=10,height=265)
        self.clasinfo.place(x=10, y=270)
        self.testname.place(x=10, y=300)
        self.exdate.place(x=10, y=330)
        self.selectionframe.place(x=205,y=270)




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

class Graphs():
    def __init__(self,exam,clas):
        self.exam=exam
        self.clas=clas

    def getFailureRate(self,window,subject="ALL"):
        fig = Figure(figsize=(3,3),
                     dpi=130)
        if subject=="ALL":
            a = get_no_failed(self.clas, self.exam)
            fig.suptitle("Failure Rate on All Subjects", fontsize=13)
            y = [a, 40 - a]
            labes = ["Failed", "Passed"]
            plot1 = fig.add_subplot()
            plot1.pie(y, labels=labes, wedgeprops={'edgecolor': 'black'}, autopct=lambda p: '{:.0f}'.format(p * 0.4))

        else:
            a = get_no_failed(self.clas, self.exam,subject)
            fig.suptitle(f"Failure Rate on {subject}", fontsize=13)
            y = [a, 40 - a]
            labes = [f"Failed", f"Passed"]
            plot1 = fig.add_subplot()
            plot1.pie(y, labels=labes, wedgeprops={'edgecolor': 'black'}, autopct=lambda p: '{:.0f}'.format(p * 0.4))

        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig,
                                   master=window)
        canvas.draw()
        a=canvas.get_tk_widget()
        toolbar = NavigationToolbar2Tk(canvas,
                                       window)
        toolbar.update()
        b=canvas.get_tk_widget()
        return a,b

    def getMarkDistribution(self,window,subject="ALL"):
        fig = Figure(figsize=(3,3),
                     dpi=130)
        if subject=="ALL":
            fig.suptitle("Total Mark Distribution", fontsize=15)
            marks = get_marks(self.clas, self.exam)
            mbins = [i for i in range(0, 401, 50)]
            ax = fig.add_subplot()
            counts, edges, bars = ax.hist(marks, bins=mbins, edgecolor='black')
            ax.set_xlabel("Total Marks")
            ax.set_ylabel("Number of students")
            ax.bar_label(bars)
        else:
            fig.suptitle(f"Mark Distribution for {subject}", fontsize=13)
            marks = get_marks(self.clas, self.exam,subject)
            mbins = [i for i in range(0, 101, 10)]
            ax = fig.add_subplot()
            counts, edges, bars = ax.hist(marks, bins=mbins, edgecolor='black')
            ax.set_xlabel(f"Marks in {subject}")
            ax.set_ylabel("Number of students")
            ax.bar_label(bars)

        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig,
                                   master=window)
        canvas.draw()
        a=canvas.get_tk_widget()
        toolbar = NavigationToolbar2Tk(canvas,
                                       window)
        toolbar.update()
        b=canvas.get_tk_widget()
        return a,b


mainwindow=Tk()
open_reportCard(mainwindow,"12-E","premidterm")