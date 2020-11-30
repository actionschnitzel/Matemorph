from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
import os
import sys
from tkinter import ttk
from os import popen
from os import system as cmd
import subprocess
from PIL import ImageTk, Image
from tkinter import messagebox
import webbrowser


fenster = Tk()
fenster['background']='#000000'
#fenster['borderwidth']='5'
fenster.title("Matemorph")
fenster.geometry("450x600")
icon = tk.PhotoImage(file="/home/pi/matemorph/logo.png")
fenster.tk.call('wm', 'iconphoto', fenster._w, icon)


def m1():   
    os.system('xterm -into %d -geometry 100x20 -e ~/matemorph/scripts/m1.sh &' % wid)


def m2():   
    os.system('xterm -into %d -geometry 100x20 -e ~/matemorph/scripts/m2.sh &' % wid)



i10=Image.open('/home/pi/matemorph/matemorph.png')
p10=ImageTk.PhotoImage(i10)


my_label1 = Label(image = p10,highlightcolor="black",highlightbackground="black",highlightthickness=0,borderwidth=0).place(x=0,y=0)



termf = Frame(fenster, height=100, width=450,borderwidth=0)
termf['background']='grey20'
termf.place(x=0,y=380)#,fill=BOTH, expand=NO
wid = termf.winfo_id()

os.system('xterm -into %d -geometry 100x100  &' % wid)

def send_entry_to_terminal(*args):
    """*args needed since callback may be called from no arg (button)
   or one arg (entry)
   """
    cmd("%s" % (BasicCovTests))


sm = Button(fenster,text="Start Metamorphosis Part I",highlightcolor="black",highlightbackground="black",highlightthickness=0,borderwidth=0,font='12',bg='black', fg='#32cd32',command=m1).place(x=0,y=500)

sm2 = Button(fenster,text="Start Metamorphosis Part II",highlightcolor="black",highlightbackground="black",highlightthickness=0,borderwidth=0,font='12',bg='black', fg='#32cd32',command=m2).place(x=0,y=530)















#################################
fenster.mainloop()