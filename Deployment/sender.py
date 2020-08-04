from tkinter import *
import tkinter as tk
import serial
serialcom = serial.Serial('COM5', 9600)
serialcom.timeout = 1
t = 0
b = 0
def key(event):
    """shows key or tk code for the key"""
#    if event.keysym == 'Escape':
#        root.destroy()
    global t
    global b
    if event.keysym == 'Up':
        i = 'f'
        t = t+1
        if(t == 1):
            print("f")
            serialcom.write(i.encode())
            print(serialcom.readline().decode('ascii'))
    if event.keysym == 'Down':
        i = 'b'
        b = b+1
        if(b == 1):
            print("b")
            serialcom.write(i.encode())
            print(serialcom.readline().decode('ascii'))
    if event.keysym == 'Left':
        print("l")
        i = 'l'
        serialcom.write(i.encode())
        print(serialcom.readline().decode('ascii'))
    if event.keysym == 'Right':
        print("r")
        i = 'r'
        serialcom.write(i.encode())
        print(serialcom.readline().decode('ascii'))
    if event.keysym == 'a':
        print("[")
        i = '['
        serialcom.write(i.encode())
        print(serialcom.readline().decode('ascii'))
    if event.keysym == 'b':
        print("]")
        i = ']'
        serialcom.write(i.encode())
        print(serialcom.readline().decode('ascii'))


class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.go = False
        self.bind('<Key>', key)
        self.bind('<KeyRelease>', self.makeChoice)
#        self.bind('<Button-1>', self.showJudgments)
        self.pack(expand=YES, fill=BOTH)
        self.focus_force()

    def makeChoice(self, event=None):
        print("now stop")
        i = 's'
        global t
        t = 0
        global b
        b = 0
        serialcom.write(i.encode())
        print(serialcom.readline().decode('ascii'))
        self.go = False


mainw = Tk()
mainw.f = MyFrame(mainw)
mainw.f.grid()
mainw.mainloop()
serialcom.close()
