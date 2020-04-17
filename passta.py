from datetime import datetime
from tkinter import Tk
import os.path
from time import *

pasta = Tk().clipboard_get()
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y")
postoji = os.path.isfile('MyFile.txt')
if postoji:
    f = open("MyFile.txt")
    last_line = f.readlines()[-1]
    f.close()

    if last_line != pasta + " - text was copied on " + dt_string:
        file1 = open("MyFile.txt", "a")
        file1.write("\n" + pasta + " - text was copied on " + dt_string)
        file1.close()
    else:
        print("The text you copied is the same as the last saved link!")
        sleep(4)
else:
    file1 = open("MyFile.txt", "a")
    file1.write("All of your saved links")
    file1.close()
