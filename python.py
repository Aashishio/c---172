from tkinter import *

root = Tk()

root.title("User Database")
root.geometry("600x600")

lbl_usrname = Label(root, text="Username: ")
lbl_usrname.place(relx=0.4, rely=0.1, anchor=CENTER)

ent_usrname = Entry(root)
ent_usrname.place(relx=0.6, rely=0.1, anchor=CENTER)

lbl_emailid = Label(root, text="Email id: ")
lbl_emailid.place(relx=0.4, rely=0.2, anchor=CENTER)

ent_emailid = Entry(root)
ent_emailid.place(relx=0.6, rely=0.2, anchor=CENTER)

lbl_database = Label(root)
lbl_database.place(relx=0.5, rely=0.5, anchor=CENTER)

# dictionary = {}
dictionary1 = []

val = ent_usrname.get()
ent = ent_emailid.get() 

class User():
    def __init__(self):
        pass
    
    def addUser(user, email):
        # global dictionary1
        # dictionary[key] = value
        dictionary1.append("{ "+user+" : "+ email +" } ")
        lbl_database['text'] = str(dictionary1)
    
class GetUser(User):
    def __init__(self, key, val):
        self.key = key
        self.val = val
    
    def getUser(self):
        print(self.key+":"+self.val)
        User.addUser(self.key, self.val)

obj = GetUser(ent_usrname.get(), ent_emailid.get())
obj.getUser()

def ent():
    print(str(val)+":"+str(ent))

btn = Button(root, text="Add user details", command=ent())
btn.place(relx=0.5, rely=0.3, anchor=CENTER)

root.mainloop()