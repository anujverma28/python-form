import tkinter
import sqlite3
from tkinter import *
from tkinter import messagebox
root = tkinter.Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title('Registration Form')
FullName = StringVar()
Email = StringVar()
var = IntVar()
c=StringVar()
var1 = IntVar()

def not_allowed():
    messagebox.showinfo('Gui','All field are requered')



def check():
    messagebox.showinfo('Gui','Data saved successfully')


def database():
    name1 = FullName.get()
    email=Email.get()
    gender=var.get()
    if gender==1:
        gender='Male'
    else:
        gender='Female'

    country=c.get()
    prog=var1.get()
    if prog==1:
        prog='Java'
    else:
        prog='Python'

    if name1=='' and email=='' and gender=='Female' or gender=='Male' and country=='select your country' and prog=='Python' or prog=='Java':
        not_allowed()
    else:
        conn =sqlite3.connect('From.db')
        with conn:
            cursor=conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT, Email TEXT,Gender TEXT,Country TEXT,Programming TEXT )')
            cursor.execute('INSERT INTO Student (Fullname,Email,Gender,Country,Programming) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog))
            conn.commit()

            check()




            

label_0 =Label(root, text='Registration Form', width=20,font=('Arial',10,'bold'))
label_0.place(x=90,y=53)
label_1 =Label(root, text='FullName', width=20,font=('bold',10))
label_1.place(x=80,y=130)


entry_1 =Entry(root,textvar=FullName)
entry_1.place(x=240,y=130)

label_2 = Label(root, text='Email',width=20,font=('bold',10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text='Gender',width=20,font=('bold',10))
label_3.place(x=70,y=230)

tkinter.Radiobutton(root, text='Male',variable=var, value=1).place(x=235,y=230)
tkinter.Radiobutton(root, text='Female',variable=var, value=2).place(x=290,y=230)

label_4 = tkinter.Label(root, text='City', width=20,font=('bold',10))
label_4.place(x=70,y=280)

list1 = ['Hello World','Roorkee','UP','Uk','Meerut','Noida','Tamil Nadu']

droplist = OptionMenu(root,c,*list1)
droplist.config(width=15)
c.set('select your city')
droplist.place(x=240,y=280)


label_4 = tkinter.Label(root,text='Programming',width=20, font=('bold',10))
label_4.place(x=85,y=330)
var2 = IntVar()
Checkbutton(root,text='java',variable=var1).place(x=235,y=330)

Checkbutton(root,text='Python',variable=var2).place(x=290,y=330)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)
root.mainloop()
