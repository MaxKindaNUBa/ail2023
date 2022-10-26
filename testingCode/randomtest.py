from matplotlib import pyplot as plt
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
from sqlConnectors import get_no_failed

class Graphs():
    def __init__(self,exam,clas):
        self.exam=exam
        self.clas=clas
        self.failured=get_no_failed(self.clas,self.exam)

    def plot(self,window):
        fig = Figure(figsize=(4, 4),
                     dpi=100)

        y = [self.failured,40-self.failured]
        labes = ["Total Failed", "Total Passes"]
        plot1 = fig.add_subplot(111)
        plot1.pie(y, labels=labes, wedgeprops={'edgecolor': 'black'},autopct=lambda p: '{:.0f}'.format(p * 0.4))

        canvas = FigureCanvasTkAgg(fig,
                                   master=window)
        canvas.draw()
        a=canvas.get_tk_widget()

        toolbar = NavigationToolbar2Tk(canvas,
                                       window)
        toolbar.update()
        b=canvas.get_tk_widget()
        return a,b




window = Tk()
window.title('Plotting in Tkinter')
window.geometry("500x500")
graphs=Graphs("midterm1","12-A")

failure_pie=graphs.plot(window)

failure_pie[0].pack()
failure_pie[1].pack(anchor=S)
window.mainloop()