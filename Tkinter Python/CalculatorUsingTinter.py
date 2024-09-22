# importing modules
from tkinter import *
from math import *

# creating Tk() instance
root=Tk()
root.title('Calculator')
root.geometry('400x400')
root.minsize(375,310)
root.maxsize(375,310)
# functions 
def sc(event):
    pass
def click():
    pass

# widget place
variable=StringVar()
e=Entry(root,bg='powder blue',borderwidth=10,bd=15,relief=SUNKEN,width=31,font='comicsansms 15 bold').grid(row=0,column=0,columnspan=5)

# creating buttons
btn=Button(root,text="log",pady=5,padx=27,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=3,column=0)
btn.bind("<Button-1>",sc)
btn=Button(root,text="ln",pady=5,padx=27,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=3,column=1)
btn.bind("<Button-1>",sc)
btn=Button(root,text="(",pady=5,padx=27,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('(')).grid(row=3,column=2)
btn=Button(root,text=")",pady=5,padx=27,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click(')')).grid(row=3,column=3)
btn=Button(root,text=".",pady=5,padx=27,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('.')).grid(row=3,column=4)

# buttons second row
btn=Button(root,text="^",pady=5,padx=33,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=4,column=0)
btn=Button(root,text="deg",pady=5,padx=20,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=4,column=1)
btn=Button(root,text="sin",pady=5,padx=20,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=4,column=2)
btn=Button(root,text="cos",pady=5,padx=20,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=4,column=3)
btn=Button(root,text="tan",pady=5,padx=20,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=4,column=4)

# button for back and others
btn=Button(root,text="sqrt",pady=5,padx=25,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=5,column=0)
btn.bind("<Button-1>",sc)
btn=Button(root,text="c",pady=5,padx=29,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=5,column=1)
btn=Button(root,text="Bksp",pady=5,padx=14,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=5,column=2)
btn=Button(root,text="mod",pady=5,padx=16,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=5,column=3)
btn.bind("<Button-1>",sc)
btn=Button(root,text="/",pady=5,padx=28,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('/')).grid(row=5,column=4)
# button number1
btn=Button(root,text="x!",pady=5,padx=30,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=6,column=0)
btn.bind("<Button-1>",sc)
btn=Button(root,text="7",pady=5,padx=30,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('7')).grid(row=6,column=1)
btn=Button(root,text="8",pady=5,padx=26,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('8')).grid(row=6,column=2)
btn=Button(root,text="9",pady=5,padx=27,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('9')).grid(row=6,column=3)
btn=Button(root,text="*",pady=5,padx=27,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('*')).grid(row=6,column=4)
# button number2
btn=Button(root,text="1/x",pady=5,padx=26,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=7,column=0)
btn.bind("<Button-1>",sc)
btn=Button(root,text="4",pady=5,padx=30,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('4')).grid(row=7,column=1)
btn=Button(root,text="5",pady=5,padx=26,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('5')).grid(row=7,column=2)
btn=Button(root,text="6",pady=5,padx=27,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('6')).grid(row=7,column=3)
btn=Button(root,text="-",pady=5,padx=27,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('-')).grid(row=7,column=4)
# button number3
btn=Button(root,text="pi",pady=5,padx=30,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=8,column=0)
btn=Button(root,text="1",pady=5,padx=30,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('1')).grid(row=8,column=1)
btn=Button(root,text="2",pady=5,padx=26,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('2')).grid(row=8,column=2)
btn=Button(root,text="3",pady=5,padx=27,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('3')).grid(row=8,column=3)
btn=Button(root,text="+",pady=5,padx=27,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('+')).grid(row=8,column=4)
# button evaluation
btn=Button(root,text="qrt",pady=5,padx=30,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=9,column=0)
btn.bind("<Button-1>",sc)
btn=Button(root,text="e",pady=5,padx=30,bg='powder blue',fg='black',font='comicsansms 10 bold').grid(row=9,column=1)
btn.bind("<Button-1>",sc)
btn=Button(root,text="0",pady=5,padx=26,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('0')).grid(row=9,column=2)
btn=Button(root,text="=",pady=5,padx=27,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('=')).grid(row=9,column=3)
btn=Button(root,text="%",pady=5,padx=27,bg='powder blue',fg='black',font='comicsansms 10 bold',command=lambda:click('%')).grid(row=9,column=4)
root.mainloop()
