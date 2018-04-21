#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidget()
    def createWidget(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alterButton = Button(self, text="hello", command=self.hello)
        self.alterButton.pack()

    def hello(self):
        text = self.nameInput.get() or "world"
        messagebox.showinfo("Message", "Hello, %s" % text)


if __name__ == '__main__':
    app = Application()
    app.master.label = "Hello world!"
    app.mainloop()
