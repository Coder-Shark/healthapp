import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import html5lib


root= tk.Tk()
root.title('HEATH APP')




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




label0 = tk.Label(root, text='꧁༒Diseases Wiki༒꧂',fg="black",bg="yellow")
label0.config(font=('algerian', 30))
canvas1.create_window(500, 25, window=label0)

label11 = tk.Label(root, text='Type name of disease:')
label11.config(font=('algerian', 20))
canvas1.create_window(500, 210, window=label11)


entry1 = tk.Entry (root,font=("century schoolbook",15))
canvas1.create_window(500, 250, window=entry1)


def getsrgoogle():
    srch=entry1.get()
    if entry1.get() == "":
         messagebox.showerror("ERROR","No Internet Connection")
         return None
    else:
        lsd=" "
        url="https://www.google.com/search?q="+entry1.get()+"&start=0&sa=N&ved=2ahUKEwi7_fTxvcPrAhUy6XMBHahXAuc4ChDy0wN6BAgLEC8&biw=1600&bih=757"
        r=requests.get(url)
        soup=BeautifulSoup(r.content,'html5lib')
        f=soup.find('div',id="main")
        for i in range(1,len(f)-1):
            try:
                g=f.find_all(class_='ZINbbc xpd O9g5cc uUPGi')[i]
                desc=g.find(class_="BNeawe vvjwJb AP7Wnd").getText()
                desc2=g.find(class_="BNeawe s3v9rd AP7Wnd").getText()
                
                try:
                    u=g.find('a')['href']
                    x=u.split('&')[0].split('?q=')[1]
                    lsd=lsd+"\n"+desc+"\n"+desc2+"\n"+x+"\n"+"__________________"+"\n"
                    
                except:
                    u=g.find('a')['href']
                    x=u.split('&')[0]
                    gh={"url":x,"desc":desc,"desc2":desc2}
                    l=l+[gh]
                    lsd=lsd+"\n"+desc+"\n"+desc2+"\n"+x+"\n"+"__________________"+"\n"
                    
            except:
                print()


    top=Toplevel()
    top.title('google results are{}'.format(entry1.get()))
    
    bottomframe=Frame(top)
    scroll=Scrollbar(bottomframe)
    scroll.pack(side=RIGHT,fill=Y)
    answer=Text(bottomframe,width=100, height=25,font=("century",13),yscrollcommand=scroll.set,wrap=WORD)
    scroll.config(command=answer.yview)
    answer.insert(END,lsd)
    answer.pack()
    bottomframe.pack()
    b1=tk.Button(top,text='search database',bg='red',fg='white',font=('century schoolbook',12,'bold'))
    b1.pack()
    b2=tk.Button(top,text='search abc',bg='blue',fg='white',font=('century schoolbook',12,'bold'))
    b2.pack()

    
def getsrwiki():
    ad=entry1.get()
    if entry1.get() == "":
         messagebox.showerror("ERROR","No Internet Connection")
         return None
    else:
        r=requests.get('https://en.wikipedia.org/wiki/{}'.format(entry1.get()))
        so=BeautifulSoup(r.content,'html5lib')
        title=so.find("h1",class_="firstHeading").getText()
        p=so.find_all("p")[2].getText()
        s=so.find('table',class_="infobox")
        f=s.find('tbody')
        try:
            one=s.find_all('tr')[1]
            oneo=one.find('th').getText()
            onet=one.find('td').getText()
            two=s.find_all('tr')[5]
            twoo=two.find('th').getText()
            twot=two.find('td').getText()
            three=s.find_all('tr')[6]
            threeo=three.find('th').getText()
            threet=three.find('td').getText()
            four=s.find_all('tr')[7]
            fouro=four.find('th').getText()
            fourt=four.find('td').getText()
            five=s.find_all('tr')[8]
            fiveo=five.find('th').getText()
            fivet=five.find('td').getText()
            six=s.find_all('tr')[9]
            sixo=six.find('th').getText()
            sixt=six.find('td').getText()
            wiki=title+"\n"+"___________"+"\n"+p+"___________"+"\n"+oneo+"--"+onet+"\n"+twoo+"--"+twot+"\n"+threeo+"--"+threet+"\n"+fouro+"--"+fourt+"\n"+fiveo+"--"+fivet+"\n"+sixo+"--"+sixt+"\n"+"_____________"
        except:
            wiki="There has been a error"    


    top1=Toplevel()
    top1.title('wiki results are')

    bottomframe=Frame(top1)
    scroll=Scrollbar(bottomframe)
    scroll.pack(side=RIGHT,fill=Y)
    answer=Text(bottomframe,width=100, height=25,font=("century",13),yscrollcommand=scroll.set,wrap=WORD)
    scroll.config(command=answer.yview)
    answer.insert(END,wiki)
    answer.pack()
    
    bottomframe.pack()
    def addfile():
        s=ad+".txt"
        fd=open(s,'w+')
        fd.write(wiki.encode("utf-8"))
        fd.close()
        messagebox.showinfo("SUCESS","{} is cretated and saved".format(s))
    b1=tk.Button(top1,text='search database',bg='red',fg='white',font=('century schoolbook',12,'bold'))
    b1.pack()
    b2=tk.Button(top1,text='search abc',command=addfile,bg='blue',fg='white',font=('century schoolbook',12,'bold'))
    b2.pack()
    

    
def getsrother():
    if entry1.get() == "":
         messagebox.showerror("ERROR","PLease enter something to search")
         return None
    top3=Toplevel()
    top3.title('other results are')
    

    bottomframe=Frame(top3)
    scroll=Scrollbar(bottomframe)
    scroll.pack(side=RIGHT,fill=Y)
    answer=Text(bottomframe,width=100, height=25,font=("century",13),yscrollcommand=scroll.set,wrap=WORD)
    scroll.config(command=answer.yview)
    answer.pack()
    bottomframe.pack()
    
    b1=tk.Button(top3,text='search database',bg='red',fg='white',font=('century schoolbook',12,'bold'))
    b1.pack()
    b2=tk.Button(top3,text='search abc', bg='blue',fg='white',font=('century schoolbook',12,'bold'))
    b2.pack()

def getadoc():
    top2=Toplevel()
    top2.title('Information about the doctor')
    canvas3 = tk.Canvas(top2, width = 600, height = 600,  relief = 'raised')
    canvas3.pack()
    
    b1=tk.Label(top2,text='specialist',bg='red',fg='white')
    b1.config(font=('algerian',20))
    canvas3.create_window(300,100,window=b1)
    
    entry2 = tk.Entry (top2,font=("century schoolbook",15))
    canvas3.create_window(300, 150, window=entry2)
    
    b2=tk.Label(top2,text='location', bg='blue',fg='white')
    b2.config(font=('algerian',20))
    canvas3.create_window(300,250,window=b2)
    
    entry3 = tk.Entry (top2,font=("century schoolbook",15))
    canvas3.create_window(300, 300, window=entry3)

    def getsaloc():
        s1=entry2.get()
        s2=entry3.get()
        if entry2.get() == "" and entry3.get() == "":
            messagebox.showerror("ERROR","PLease enter something to search")
            return None
        else:
            url="https://www.practo.com/search?results_type=doctor&q=%5B%7B%22word%22%3A%22{}%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%2C%7B%22word%22%3A%22{}%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22locality%22%7D%5D&city=Kottayam".format(s1,s2)
            re=requests.get(url)
            so=BeautifulSoup(re.content,'html5lib')
            a=so.find_all('div',class_="u-border-general--bottom")
            addd=" "
            for i in range(0,len(a)):
                try:
                    c=a[i].find('div',class_="listing-doctor-card")
                    d=c.find('div',class_="info-section")
                    url="https://www.practo.com"+d.find('a')['href']
                    name=d.find('a').getText()
                    try:
                        recurreq=requests.get(url)
                        sop=BeautifulSoup(recurreq.content,'html5lib')
                        add=sop.find('p',class_="c-profile--clinic__address").getText()
                        
                    except:
                        pass    
                    f=d.find_all('div',class_="u-grey_3-text")
                    proff=f[0].find('h3').getText()

                    h=d.find_all('div',class_="uv2-spacer--sm-top")   
                    addd=addd+"\n"+name+"\n"+url+h[0].getText()+"\n"+add+"\n"+proff+"\n"+"#######################################"+"\n"
                except:
                    pass   

        top5=Toplevel()
        top5.title('')
      

        bottomframe=Frame(top5)
        scroll=Scrollbar(bottomframe)
        scroll.pack(side=RIGHT,fill=Y)
        answer=Text(bottomframe,width=100, height=25,font=("century",13),yscrollcommand=scroll.set,wrap=WORD)
        answer.insert(END,addd)
        scroll.config(command=answer.yview)
        answer.pack()
        bottomframe.pack()
        def addfileP():
            s=s1+"_in_"+s2+".txt"
            fd=open(s,'w',encoding='utf-8')
            fd.write(addd)
            fd.close()
            messagebox.showinfo("SUCESS","{} is cretated and saved".format(s))
       
        b2=tk.Button(top5,text='Save as Text File',command=addfileP, bg='blue',fg='white',font=('century schoolbook',12,'bold'))
        b2.pack()

    b3=tk.Button(top2,text="Search",command=getsaloc,bg='black',fg='white',font=('century schoolbook',12,'bold'))
    canvas3.create_window(300,400,window=b3)


    
def getsrcredits():
    top4=Toplevel()
    top4.title('CREDITS')
    
    canvas2 = tk.Canvas(top3, width = 600, height = 500,  relief = 'raised')
    canvas2.pack()
    
    label=tk.Label(top4, text='##Owned & Created by##',bg="black",fg="white")
    label.config(font=('algerian', 20))
    canvas2.create_window(300, 80, window=label)
    label1=tk.Label(top4, text=' #Shahin_Sha ',bg="yellow",fg="black")
    label1.config(font=('algerian', 20))
    canvas2.create_window(300, 220, window=label1)
    label2=tk.Label(top4, text=' #Fredy_Somy ',bg="yellow",fg="black")
    label2.config(font=('algerian', 20))
    canvas2.create_window(300, 150, window=label2)
    label3=tk.Label(top4, text=' #Alphin_Benny ',bg="yellow",fg="black")
    label3.config(font=('algerian', 20))
    canvas2.create_window(300, 290, window=label3)
    label4=tk.Label(top4, text=' #Sidharth_M ',bg="yellow",fg="black")
    label4.config(font=('algerian', 20))
    canvas2.create_window(300, 360, window=label4)
    label5=tk.Label(top4, text=' thank you  ',bg="black",fg="white")
    label5.config(font=('algerian', 20))
    canvas2.create_window(300, 480, window=label5)



button1 = tk.Button(text='Google',command=getsrgoogle, bg='brown', fg='white', font=('century schoolbook', 12 , 'bold'))
canvas1.create_window(520, 320, window=button1)

button2= tk.Button(text='Wikipedia',command=getsrwiki,bg='green',fg='white',font=('century schoolbook',12,'bold'))
canvas1.create_window(410,320,window=button2)

button3= tk.Button(text='Other',command=getsrother,bg='blue',fg='white',font=('century schoolbook',12,'bold'))
canvas1.create_window(610,320,window=button3)

button3= tk.Button(text='Consult Doctor',command=getadoc,bg='blue',fg='white',font=('century schoolbook',12,'bold'))
canvas1.create_window(510,500,window=button3)

k=tk.Button(text="Credits",command=getsrcredits,bg="black",fg="white",font=("century schoolbook",12,"bold"))
canvas1.create_window(960,660,window=k)



button_quit=tk.Label(root,text='----------END OF THE HOMEPAGE----------')
button_quit.config(font=('algerian',15))
button_quit.pack()



root.mainloop()
