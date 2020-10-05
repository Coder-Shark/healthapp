import tkinter as tk
from tkinter import *
"""import pycountry
import plotly.express as px
import pandas as pd
import requests as r"""
from bs4 import BeautifulSoup
import html5lib
"""import lxml"""


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='⚕️Diseases wiki⚕️',fg="black",bg="yellow")
label1.config(font=('algerian', 30))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type name of disease:')
label2.config(font=('algerian', 20))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root,font=("century schoolbook",15))
canvas1.create_window(200, 140, window=entry1)



def getSR():
    
    x1 = entry1.get()
    
    label3 = tk.Label(root, text= 'The possible results of ' + x1 + ' is:',font=('century schoolbook', 15))
    canvas1.create_window(200, 210, window=label3)
    
    label4 = tk.Label(root,font=('century', 12, 'bold'))
    canvas1.create_window(200, 230, window=label4)
    
    
    
button1 = tk.Button(text='Search Google',command=getSR, bg='brown', fg='white', font=('century schoolbook', 12 , 'bold'))
canvas1.create_window(100, 180, window=button1)

button1 = tk.Button(text='Search Wikipedia',command=getSR, bg='brown', fg='white', font=('century schoolbook', 12 , 'bold'))
canvas1.create_window(280, 180, window=button1)



bottomframe=Frame(root)
scroll=Scrollbar(bottomframe)
scroll.pack(side=RIGHT,fill=Y)
answer=Text(bottomframe,width=140, height=20,font=("century",13),yscrollcommand=scroll.set,wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()
bottomframe.pack()

button_quit=tk.Label(root,text='******END OF THE PROGRAM****')
button_quit.config(font=('algerian',15))
button_quit.pack()


root.mainloop()
