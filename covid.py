import requests


def covid(state):
    r=requests.get('https://api.covid19india.org/zones.json')
    print(r.text)
covid("ads")    