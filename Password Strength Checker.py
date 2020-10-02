from tkinter import *
import os
import re

myGui = Tk()
myGui.geometry('515x115+700+250')
myGui.resizable(0,0)

myGui.title('Check Password Strength')
guiFont = font = dict(family='Courier New, monospaced', size=25, color='Red')


#====== Password Entry ==========
eLabel = Label(myGui, text="Please Enter your Password :-   ",font=('Calibri',15,"bold")
               ,bd=5)
eLabel.grid(row=0, column=0)
ePassword = Entry(myGui,font=("roman",15,"bold"),bd=5, show="*")
ePassword.grid(row=0, column=1)

#====== Strength Check =======


def checkPassword():
    strength = ['Password can not be Blank', 'Very Weak', 'Weak', 'Medium', 'Strong', 'Very Strong']
    score = 1
    password = ePassword.get()
    print(password, len(password))

    if len(password) == 0:
        passwordStrength.set(strength[0])
        return

    if len(password) < 4:
        passwordStrength.set(strength[1])
        return

    if len(password) >= 8:
        score += 1

    if re.search("[0-9]", password):
        score += 1

    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1

    if re.search(".", password):
        score += 1

    passwordStrength.set(strength[score])

passwordStrength = StringVar()
checkStrBtn = Button(myGui, text="Check Strength", bd=4,bg='red',
                     activebackground='black',activeforeground='Red',
                     command=checkPassword, height=2, width=25, font=guiFont)
checkStrBtn.grid(row=2, column=0)
checkStrLab = Label(myGui, textvariable=passwordStrength)
checkStrLab.grid(row=2, column=1, sticky=W)
print("By:- @Er.ShubhamBhagat©®")
myGui.mainloop()
