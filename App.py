import os, shutil
from tkinter import *
from tkinter import messagebox

from FaceID import FaceID


class Application(object):
    PATH = 'users/'
    IDENTIFY_ACCURACY = 0.5

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
        self.but_reset = Button(self.root, bg='#c3b3e4', text="Reset", command=self.but_reset)
        self.but_reset.pack(fill='both', side='top')
        self.listbox = Listbox(self.root, font='Arial 14', bg='#8bb4d3', height=5, selectmode=EXTENDED)
        self.listbox.pack(fill='both', side='top')

    def but_reset(self):
        user_id = self.listbox.curselection()
        # select with less index
        FaceID.create_person(self.PATH + self.listbox.get(user_id[0]) + '\\', 10)

    def but_add_user(self):
        username = self.input_user.get(0.0, END)
        # without \n at the end
        short_name = username[:self.input_user.count(0.0, END)[0] - 1]
        if not short_name in self.listbox.get(0, END) \
                and not username in self.listbox.get(0, END):
            self.listbox.insert(END, username)
            os.mkdir(self.PATH + short_name) # create user folder
            FaceID.create_person(self.PATH + short_name + '\\', 10)

    def but_delete_user(self):
        for i in reversed(self.listbox.curselection()): # selected users
            self.listbox.delete(i)
        users = self.listbox.get(0, END)
        for user in os.listdir(self.PATH):
            if not user in users and not user + '\n' in users:
                if os.path.exists(self.PATH + user):
                    shutil.rmtree(self.PATH + user) # remove user folder

    def identify_users(self):
        for user_dir in os.listdir(self.PATH):
            if len(os.listdir(self.PATH + '/' + user_dir)) == 0: continue
            if FaceID.identify(self.PATH + '/' + user_dir, self.IDENTIFY_ACCURACY):
                messagebox.showinfo("Info", "Recognized successfully")
                return True
        return False

    def load_users(self):
        if not os.path.exists('users'): os.mkdir('users')
        for user in os.listdir(self.PATH): self.listbox.insert(END, user)

    def app_run(self):
        self.load_users()
        self.identify_users()
        self.root.mainloop()


Application().app_run()  # run main function
