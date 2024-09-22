from tkinter import * 
# using Tk() class
root=Tk()
root.title('Check Box')
root.geometry('600x300')
def run():
    with open('record.txt','a') as f:
        f.write(f"{name_var.get()},{email_var.get()},{phone_var.get()},{gender_var.get()},{check_var.get()}")
        print()

# heading label
Label(root,text='Survey Form',font='comicsansms 18 bold',fg='blue').grid(row=0,column=4) 

# form Label with entry
Label(root,text='Name:',font='comicsansms 18 bold').grid(row=1,column=3)
Label(root,text='Email:',font='comicsansms 18 bold').grid(row=2,column=3)
Label(root,text='Phone:',font='comicsansms 18 bold').grid(row=3,column=3)
Label(root,text='Gender:',font='comicsansms 18 bold').grid(row=4,column=3)
Button(text='SUBMIT',font='comicsansms 13 bold',command=run).grid(row=6,column=4)

# creating variable for Entry
name_var=StringVar()
email_var=StringVar()
phone_var=StringVar()
gender_var=StringVar()
check_var=IntVar()

# creating Entry for label
Entry(root,textvariable=name_var).grid(row=1,column=4)
Entry(root,textvariable=email_var).grid(row=2,column=4)
Entry(root,textvariable=phone_var).grid(row=3,column=4)
Entry(root,textvariable=gender_var).grid(row=4,column=4)


# creating check button
Checkbutton(text='You want to join our organisation?',variable=check_var,font='comicsansms 10').grid(row=5,column=4)

root.mainloop()