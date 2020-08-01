#This class will be the runner for the gui

import tkinter as tk
from tkinter import ttk

VERSIONNUMBER = 0.1
LASTUPDATED = "7/31/2020"



#inits the window
window = tk.Tk()

window.title("CSV Compare Tool " + str(VERSIONNUMBER))
window.geometry("600x600")
window.minsize(500,500)
window.maxsize(750,750)

#top windows
#top menus ****Needs work***
menu = tk.Menu(window)
window.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Exit", command=window.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command = lambda: openAboutWindow(LASTUPDATED,VERSIONNUMBER))








#functions
#opens a new window to explain how to use the tester
def openAboutWindow(updatedDate, versionNum):
    aboutWindow = tk.Tk()
    aboutWindow.geometry("500x500")
    aboutWindow.maxsize(500,350)
    aboutWindow.minsize(500,350)
    aboutWindow.title("About the CSV compare tool")
    ttk.Label(aboutWindow, text = "This program is used to compare two csv files to the other\n\nThis will take the first file and compare it to the second, not vice virsa"
                     "\n\n"
                     "For Help Please contact IT and ask for Amanda Hugenkiz, or reach out to her pager at 8675309\n\n").grid(column =0, row = 0)
    ttk.Label(aboutWindow, text = "Version Number: " + str(versionNum) +" Updated: " +updatedDate).grid(sticky = 's')
    return







#starts the fun
window.mainloop()