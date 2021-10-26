import random
from tkinter import *
import tkinter.scrolledtext as scrolledtext
import pyautogui
global str1,str2,str3
def onclick(choice, line):
    when = ['A long time ago', 'Yesterday', 'Before you were born', 'In future', 'Before Thanos arrived']
    who = ['Shazam', 'Iron Man', 'Batman', 'Superman', 'Captain America']
    went = ['Arkham Asylum', 'Gotham City', 'Stark Tower', 'Bat Cave', 'Avengers HQ']
    what = ['He went to eat a lot of cakes', 'He went to fight for justice', 'He went to steal ice cream',
            'He went to dance']
    extraa = ['Then they listen to songs', 'Then they played cricket', 'Then they watched movie',
              'Then they played chess', 'Then they had coffee']
    other = ['After that they sit to study', 'After that they ran away', 'After that they cooked food',
             'After that they quarreled', 'After that they ']

    if (line == 1):
        return (random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + '.' + choice + '.')
    elif (line == 2):
        return (random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + ' ' + random.choice(what) + '.' + choice + '.')
    elif (line == 3):
        return (random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + '.' + random.choice(
            what) + '.' + random.choice(extraa) + '.' + choice + '.')
    elif (line == 4):
        return (random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + '.' + random.choice(
            what) + '.' + random.choice(extraa) + '.' + random.choice(other) + '.' + choice + '.')
# choice = input('Enter the lines you wanna add to story.')
# line = int(input("Enter the number of lines story (1/2/3/4)"))
root=Tk()
root.geometry("1400x980")
root.title("Random Story Generator")
root.minsize(1400,980)
# root.maxsize(1250,980)
frame1=Frame(root,relief="sunken",height="500",width="800")
frame2=Frame(root,bg="grey",relief="sunken",height="200",width="980")
frame1.grid(row=1)
frame2.grid(row=3,ipady=154,column=0,padx=120)
text_entry1=Label(frame1,text="Enter your text",font="comicsansms""bold").grid(row=1,column=2,padx=70,pady=50)
text_entry2=Label(frame1,text="Enter No of lines you want to add",font="comicsansms""bold").grid(row=2,column=2,padx=20,pady=50)
font_size=('normal',16)
window=scrolledtext.ScrolledText(frame2, font = font_size)
window.grid(row=3,column=0)
userText1=StringVar()
userText2=StringVar()
def getText(*args):
    str1=str(userText1.get())
    str2=int(userText2.get())
    str3=onclick(str1,str2)
    window.insert(0.0,str3)
def setval(*args):
    userText1.set("")
    userText2.set("")
    window.delete(1.0,END)
    window.update()
btn1=Button(frame1,text="Generate story")
btn1.grid(row=3,ipadx=10,column=2)
btn1.bind('<Button-1>',getText)
btn2=Button(frame1,text="Reset")
btn2.grid(row=3,ipadx=10,column=7)
btn2.bind('<Button-1>',setval)
userEntry1=Entry(frame1,textvariable=userText1)
userEntry2=Entry(frame1,textvariable=userText2)
userEntry1.grid(row=1,column=4,ipadx=30,ipady=5)
userEntry2.grid(row=2,column=4,ipadx=30,ipady=5)
root.mainloop()