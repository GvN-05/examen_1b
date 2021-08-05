#!/usr/bin/env python
# coding: utf-8

# In[6]:


#pip install tweepy


# In[7]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


# In[12]:



###API ########################
ckey = "6Ea6KWh9OtUzrWLeCaRMVLuN4"
csecret = "DmW0jFhlmPde3OARqtk9zEelMYJGHO7KOfoFtXjRORH55fGOPD"
atoken = "1418325908956532736-jV1V2gAvpYDdgbWSGFLZJuCr1nysYf"
asecret = "J2eQPBUobPHM8TUrcKF6OyHIJ7ENEB7xz1J4jkxghvcZ6"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
            print("Se guardo con éxito")
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:admin@localhost:5984')
try:
    db = server.create('resultados')
except:
    db = server['resultados']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-74.25909,40.477399,-73.700181,40.916178])  # New York
# twitterStream.filter(track=['bts','black pink'])


# In[ ]:





# In[ ]:




