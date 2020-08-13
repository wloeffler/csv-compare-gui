# This class will be the runner for the gui

import tkinter as tk
from tkinter import ttk
from tkinter import font
from Info import inputInfo
from drisComp import Comparer

VERSIONNUMBER = 0.69
LASTUPDATED = "7/31/2020"
DEFAULTRANGELIST = list(range(1,21))


# inits the window
window = tk.Tk()

window.title("CSV Compare Tool " + str(VERSIONNUMBER))
window.geometry("450x400")
window.minsize(400, 400)
window.maxsize(750, 750)

# top windows
# top menus ****Needs work***
menu = tk.Menu(window)
window.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Exit", command=window.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=lambda: __openAboutWindow(LASTUPDATED, VERSIONNUMBER))


# functions
# opens a new window to explain how to use the tester
def __openAboutWindow(updatedDate, versionNum):
    aboutWindow = tk.Tk()
    aboutWindow.geometry("500x350")
    aboutWindow.maxsize(500, 350)
    aboutWindow.minsize(500, 350)
    aboutWindow.title("About the CSV compare tool")
    ttk.Label(aboutWindow,
              text="This program is used to compare two csv files to the other\n\nThis will take the first file and compare it to the second, not vice virsa"
                   "\n\n"
                   "For Help Please contact IT and ask for Amanda Hugenkiz, or reach out to her pager at 8675309\n\n").grid(
        column=0, row=0)
    ttk.Label(aboutWindow, text="Version Number: " + str(versionNum) + " Updated: " + updatedDate).grid(sticky='s')
    return


def __clearInput(entryToBeCleared):
    entryToBeCleared.delete(0,'end')
    entryToBeCleared.insert(0,"")

def __compare(input1, input2):
    if(input1.get()=="" or input2.get()==""):
        temp1 = tk.Label(window, text ="YOU DONE MESSED UP A-A-RON...\nPlease input a valid file path", fg = 'red').grid(row = 4,column = 0, columnspan = 2,sticky = "s")

    else:
       # numberOfCols = __numberOfColumns(numberColumns)
        infoPasser = inputInfo(input1.get(), input2.get())

        #calls the comparison tool
        magicComparer = Comparer(infoPasser)

    return


#this will display a message from an external source
def externalWindow(messageString,runningChar, specialMessage):
    externalWindowInstance = tk.Tk()
    externalWindowInstance.geometry(200,200)
    label = tk.Label(externalWindowInstance, text = messageString).grid(row = 0, column = 0, sticky = 's')
    label2 = tk.Label(externalWindowInstance, text = specialMessage).grid(row = 1, column = 0, sticky ='s')
    return

#returns a list for the total number of columns to be compared
def __numberOfColumns(num):
    return list(range(0,(int(num)-1)))




#gui layout


bbc = font.Font(weight = 'bold')
inputBox1Label = tk.Label(window,text="Input CSV 1", font = bbc).grid(column=0, row=0, padx=10, pady=10)
inputBox1 = ttk.Entry(window, width = 20)
inputBox1.grid(column=0, row=1, padx=10, pady=10)

inputBox2Label = tk.Label(window,text="Input CSV 2", font = bbc).grid(column=1, row=0, padx=10, pady=10)
inputBox2 = ttk.Entry(window, width = 20)
inputBox2.grid(column=1, row=1, padx=10, pady=10)

clearButton1 = tk.Button(text = "clear CSV 1", command = lambda:__clearInput(inputBox1)).grid(column= 0, row = 2, padx = 10, pady =5)
clearButton2 = tk.Button(text = "clear CSV 2", command = lambda:__clearInput(inputBox2)).grid(column= 1, row = 2, padx = 10, pady =5)

'''
numberColLabel = tk.Label(window, text = "Number of Columns").grid(column = 0, row =3, padx =5, pady = 5)
numberColEntry = ttk.Combobox(window, values = DEFAULTRANGELIST)
numberColEntry.grid(column = 1, row = 3, padx = 5, pady =5)

'''



runButton= tk.Button(text = "Compare", command = lambda: __compare(inputBox1, inputBox2), font = bbc).grid(row = 5,column = 0, columnspan = 2,sticky = "s")


# starts the fun
window.mainloop()
