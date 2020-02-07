import tweepy
import time
import numpy as np
from ExtractInfo import * 
from context import *
from favCount import * 
from keyWords import *
from get_comment import *
from get_cmt import *


print("wait for it...")

consumer_key = 'Iuc6ILibSA5CfkDbt7TeWnXZD'
consumer_secret = 'GddSQvkSrnvnJ5jdeUc7ccQmk0nGmPh15o1Qi4bkCSgKzVN7Ix'
access_key = '823567681823522816-zevZd3cbpzej5MQVxxoCxGNh2TlEB33'
access_secret = 'bCZMkGIuwDgHyreBy56842dYySPouD6VKwsx6NC881NKI'
f_name = 'last_trend_id.txt'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api = tweepy.API(auth)


def lst_id(file_name):
    f_read = open(file_name,'r')
    id = int(f_read.read().strip())
    f_read.close()
    return id

def insert_lst_id(id,file_name):
    f_write = open(file_name,'w')
    f_write.write(str(id))
    f_write.close()

def comment(tweet,s):
    api.update_status(s, tweet.id)
    return tweet


def loadGloveModel(gloveFile):
    print("Loading Glove Model")
    f = open("glove.6B.50d.txt",'r',encoding="utf8")
    model = {}
    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    print("Done.",len(model)," words loaded!")
    return model

file = "glove.6B.300d.txt"
model = loadGloveModel(file)

def driver(model):
    print('another time')
    lst_trend = lst_id(f_name) 
    print(lst_trend)
    mentions = api.mentions_timeline(lst_trend,tweet_mode='extended')
    # print(mentions[0].__dict__.keys())
    trendId = []
    tag = "#trendme"
    for i in reversed(mentions):
        # print("Favourate count = " , i.favorite_count) 
        txt = i.full_text.lower()
        if tag in txt:
            trendId.append(i.id)
            s = getComment(str(txt),model)
            # ctx = getCxt(str(txt))
            # print(ctx , 'this is list') 
            # s = getComment1(ctx,model) # remember u got hashtags and names and other in ctx list..
            print(s)
            if len(s)>200 :
                s1 = s[0:200]
            else :
                s1 = s
            # t = extTwitter('bitcoin')
            # u = extOther('bitcoin')
            comment(i,s1) # analyze(tweet) 
            #comment(i,t) comment(i,u) -> t,u are extracted infos from other joners..
            fav_time(i.id)
            insert_lst_id(i.id,f_name)


while(True):
    driver(model)
    time.sleep(60)
