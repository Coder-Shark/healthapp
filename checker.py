class Disease:
     def __init__(self, name, symptoms):
         self.name = name
         self.symptoms = symptoms


known_diseases = [
   Disease('cold', set(
     "sore throat|runny nose|congestion|cough|aches".split("|"))
     ),
   Disease('flu', set(
     "fever|headache|muscle aches|returning fever".split("|"))
     ),
   Disease('ebola', set(
     "tiredness|death|bruising|black blood".split("|"))
     ),
   ]


# note: for Python 2, use "raw_input" instead of input
symptoms = input("Please enter symptoms separated by commas: ")
symptoms = symptoms.lower()
symptoms = symptoms.split(",")

possible = []
for symptom in symptoms:
     for disease in known_diseases:
         if symptom in disease.symptoms:
             possible.append(disease.name)

if possible:
     print("You may have these diseases:")
     print(*possible)
else:
     print("Good news! You're going to have a disease named after you!")


import tkinter as tk
from tkinter import *
import pycountry
import plotly.express as px
import pandas as pd
import requests as r
from bs4 import BeautifulSoup
import html5lib
import lxml
import time