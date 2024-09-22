from tkinter import *
root=Tk()
root.geometry('250x100')
root.title('Button in Tkinter')
button=Button(root,height=3,width=20,
text='SUBMIT',
bg='blue',
fg='yellow',
borderwidth=2,
relief=SUNKEN,
justify='right',
)
button.pack()
root.mainloop()