import requests as r
from bs4 import BeautifulSoup
import html5lib
r=r.get('https://en.wikipedia.org/wiki/aids')
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
    five=s.find_all('tr')[7]
    fiveo=five.find('th').getText()
    fivet=five.find('td').getText()
    six=s.find_all('tr')[8]
    sixo=six.find('th').getText()
    sixt=six.find('td').getText()
except:
    print("THere has been a tech difficulty")    
print(p)

print("by: \n fredysomy")
