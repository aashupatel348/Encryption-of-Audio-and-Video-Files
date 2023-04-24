import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
import subprocess

window1 = tk.Tk() 
window1.title("Video and Audio Encryption Decryption") 
window1.geometry('1259x729')


start1 = tk.Label(text = "Video And Audio \nENCRYPTION DECRYPTION", font=("Arial", 55, "underline"), fg="magenta") 
start1.place(x = 120, y = 10)

def start_enc():
                subprocess.call(['python', 'enc.py'])

def start_dec():
        
        subprocess.call(['python', 'dec.py'])


selectb=Button(window1, text="ENCRYPT FILE",command=start_enc,  font=("Arial", 25), bg = "orange", fg = "blue")
selectb.place(x = 120, y = 450)


selectb=Button(window1, text="DECRYPT FILE",command=start_dec,  font=("Arial", 25), bg = "orange", fg = "blue")
selectb.place(x = 550, y = 450)


def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()


getb=Button(window1, text="EXIT",command=exit_win1,  font=("Arial", 25), bg = "red", fg = "blue")
getb.place(x = 980, y = 450)

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()