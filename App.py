from tkinter import *


class Application(object):

    def __init__(self):
        self.root = Tk()
        self.root.title("FaceId")
        self.root.geometry('300x200+600+200')

        self.input_user = Text(self.root, bg='#b2b3d5', height=1, bd=1, font='Arial 14')
        self.input_user.pack(fill='both', side='top')
        self.input_user.insert(1.0, 'username')
        self.but_add_user = Button(self.root, bg='#c3b3e4', text="Add user", command=self.but_add_user)
        self.but_add_user.pack(fill='both', side='top')
        self.but_delete_user = Button(self.root, bg='#c3b3e4', text="Delete user", command=self.but_delete_user)
        self.but_delete_user.pack(fill='both', side='top')
        self.but_reset = Button(self.root, bg='#c3b3e4', text="Reset", command=self.but_start)
        self.but_reset.pack(fill='both', side='top')
        self.listbox = Listbox(self.root, font='Arial 14', bg='#8bb4d3', height=5, selectmode=EXTENDED)
        self.listbox.pack(fill='both', side='top')

    def but_start(self):
        print("Hello World!")

    def but_add_user(self):
        self.listbox.insert(END, '- ' + self.input_user.get(0.0, END))

    def but_delete_user(self):
        for i in reversed(self.listbox.curselection()):
            self.listbox.delete(i)

    def app_run(self):
        self.root.mainloop()


app = Application()
app.app_run()
