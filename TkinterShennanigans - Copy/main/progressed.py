import time, string, random
import tkinter as tk
import tkinter.simpledialog
from tkinter import messagebox as mb
import os
from tkinter.messagebox import showinfo, showwarning
from pyautogui import *

def rand(n):
    y=''
    for i in range(0,n):
        x = ''.join(random.choice(string.ascii_letters + string.digits))
        y = y + x
    return y

def fibonacci(n):

    top = tk.Toplevel()
    top.attributes('-fullscreen', True)
    top.overrideredirect(True)
    entryBox = (tk.Entry(top,font=36))
    entryBox.focus()
    entryBox.pack()
    f = [0,1,1]
    for i in range(3,n):
        f.append(f[i-1] + f[i-2])
        z = len(str(f[i]))
        for i in range(0,z):
            top.after(0,typewrite(''.join(random.choice(string.ascii_letters + string.digits))))
            top.update()
    btn = tk.Button(top,text='BEGIN', command= lambda: login()).pack()
    return 'The %.0fth fibonacci number is: %.0f' % (n,f[-1])

def login():
    root.destroy()
    name = tkinter.simpledialog.askstring('ANSWER_TRUTHFULLY', 'ENTER_NAME')

    mb.askyesno('USR_NM', 'IS THIS YOUR NAME? ' + name)
    mb.askyesno('...','DID YOU TELL THE TRUTH?')
    if name in os.getlogin() and len(name) >= 4:
        ans = mb.askyesno(rand(26),'want to play some pictionary?')
        if ans:
            quit()
        else:
            showwarning(rand(26), 'looks like we got a party pooper here')
            quit()
    else :
        ttl = 'THEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVER'
        showwarning(title=ttl, message=ttl)
        showinfo('','you lied to me, ' + os.getlogin())

#root.mainloop()