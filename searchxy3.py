import tkinter as tk                

from tkinter import *




def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)

    container = tk.Frame(self)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    self.frames = {}
    for F in (StartPage, PageOne, PageTwo):
        page_name = F.__name__
        frame = F(parent=container, controller=self)
        self.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()




def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    canvas1 = tk.Canvas(self, width = 600, height = 700,  relief = 'raised')
    canvas1.pack()
    label9=tk.Label(self,text="⚕️",fg="white",bg="red")
    label1=tk.Label(self,text="2 Handle & Prepare Food Safely",fg="black",bg="yellow")
    label2=tk.Label(self,text="4 Wash hands often",fg="black",bg="yellow")
    label3=tk.Label(self,text="1 Disinfect Commonly Used Surfaces",fg="black",bg="yellow")
    label4=tk.Label(self,text="3 Cough and Sneeze into a Tissue",fg="black",bg="yellow")
    label5=tk.Label(self,text="5 Don’t Share Personal Items",fg="black",bg="yellow")
    label6=tk.Label(self,text="6 Get Vaccinated",fg="black",bg="yellow")
    label7=tk.Label(self,text="8 Avoid Touching Wild Animals",fg="black",bg="yellow")
    label8=tk.Label(self,text="7 Stay Home When Sick",fg="black",bg="yellow")
                                   
    label1.config(font=('jokerman',15))
    canvas1.create_window(700,100,window=label1)
    label2.config(font=('jokerman',15))
    canvas1.create_window(665,220,window=label2)
    label3.config(font=('jokerman',15))
    canvas1.create_window(-120,100,window=label3)
    label4.config(font=('jokerman',15))
    canvas1.create_window(-115,220,window=label4)
    label5.config(font=('jokerman',15))
    canvas1.create_window(-90,380,window=label5)
    label6.config(font=('jokerman',15))
    canvas1.create_window(649,380,window=label6)
    label7.config(font=('jokerman',15))
    canvas1.create_window(698,530,window=label7)
    label8.config(font=('jokerman',15))
    canvas1.create_window(-75,530,window=label8)
    label9.config(font=('jokerman',45))
    canvas1.create_window(300,120,window=label9)
    label = tk.Label(self, text="꧁༒Diseases Search༒꧂",fg='black',bg='yellow')
    label.config(font=('algerian', 30))
    canvas1.create_window(300, 25, window=label)

    label0 = tk.Label(self, text='Type name of disease:')
    label0.config(font=('algerian', 25))
    canvas1.create_window(300, 200, window=label0)

    entry1 = tk.Entry (self,font=("century schoolbook",20))
    canvas1.create_window(300, 240, window=entry1)



    button1 = tk.Button(self, text="Google search",
                            command=lambda: controller.show_frame("PageOne"),bg="brown",fg="white", font=('century schoolbook',15,'bold'))
    canvas1.create_window(300, 300,window=button1)
    button2 = tk.Button(self, text="Wikipedia search",
                            command=lambda: controller.show_frame("PageTwo"),bg="blue",fg="white",font=('century schoolbook',15,'bold'))
    canvas1.create_window(300, 350,window=button2)


 



def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    label = tk.Label(self, text="Google results",fg="black",bg="yellow",font=('century schoolbook',10,'bold'))
    label.config(font=('algerian',20))
    label.pack(side="top", fill="x", pady=10)

           
    bottomframe=Frame(self)
    scroll=Scrollbar(bottomframe)
    scroll.pack(side=RIGHT,fill=Y)
    answer=Text(bottomframe,width=140, height=25,font=("century",13),yscrollcommand=scroll.set,wrap=WORD)
    scroll.config(command=answer.yview)
    answer.pack()
    bottomframe.pack()

        
    button = tk.Button(self, text="Go to the Home page",
                           command=lambda: controller.show_frame("StartPage"),font=('century schoolbook',13,'bold'))
    button.pack(side="bottom",fill="x",pady=10)




def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    label = tk.Label(self, text="Wikipedia results", fg="black",bg="yellow",font=('century schoolbook',10,'bold'))
    label.config(font=('algerian',20))
    label.pack(side="top", fill="x", pady=10)
        
    bottomframe=Frame(self)
    scroll=Scrollbar(bottomframe)
    scroll.pack(side=RIGHT,fill=Y)
    answer=Text(bottomframe,width=140, height=25,font=("century",13),yscrollcommand=scroll.set,wrap=WORD)
    scroll.config(command=answer.yview)
    answer.pack()
    bottomframe.pack()


     
     button = tk.Button(self, text="Go to the Home page",
                           command=lambda: controller.show_frame("StartPage"),font=('century schoolbook',13,'bold'))
        
     button.pack(side="bottom",fill="x",pady=10)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
