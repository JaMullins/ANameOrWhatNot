import math
import time
from random import random, randint
from tkinter import Button, Toplevel
import pyautogui
from pyautogui import FailSafeException
import dialogue
import BetterShennanigans as bs
import progressed
import FunGame
import tkinter as tk
import pygame as pg
import datetime

def afterChaos():
    progressed.root = tk.Tk()
    progressed.button = tk.Button(progressed.root, text="Initiate secure login",command=lambda: progressed.fibonacci(10)).pack()
    progressed.root.mainloop()
    FunGame.root = pg.display.set_mode((500, 500))
    FunGame.drawStickFigure()
    FunGame.mainLoop()
    FunGame.angry()

def main():
    pyautogui.FAILSAFE = False
    for i in range(0,100):
        t = Toplevel(win)
        color = ['blue','yellow','green','red','orange','purple']
        t.configure(background=color[randint(0, len(color) - 1)])
        #t.attributes('-fullscreen',True)
        x = randint(0,2000)
        y = randint(0,1000)
        t.geometry('+%d+%d'%(x,y))
        time.sleep(0.01)
    win.withdraw()
    #dialogue.main(dialogue.diaList,dialogue.responseList)
    try:
        starttime = datetime.datetime.now()
        print('af')
        annoying = bs.AntiClick()
        annoying.__init__()
        endtime = datetime.datetime.now()
        timer = endtime - starttime
        while timer.seconds < 10:
            endtime = datetime.datetime.now()
            timer = endtime - starttime
            print(timer.seconds)
        else:
            print('done')
    except pyautogui.FailSafeException:
        afterChaos()
    except KeyboardInterrupt:
        print('UH OH KEYBOARD BROKE')
    except NotImplementedError:
        afterChaos()

win = tk.Tk()
btn = Button(win,command=main,text='NO TRESPASSING')
btn.pack()
win.mainloop()