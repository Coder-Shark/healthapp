import requests
from bs4 import BeautifulSoup
import html5lib

def googleapi():
   
    d=str(pg)
    dd={}
    l=[]
    url="https://www.google.com/search?q="+s+"&start="+d+"&sa=N&ved=2ahUKEwi7_fTxvcPrAhUy6XMBHahXAuc4ChDy0wN6BAgLEC8&biw=1600&bih=757"
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
                gh={"url":x,"desc":desc,"desc2":desc2}
                l=l+[gh]
            except:
                u=g.find('a')['href']
                x=u.split('&')[0]
                gh={"url":x,"desc":desc,"desc2":desc2}
                l=l+[gh]
                
        except:
            print()
    return l