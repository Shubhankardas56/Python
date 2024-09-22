from tkinter import * 
from math import *

# using the Tk() class create root
root=Tk()
root.title('Calculator')
root.geometry("400x580")
root.minsize(400,545)
root.maxsize(400,545)

# click function
def click(event):
    global outputScreen
    text=event.widget.cget('text')
    # print(text)
    if text=='=':
        if (outputScreen.get()).isdigit():
            value=int(outputScreen.get()) 
        else:
            value=eval(entry.get())
        outputScreen.set(value)
        entry.update()
    elif text=='c':
        outputScreen.set('')
        entry.update()
    else:
        outputScreen.set(outputScreen.get()+text)
        entry.update()
def power(operator):
    global outputScreen
    outputScreen.set(outputScreen.get()+operator)
    entry.update()
    # not working
    # TODO
# def ck(event):
#     screen_value=entry.get()
#     sqroot=str(sqrt(float(screen_value)))
#     entry.delete(0,END)
#     entry.insert(0,sqroot)
#     entry.update()
# creating result screen
outputScreen=StringVar()
outputScreen.set('')
frame=Frame(root,bg="gray",relief=SUNKEN)
entry=Entry(frame,textvar=outputScreen,borderwidth=4,relief=SUNKEN,font='comicsansms 32 bold')
entry.pack(fill=X,pady=20,padx=20)
frame.pack()
# upper part button
frame1=Frame(root,bg="yellow")
button=Button(frame1,text='x',font='comicsansms 32 bold',bg='blue',fg='orange',padx=16,
command=root.destroy)
button.pack(side=LEFT)
button=Button(frame1,text='c',font='comicsansms 32 bold',bg='blue',fg='white',padx=16)
button.bind('<Button-1>',click)
button.pack(side=LEFT)
button=Button(frame1,text='^',font='comicsansms 32 bold',bg='blue',fg='white',padx=16,
command=lambda:power("**"))
button.pack(side=LEFT)
button=Button(frame1,text='√',font='comicsansms 32 bold',bg='blue',fg='white',padx=33)
# button.bind('<Button-2>',ck)
button.pack(side=RIGHT)
frame1.pack(fill='both')
# space for creating button
frame1=Frame(root,bg="yellow")
button=Button(frame1,text='7',font='comicsansms 32 bold',bg='blue',fg='white',padx=16)
button.bind('<Button-1>',click)
button.pack(side=LEFT)
button=Button(frame1,text='8',font='comicsansms 32 bold',bg='blue',fg='white',padx=16)
button.bind('<Button-1>',click)
button.pack(side=LEFT)
button=Button(frame1,text='9',font='comicsansms 32 bold',bg='blue',fg='white',padx=17)
button.bind('<Button-1>',click)
button.pack(side=LEFT)
button=Button(frame1,text='*',font='comicsansms 32 bold',bg='blue',fg='white',padx=33)
button.bind('<Button-1>',click)
button.pack(side=RIGHT)
frame1.pack(fill='both')
# second line button
frame1=Frame(root,bg="yellow")
button=Button(frame1,text='4',font='comicsansms 32 bold',bg='blue',fg='white',padx=16)
button.bind('<Button-1>',click)
button.pack(side=LEFT)
button=Button(frame1,text='5',font='comicsansms 32 bold',bg='blue',fg='white',padx=16)
button.bind('<Button-1>',click)
button.pack(side=LEFT)
button=Button(frame1,text='6',font='comicsansms 32 bold',bg='blue',fg='white',padx=17)
button.bind('<Button-1>',click)
button.pack(side=LEFT)
button=Button(frame1,text='-',font='comicsansms 32 bold',bg='blue',fg='white',padx=34)
button.bind('<Button-1>',click)
button.pack(side=RIGHT)
frame1.pack(fill='both')
# third line button
frame1=Frame(root,bg="yellow")
button=Button(frame1,text='1',font='comicsansms 32 bold',bg='blue',fg='white',padx=16)
button.bind('<Button-1>',click)
button.pack(side=LEFT)
button=Button(frame1,text='2',font='comicsansms 32 bold',bg='blue',fg='white',padx=16)
button.bind('<Button-1>',click)
button.pack(side=LEFT)
button=Button(frame1,text='3',font='comicsansms 32 bold',bg='blue',fg='white',padx=17)
button.bind('<Button-1>',click)
button.pack(side=LEFT)
button=Button(frame1,text='+',font='comicsansms 32 bold',bg='blue',fg='white',padx=29)
button.bind('<Button-1>',click)
button.pack(side=RIGHT)
frame1.pack(fill='both')
# fourth line button
frame1=Frame(root,bg="yellow")
button=Button(frame1,text='0',font='comicsansms 32 bold',bg='blue',fg='white',padx=16)
button.bind('<Button-1>',click)
button.pack(side=LEFT)
button=Button(frame1,text='00',font='comicsansms 23 bold',bg='blue',fg='white',pady=14,padx=16)
button.bind('<Button-1>',click)
button.pack(side=LEFT)
button=Button(frame1,text='.',font='comicsansms 32 bold',bg='blue',fg='white',padx=23)
button.bind('<Button-1>',click)
button.pack(side=LEFT)
button=Button(frame1,text='=',font='comicsansms 32 bold',bg='blue',fg='white',padx=29)
button.bind('<Button-1>',click)
button.pack(side=RIGHT)
frame1.pack(fill='both')

root.mainloop()