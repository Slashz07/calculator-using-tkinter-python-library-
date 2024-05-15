from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.configure(background="grey")

inputBar=Entry(root,width=55,borderwidth=3,background="light grey")
inputBar.grid(row=0,column=0,padx=10,pady=10,columnspan=4)

def getBtn(btnVal):
  currVal=str(inputBar.get())
  inputBar.delete(0,END)
  inputBar.insert(0,currVal+str(btnVal))
  return

def clearBtn():
  inputBar.delete(0,END)

def addBtn():
    currVal = str(inputBar.get())
    inputBar.delete(0, END)
    inputBar.insert(0, currVal + "+")
def subBtn():
    currVal = str(inputBar.get())
    inputBar.delete(0, END)
    inputBar.insert(0, currVal + "-")
def mulBtn():
    currVal = str(inputBar.get())
    inputBar.delete(0, END)
    inputBar.insert(0, currVal + "*")
def divBtn():
    currVal = str(inputBar.get())
    inputBar.delete(0, END)
    inputBar.insert(0, currVal + "/")
def decimalBtn():
    currVal = str(inputBar.get())
    inputBar.delete(0, END)
    inputBar.insert(0, currVal + ".")
def setBracketOpen():
    currVal = str(inputBar.get())
    inputBar.delete(0, END)
    inputBar.insert(0, currVal + "(")
def setBracketClose():
    currVal = str(inputBar.get())
    inputBar.delete(0, END)
    inputBar.insert(0, currVal + ")")

def getRes():
    currVal=inputBar.get()
    inputBar.delete(0, END)
    result=eval(currVal)
    inputBar.insert(0,result)

# Create Buttons-->

button_1 = Button(
    root, background="Dark Gray", text=1, padx=40, pady=20, command=lambda: getBtn(1))
button_2=Button(root,background="Dark Gray",text=2,padx=40,pady=20,command=lambda:getBtn(2))
button_3=Button(root,background="Dark Gray",text=3,padx=40,pady=20,command=lambda:getBtn(3))
button_4=Button(root,background="Dark Gray",text=4,padx=40,pady=20,command=lambda:getBtn(4))
button_5=Button(root,background="Dark Gray",text=5,padx=40,pady=20,command=lambda:getBtn(5))
button_6=Button(root,background="Dark Gray",text=6,padx=40,pady=20,command=lambda:getBtn(6))
button_7=Button(root,background="Dark Gray",text=7,padx=40,pady=20,command=lambda:getBtn(7))
button_8=Button(root,background="Dark Gray",text=8,padx=40,pady=20,command=lambda:getBtn(8))
button_9=Button(root,background="Dark Gray",text=9,padx=40,pady=20,command=lambda:getBtn(9))
button_0=Button(root,background="Dark Gray",text=0,padx=40,pady=20,command=lambda:getBtn(0))
button_decimal = Button(
    root, background="#C7C7C7", text=".", padx=40, pady=20, command=decimalBtn
)

button_clear = Button(
    root, background="#4285F4", text="Clear", padx=78, pady=20, command=clearBtn
)
button_bracOpen = Button(
    root, background="Light Blue", text="(", padx=42, pady=20, command=setBracketOpen
)
button_bracClose = Button(
    root, background="Light Blue", text=")", padx=42, pady=20, command=setBracketClose
)

button_equal = Button(
    root, background="Light Green", text="=", padx=40, pady=20, command=getRes
)
button_add=Button(root,background="Light Blue", text='+',padx=40,pady=20,command=addBtn)
button_subtract=Button(root,background="Light Blue", text='-',padx=40,pady=20,command=subBtn)
button_multiply=Button(root,background="Light Blue", text='*',padx=40,pady=20,command=mulBtn)
button_divide=Button(root,background="Light Blue", text='/',padx=40,pady=20,command=divBtn)

# add Buttons on Screen-->

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_decimal.grid(row=4,column=1)

button_equal.grid(row=4,column=2)
button_add.grid(row=4,column=3)
button_subtract.grid(row=3,column=3)
button_multiply.grid(row=2,column=3)
button_divide.grid(row=1,column=3)

button_clear.grid(row=5,column=0,columnspan=2)
button_bracOpen.grid(row=5,column=2)
button_bracClose.grid(row=5,column=3)

root.mainloop()
