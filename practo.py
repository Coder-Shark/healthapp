import requests as r
from bs4 import BeautifulSoup
import html5lib
re=r.get('https://www.practo.com/search?results_type=doctor&q=%5B%7B%22word%22%3A%22Pediatric Dermatologist%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%2C%7B%22word%22%3A%22Chethipuzha%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22locality%22%7D%5D&city=Kottayam')
so=BeautifulSoup(re.content,'html5lib')
a=so.find_all('div',class_="u-border-general--bottom")


for i in range(0,len(a)):
    try:
        c=a[i].find('div',class_="listing-doctor-card")
        d=c.find('div',class_="info-section")
        url="https://www.practo.com"+d.find('a')['href']
        name=d.find('a').getText()
        try:
            recurreq=r.get(url)
            sop=BeautifulSoup(recurreq.content,'html5lib')
            add=sop.find('p',class_="c-profile--clinic__address").getText()
        except:
            pass    
        f=d.find_all('div',class_="u-grey_3-text")
        proff=f[0].find('h3').getText()

        h=d.find_all('div',class_="uv2-spacer--sm-top")
        print(name)
        print(url)
        print(h[0].getText())
        print(add)
        print(proff)
        print('-+-+-+-+-+-+-+-+-+-+-+')
    except:
        pass
