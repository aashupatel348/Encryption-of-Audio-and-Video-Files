import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
import subprocess

window = tk.Tk()  
window.title("Video and Audio  Encryption Decryption") 
window.geometry('1259x729')


start1 = tk.Label(text = "Video and Audio \nENCRYPTION  DECRYPTION", font=("Arial", 55,"underline"), fg="magenta") 
start1.place(x = 120, y = 10)

def start_fun():
    subprocess.call(['python', 'Start.py'])

startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =150 , y =580 )

def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()



exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y = 580 )
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()


