import os
from tkinter import *
import tkinter as tk

# Create an instance of tkinter frame or window
window=Tk()
# Set the size of the tkinter window
window.geometry("700x350")
window.title("PythonGeeks")#give title to the window
head=Label(window, text="SHUTDOWN, RESTART, LOGOUT WITH PYTHON", font=('Times Roman', '14'))# a label
head.pack(pady=20)

#creating buttons
#Button(window,text='Shutdown',command=Shutdown, font=('normal',11), bg='yellow').pack()
#Button(window,text='Restart',command=Restart,font=('normal',11), bg='yellow').pack()
#Button(window,text='Logout',command=logout,font=('normal',11), bg='yellow').pack()

def Shutdown():#function to shutdown
    os.system("shutdown /s /t 0")

Button(window,text='Shutdown',command=Shutdown, font=('normal',11), bg='cyan').pack()

def Restart():#function to restart
    os.system("shutdown /r /t 0")
Button(window,text='Restart',command=Restart,font=('normal',11), bg='blue').pack()

def logout():#function to logout
    os.system("shutdown /l /t 0") 

Button(window,text='Logout',command=logout,font=('normal',11), bg='brown').pack() 

#creating buttons
Button(window,text='Shutdown',command=Shutdown, font=('normal',11), bg='yellow').pack()
Button(window,text='Restart',command=Restart,font=('normal',11), bg='yellow').pack()
Button(window,text='Logout',command=logout,font=('normal',11), bg='yellow').pack()

window.mainloop() 