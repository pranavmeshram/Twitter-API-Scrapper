#!/usr/bin/env python
# coding: utf-8


# ### AngelList Twitter Scrapping


import csv                    #comes in-build with python
import tweepy                 #run cmd -> "pip install tweepy" if not installed.
import pandas as pd           #run cmd -> "pip install pandas" if not installed.

auth = tweepy.OAuthHandler('yvU1l3ePlCjo8MAnNiMguvnVc', 'xJejOubYQB64FUUR5kpoV1MhMcEh0tIyx0KcjQYuw9Ce6n9uR7')
auth.set_access_token('1362676910086516736-Bhjk7ZhKnLXbUALdUnsAyQCKFt1z2p','fLzADTA5b6bhIKFqGC2ibYhpLQfcV2MfFzIMdY9Wvxwpr')

api = tweepy.API(auth)


filename = "test.csv"
with open(filename, 'w') as csvfile:
    
    # Table headings  
    fields = ['Name', 'Text']
    
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile) 
    
    # writing the fields  
    csvwriter.writerow(fields)  
    
    for tweet in tweepy.Cursor(api.user_timeline, id="AngelList").items(20): #Mentioned user timeline tweets for first 20 items.
        if tweet.entities.get('user_mentions'): # to check if there are any users mentioned
            
            for item in tweet.entities.get('user_mentions'):  #iterating the tweets so that each tweet is fetch and stored in the file   
                rows = [ [item.get('screen_name'), "   ",tweet.text.encode('utf-8'),]]  # table rows of csv file  
                
                # writing the rows in the file
                csvwriter.writerows(rows) 
    else:
        print("File with tweets has been created")
        
        
df = pd.read_csv("test.csv") 
print(df)





