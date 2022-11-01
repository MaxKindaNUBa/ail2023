import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def remove_plot():
    w.pack_forget()   # here you remove the widget from the tk window
    # w.destroy()


if __name__ == '__main__':

    # data
    x, y = [1, 2, 3, 4], [1, 4, 9, 16]

    # matplotlib stuff
    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    ax1.plot(x, y)
    ax1.set_title('Country Vs. GDP Per Capita')

    # tkinter stuff
    root = tk.Tk()

    bar1 = FigureCanvasTkAgg(figure1, root)
    w = bar1.get_tk_widget()
    w.pack(side=tk.LEFT, fill=tk.BOTH)   # here you insert the widget in the tk window
    button_delete = tk.Button(root, text='Remove Plot', command=remove_plot)
    button_delete.place(height=30, width=100, rely=0.02, relx=0.4)   # place is an odd choice of geometry manager, you will have to adjust it every time the title changes

    root.mainloop()