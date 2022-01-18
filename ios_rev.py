
from app_store_scraper import AppStore
import pandas as pd
import numpy as np
import datetime
from datetime import datetime
import json
import re
from time import sleep


lista_site=pd.read_csv("C:/Users/antfiera/Documents/GitHub/app-store_reviews_crawler/in-ios.csv")
#lista_site1=lista_site.str.split('/', expand=True)
print(lista_site)
#print (len(lista_site))

all_data = pd.DataFrame()

aplicatii=lista_site['app']
iduri=lista_site['id']


#print(iduri[1])
i=0
while i < len(lista_site) :
        reviews_all = AppStore(country="ro", 
                             app_name=aplicatii[i], 
                             app_id=iduri[i], 
                             #log_interval=10,
                             )
        reviews_all.review(sleep=3)
        reviews_all.reviews
        scrapeddata=pd.DataFrame.from_dict(reviews_all.reviews)
        scrapeddata["appl"]=aplicatii[i]
        scrapeddata["cules la"]=datetime.now()
        all_data = all_data.append(scrapeddata)   
        sleep(2)
        i+=1
        
#print(all_data)
all_data.index.name='id'


'''
t=str(datetime.now())
t1=t.replace(".","_")
t2=t1.replace("-","-")
t3=t2.replace(":","_")
t4=t3.replace(" ","-")
t5=t4[0:19]
'''
all_data.to_excel("C:/Users/antfiera/Documents/GitHub/app-store_reviews_crawler/ios_app_reviews.xlsx")