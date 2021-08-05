#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument


# In[2]:


db_client = MongoClient()
my_db = db_client.examen
my_posts = my_db.olimpiadas
    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))
response = requests.get("https://www.paho.org/es/temas/coronavirus")
soup = BeautifulSoup(response.content, "lxml")

Course=[]
Provider=[]
Duration=[]
Start_Date=[]
Offered_By=[]
No_Of_Reviews=[]
Rating=[]


post_p = soup.find_all("p", class_="text-align-justify")
post_a=soup.find_all("a", class_="button")

extracted = []
    
for element in post_p:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Course.append(limpio.strip())

for element in post_a:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Provider.append(limpio.strip())


'''
        extracted.append({
            'Course' : post_title['data-track-click'],
            'Duration'  : "",
            'Start_Date':"",
            'Offered_By':"",
            'No_Of_Reviews':"",
            'Rating':""
        })
        '''
'''
    for post in extracted:
        if db_client.my_db.my_posts.find_one({'link': post['link']}) is None:
            print("Found a new listing at the following url: ", post['link'])
            db_client.my_db.my_posts.insert(post)
'''
print(Course)
print(Provider)


# In[3]:


dfDS=pd.DataFrame({'course':Course,'provider':Provider})
out = dfDS.to_dict()
dfDS


# In[ ]:




