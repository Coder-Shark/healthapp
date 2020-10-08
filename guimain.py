import tkinter as tk
from tkinter import *



root= tk.Tk()
root.title('HEATH APP')
root.iconbitmap('D:/pack/ic.ico')



canvas1 = tk.Canvas(root, width = 1000, height = 650,  relief = 'raised')
canvas1.pack()


label9=tk.Label(root,text="⚕",fg="white",bg="red")
label1=tk.Label(root,text="2 Prepare Food Safely",fg="black",bg="yellow")
label2=tk.Label(root,text="4 Wash hands often",fg="black",bg="yellow")
label3=tk.Label(root,text="1 Disinfect Used Surfaces",fg="black",bg="yellow")
label4=tk.Label(root,text="3 Stay Home When Sick",fg="black",bg="yellow")
label5=tk.Label(root,text="5 Don’t Share Personal Items",fg="black",bg="yellow")
label6=tk.Label(root,text="6 Get Vaccinated",fg="black",bg="yellow")
label7=tk.Label(root,text="8 Avoid Touching Wild Animals",fg="black",bg="yellow")
label8=tk.Label(root,text="7 cough & sneeze using a tissue",fg="black",bg="yellow")
label10=tk.Label(root,text="➕",fg="white",bg="red")
                                   
label1.config(font=('jokerman',15))
canvas1.create_window(830,120,window=label1)
label2.config(font=('jokerman',15))
canvas1.create_window(830,250,window=label2)
label3.config(font=('jokerman',15))
canvas1.create_window(130,120,window=label3)
label4.config(font=('jokerman',15))
canvas1.create_window(140,250,window=label4)
label5.config(font=('jokerman',15))
canvas1.create_window(150,380,window=label5)
label6.config(font=('jokerman',15))
canvas1.create_window(830,380,window=label6)
label7.config(font=('jokerman',15))
canvas1.create_window(830,530,window=label7)
label8.config(font=('jokerman',15))
canvas1.create_window(170,530,window=label8)
label9.config(font=('jokerman',45))
canvas1.create_window(500,120,window=label9)
label10.config(font=('jokerman',45))
canvas1.create_window(500,490,window=label10)



label0 = tk.Label(root, text='꧁༒Diseases Wiki༒꧂',fg="black",bg="yellow")
label0.config(font=('algerian', 30))
canvas1.create_window(500, 25, window=label0)

label11 = tk.Label(root, text='Type name of disease:')
label11.config(font=('algerian', 20))
canvas1.create_window(500, 210, window=label11)


entry1 = tk.Entry (root,font=("century schoolbook",15))
canvas1.create_window(500, 250, window=entry1)


def getsrgoogle():
    top=Toplevel()
    top.title('google results are')
    
    bottomframe=Frame(top)
    scroll=Scrollbar(bottomframe)
    scroll.pack(side=RIGHT,fill=Y)
    answer=Text(bottomframe,width=100, height=25,font=("century",13),yscrollcommand=scroll.set,wrap=WORD)
    scroll.config(command=answer.yview)
    answer.pack()
    bottomframe.pack()
    b1=tk.Button(top,text='search database',bg='red',fg='white',font=('century schoolbook',12,'bold'))
    b1.pack()
    b2=tk.Button(top,text='search abc',bg='blue',fg='white',font=('century schoolbook',12,'bold'))
    b2.pack()

    
def getsrwiki():
    top1=Toplevel()
    top1.title('wiki results are')
    
    bottomframe=Frame(top1)
    scroll=Scrollbar(bottomframe)
    scroll.pack(side=RIGHT,fill=Y)
    answer=Text(bottomframe,width=100, height=25,font=("century",13),yscrollcommand=scroll.set,wrap=WORD)
    scroll.config(command=answer.yview)
    answer.pack()
    bottomframe.pack()
    
    b1=tk.Button(top1,text='search database',bg='red',fg='white',font=('century schoolbook',12,'bold'))
    b1.pack()
    b2=tk.Button(top1,text='search abc',bg='blue',fg='white',font=('century schoolbook',12,'bold'))
    b2.pack()

    
def getsrother():
    top2=Toplevel()
    top2.title('other results are')
    

    bottomframe=Frame(top2)
    scroll=Scrollbar(bottomframe)
    scroll.pack(side=RIGHT,fill=Y)
    answer=Text(bottomframe,width=100, height=25,font=("century",13),yscrollcommand=scroll.set,wrap=WORD)
    scroll.config(command=answer.yview)
    answer.pack()
    bottomframe.pack()
    
    b1=tk.Button(top2,text='search database',bg='red',fg='white',font=('century schoolbook',12,'bold'))
    b1.pack()
    b2=tk.Button(top2,text='search abc',bg='blue',fg='white',font=('century schoolbook',12,'bold'))
    b2.pack()


def getsrcredits():
    top3=Toplevel()
    top3.title('CREDITS')
    
    canvas2 = tk.Canvas(top3, width = 600, height = 500,  relief = 'raised')
    canvas2.pack()
    
    label=tk.Label(top3, text='##Owned & Created by##',bg="black",fg="white")
    label.config(font=('algerian', 20))
    canvas2.create_window(300, 80, window=label)
    label1=tk.Label(top3, text=' #Shahin_Sha ',bg="yellow",fg="black")
    label1.config(font=('algerian', 20))
    canvas2.create_window(300, 220, window=label1)
    label2=tk.Label(top3, text=' #Fredy_Somy ',bg="yellow",fg="black")
    label2.config(font=('algerian', 20))
    canvas2.create_window(300, 150, window=label2)
    label3=tk.Label(top3, text=' #Alphin_Benny ',bg="yellow",fg="black")
    label3.config(font=('algerian', 20))
    canvas2.create_window(300, 290, window=label3)
    label4=tk.Label(top3, text=' #Sidharth_M ',bg="yellow",fg="black")
    label4.config(font=('algerian', 20))
    canvas2.create_window(300, 360, window=label4)
    label5=tk.Label(top3, text=' thank you  ',bg="black",fg="white")
    label5.config(font=('algerian', 20))
    canvas2.create_window(300, 480, window=label5)



button1 = tk.Button(text='Google',command=getsrgoogle, bg='brown', fg='white', font=('century schoolbook', 12 , 'bold'))
canvas1.create_window(520, 320, window=button1)

button2= tk.Button(text='Wikipedia',command=getsrwiki,bg='green',fg='white',font=('century schoolbook',12,'bold'))
canvas1.create_window(410,320,window=button2)

button3= tk.Button(text='Other',command=getsrother,bg='blue',fg='white',font=('century schoolbook',12,'bold'))
canvas1.create_window(610,320,window=button3)

k=tk.Button(text="Credits",command=getsrcredits,bg="black",fg="white",font=("century schoolbook",12,"bold"))
canvas1.create_window(960,660,window=k)



button_quit=tk.Label(root,text='----------END OF THE HOMEPAGE----------')
button_quit.config(font=('algerian',15))
button_quit.pack()



root.mainloop()
