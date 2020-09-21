from bs4 import BeautifulSoup
import requests
import html5lib

disease = input('note: if the disease has two names connect the names with a hiphen.\nenter the disease which you want find medicine for: ')
if disease == "cancer":
    disease = "malignant-disease"
elif disease == "aids":
    disease = "hiv-infection"
elif disease == "cholesterol":
    disease = "hyperlipidemia"
elif disease == "diabetes":
    disease = "diabetes-mellitus-type-i"
elif disease == "stroke":
    disease = "ischemic-stroke"
elif disease == "glaucoma":
    disease = "glaucoma-open-angle."
elif disease == "stomach-ulcer":
    disease = "gastric-ulcer"
try:
    url = f"https://www.drugs.com/condition/{disease}.html"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html5lib")

    main_class = soup.find("tr", attrs={"class":"condition-table__summary"})
    link = main_class.find("a")

    print(link.text)
except:
    print("Check the keyword written")    
