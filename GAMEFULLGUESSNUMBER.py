from tkinter import*
import random
import time
window=Tk()
window.title("Guess Game")
window.geometry('400x400')
window.configure(bg='black')

logo1 = PhotoImage(file="bingo.png")
logo2 = PhotoImage(file="up.png")
logo3 = PhotoImage(file="down.png")

logo1 = logo1.subsample(5)
logo2 = logo2.subsample(7)
logo3 = logo3.subsample(7)


def restart():
    global a,lblcorrect,txtguess,lblthink,time,b,c
    for i in range(0, 15):
        c = random.randint(0, 100)
        lblthink.config(text=c)
        time.sleep(0.1)
        lblthink.update()

    lblthink.config(text="The number is ready")
    lblcorrect.config(text='',image='')
    txtguess.config(state='normal')
    txtguess.delete(0,END)
    a=random.randint(0,100)
    print(a)

a=random.randint(0,100)
print(a)
def game(event):
    global a , b,intb,guess,txtguess,logo1,logo2,logo3,c
    b=txtguess.get()
    


    if int(b)== a:
        lblcorrect.configure(image=logo1)
        txtguess.config(state='disabled')
    txtguess.delete(0, END)
    if int(b) > a:
        lblcorrect.configure(image=logo3)
        txtguess.delete(0, END)
        lblthink.config(text="")
    if int(b) < a:
        lblcorrect.configure(image=logo2)
        txtguess.delete(0, END)
        lblthink.config(text="")

def exit():
    window.destroy()

lblguess=Label(window,text="Guess the number ",font=('Times',20),bg='black',fg='white')
lblguess.grid(columnspan=2,row=0)

lblinstructions=Label(window,text="You will be asked to guess the number that \nthe computer is thinking ,"
                                  "\n when you think u got the answer\n write it in the text box below \n"
                                  "if your guess is not right\n  you will be shown\n to think about a higher or a lower number \n"
                                 ,
                      font=('Times',13),bg='black',fg='white')

lblinstructions.grid(column=0,columnspan=2,row=1,padx=31)

txtguess=Entry(window,text="",width=7,font=('Times',20),state='disabled',justify=CENTER)
txtguess.grid(column=0,row=3,pady=10)


lblcorrect=Label(window,text=" ",font=('Times',20),bg='black',fg='white')
lblcorrect.grid(column=1,row=3,pady=10)

btnexit=Button(window,text="Exit",width=10,font=('Times',13),command=exit)
btnexit.grid(column=0,row=5,pady=10)

btnrestart=Button(window,text="Restart",width=10,font=('Times',13),command=restart)
btnrestart.grid(column=1,row=5,pady=10)

lblthink=Label(window,text="",font=('Times',20),bg='black',fg='white')
lblthink.grid(column=0,columnspan=2,row=6,pady=10)

for i in range(0, 15):
    c = random.randint(0, 100)
    lblthink.config(text=c)
    time.sleep(0.1)
    lblthink.update()

lblthink.config(text="The number is ready")
lblcorrect.config(text='', image='')
txtguess.config(state='normal')
window.bind('<Return>',game)

window.mainloop()