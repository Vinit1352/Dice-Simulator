import random
from tkinter import * 

root= Tk()
root.geometry("410x300")

l1=Label(root,font=("times",200),bg='red')

def roll():# roll function
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685'] #ascii values associated 1,2,3,4...6 
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')#generates random number over a dice
    l1.pack()

#Button for rolling dice
b1=Button(root,text="Let's roll",command=roll,bg='yellow')
b1.place(x=180,y=0)#posyion of lets roll button
root.mainloop()