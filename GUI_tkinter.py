#GUI

from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.helloButton = Button(self, text='Hello', command=self.hello)
        self.helloButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)
        
if __name__ == '__main__':
    app = Application()
    app.master.title('Hello World')
    app.mainloop()
