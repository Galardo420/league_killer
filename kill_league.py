
# Used libraries

import psutil
import ctypes
from tkinter import *

# Window of an app

root = Tk()

root.title("League Killer by Galardo")
root.iconbitmap(r'C:\Users\38761\Desktop\python\kill_league_icon.ico') # Set your path to the location of icon.
root.geometry("300x100")

# Setting process name that we want to kill

PROCNAME = "League of Legends.exe"

# Killing process

def Kill_Process():
    for proc in psutil.process_iter():

        if proc.name() == PROCNAME:
            proc.kill()
            ctypes.windll.user32.MessageBoxW(0, "League killed by Galardo.", "League Killer", 0)
            
# Click button - execute

Kill_League = Button(root, text="Fuck you RITO", command = Kill_Process, height = 2, width = 15)
Kill_League.place(relx=0.5, rely=0.5, anchor=CENTER)

# Running an app

root.mainloop()
