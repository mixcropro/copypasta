import pyperclip
from datetime import datetime
from tkinter import Tk


pasta = Tk().clipboard_get()
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

file1 = open("MyFile.txt", "a")
file1.write("\n" + pasta + " - text was copied at " + dt_string)
file1.close()

'''while True:
    file1 = open("MyFile.txt", "w+")
    lineList = file1.readlines()
    kraj = lineList[-1]
    file1.close()
    if pasta != kraj:
        file1.write("\n" + pasta + " - text was copied at " + dt_string)
    else:
        continue'''








