import tkinter
from time import strftime

root=tkinter.Tk()
root.title('Digital Clock')
root.geometry('495x116')

def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

label=tkinter.Label(root,font=('ds-digital',80),background='black',foreground='cyan')
label.pack(anchor='center')

time()

tkinter.mainloop()
