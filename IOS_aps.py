#!/usr/bin/env python
# coding: utf-8

# ### Imports

from bs4 import BeautifulSoup
import requests 
import pandas as pd
import datetime
from datetime import datetime

# docs
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find


# HTTP Request


# store website in a variable
app_site='my-vodafone-romania/id468772675'

def IOS_APP(site):

    website = 'https://apps.apple.com/ro/app/'+site
    
    response = requests.get(website)
    
    # check status code 200 este ok
    response.status_code
    
    # ### Soup Object
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    
    #print(soup) #arata siteul
    
    #extrage ratingul general si #ratings total
    r = soup.find(class_ = 'we-rating-count star-rating__count').get_text()
    r=r.split()
    ratings=[r[0],r[2]]
    ratings
    
    #extrage pretul
    price = soup.find(class_ = 'inline-list__item inline-list__item--bulleted app-header__list__item--price').get_text()
    price
    
    #extrage categoria
    category = soup.find_all(class_ = "inline-list__item")[0].get_text().strip()
    category=category.split()
    category=category[-1]
    category
    
    
    
    # extrage procentele ratings - histograma
    h = soup.find_all(class_ = 'we-star-bar-graph__bar__foreground-bar')
    h
    
    
    #curata si pune datele de histo in lista
    histo=[]
    b=[]
    for w in h :
        histo.append(w.get('style'))
    #print(a)
    b.append(site)
    for s in histo:
        c=s.replace("width: " , "")
        d=c.replace(";" , "")
        b.append(d)
    #b.append(ratings)
    b
    
    #ompleteaza lista de la histograa cu celelalte informatii
    b.append(ratings[0])
    b.append(ratings[1])
    b.append(price)
    b.append(category)
    #b.append(site)
    
    
    #genereaza capul de tabel
    header=['site','1*','2*','3*','4*','5*', 'avg ratings', 'total ratings', 'price','category']
    #len(header)
    
    #Transforma lista in dataframe
    df=pd.DataFrame(b)
    #df
    
    #transpune dataframe sub forma de tabel
    df1=df.T
    #df1
    
    #adauga la tabel capul de tabel generat aterior
    df1.columns = header
    df1
    
    return df1




lista_site=pd.read_csv("C:/Users/antfiera/Desktop/app-store/in-ios.csv")

lista=pd.DataFrame()

for i in lista_site["app_name"]:
   aaa=IOS_APP(i)
   lista=lista.append(aaa, ignore_index=True)

lista.index.name='id'
t=str(datetime.now())
t1=t.replace(".","_")
t2=t1.replace("-","-")
t3=t2.replace(":","_")
t4=t3.replace(" ","-")
t5=t4[0:19]
print(lista)
lista.to_excel("C:/Users/antfiera/Desktop/app-store/"+t5+"-ios-apps.xlsx", index = True) 