import time

import pygame as pg
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP
import tkinter as tk
from tkinter import messagebox as mb
"""
pg.init()
root = pg.display.set_mode((500, 500))
"""
def angry(): #Add code for when [REDACTED] becomes angered
    win = tk.Tk()
    win.title('01110100 01101111 01101111 00100000 01101100 01100001 01110100 01100101')
    textBox = tk.Text(win)
    textBox.pack()
    listy = [
        "EVERY DAY",
        "YOU ALWAYS",
        "RUIN MY FUN",
        "I MAKE A GAME",
        "AND YOU KILL IT",
        "I ASK YOU TO FOLLOW DIRECTIONS",
        "AND YOU CAN'T EVEN DO THAT",
        ".............................",
        "I have an idea...",
        "Say goodbye to your computer."
    ]
    for x in range(0,len(listy)):
        for i in range(0,len(listy[x])):
            textBox.insert(tk.END,listy[x][i])
            textBox.update()
            time.sleep(0.1)
        textBox.insert(tk.END,f"\n")
    time.sleep(3)

def drawStickFigure():
    pg.draw.circle(root, 'blue', (250,100),40,7)
    pg.draw.line(root, 'blue', (250,140),  (250,240),  7)
    pg.draw.line(root, 'blue', (250, 240), (300, 300), 7)
    pg.draw.line(root, 'blue', (250, 240), (200, 300), 7)
    pg.draw.line(root, 'blue', (250, 180), (300, 220), 7)
    pg.draw.line(root, 'blue', (250, 180), (200, 220), 7)

def mainLoop():
    drawing = False
    rect = pg.Rect(240,140,20,40)

    while True:
        x, y = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    root.fill('black')
                    drawStickFigure()

        if event.type == MOUSEBUTTONDOWN:
            drawing = True

        if event.type == MOUSEBUTTONUP:
            drawing = False

        if drawing:
            x2, y2 = pg.mouse.get_pos()
            pg.draw.lines(root, 'red', True, [(x, y),(x2, y2)])
            if rect.collidepoint(x,y):
                break

        pg.display.update()

"""
drawStickFigure()
mainLoop()
mb.showwarning("...really?", "Ya killed him.")
mb.showinfo("I'm not mad", "But why did you make me do all of that just to kill the game")
mb.showinfo("You're quite rude...", "...We have ways of dealing with rude people...")
angry()
"""