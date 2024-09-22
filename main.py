# Program was written by Serhii Skyba

from tkinter import *
from tkinter import messagebox
import random

# Main function
def szyfr():

    # Variables for function
    list = []
    list2 = []
    klucz = keyVar.get()
    wpis = textVar.get()
    wpis = wpis.upper()
    klucz = klucz.upper()

    # Converts text into list of letters
    for i in range (0, len(wpis)):
        lit = wpis[i]
        list.append(lit)
        i=i+1
    i=0
    y=0
    print(list)

    # Main function
    for i in range (0, len(wpis)-1):
        if (list[i] == " "):
            list[i] = " "
            y = y - 1
        if (list[i] != " "):
            if (y >= len(klucz)):
                y = 0
                list[i] = chr(ord(klucz[y]) + (ord(list[i]) - 65))
                if (ord(list[i]) > 90):
                    list[i] = chr(ord(list[i])-26)
            else:
                print(y)
                list[i] = chr(ord(klucz[y]) + (ord(list[i]) - 65))
                if (ord(list[i]) > 90):
                    list[i] = chr(ord(list[i])-26)
        y = y + 1
        i = i + 1
    stra = ''.join(list)
    cipherVar.set(stra)
    print(list)

        

window = Tk()

# GUI Variables
textVar = StringVar() # Text
keyVar = StringVar() # Key
cipherVar = StringVar() # Ciphred text

# GUI Elements
textField_label = Label(window, text="Podaj tekst")
textField_label.pack()
textField = Entry(window, textvariable=textVar)
textField.pack()
keyField_label = Label(window, text="Podaj klucz")
keyField_label.pack()
keyField = Entry(window, textvariable=keyVar)
keyField.pack()
submitButton = Button(window, text="Rób", command=lambda:szyfr())
submitButton.pack()
resultText = Label(window, textvariable=cipherVar)
resultText.pack()

window.mainloop()