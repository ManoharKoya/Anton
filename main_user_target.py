import tweepy
import time
from ExtractInfo import * 
from context import *
from favCount import * 
from tkinter import *
from keyWords import *
import tkinter as tk
from get_comment import *
import numpy as np
from functools import partial

consumer_key = 'Iuc6ILibSA5CfkDbt7TeWnXZD'
consumer_secret = 'GddSQvkSrnvnJ5jdeUc7ccQmk0nGmPh15o1Qi4bkCSgKzVN7Ix'
access_key = '823567681823522816-zevZd3cbpzej5MQVxxoCxGNh2TlEB33'
access_secret = 'bCZMkGIuwDgHyreBy56842dYySPouD6VKwsx6NC881NKI'
f_name = 'last_trend_id.txt'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api = tweepy.API(auth)

def comment(id1,s):
    s = str(s) 
    print(s)
    api.update_status(s, in_reply_to_status_id = id1, auto_populate_reply_metadata=True)

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

def stalk(user,model):
    print('another time')
    print(user)
    mentions = api.user_timeline(screen_name=user,tweet_mode='recent')
    i = 1
    for j in mentions:
        i = j
        break
    # print(i)
    txt = i.text.lower()
    s = getComment(str(txt),model)
    # ctx = getCxt(str(txt))
    # # print(ctx , 'this is list') 
    # s = ""
    s1 = ""
    # if len(ctx):
    #     s = ExtractInfo(ctx[0]) # remember u got hashtags and names and other in ctx list..
    print("This is the posting comment ---> ",s)
    s1 = s
    # if s:
    #     if len(s)>200 :
    #         s1 = s[0:200]
    #     else :
    #         s1 = s
    # t = extTwitter('bitcoin') # extract info from twitter using #tags search 
    # u = extOther('bitcoin')
    slp0 = 0
    gp1 = fav_time(i.id)
    g = sorted(gp1.items())
    x, y = zip(*g)
    try:
        slp0 = float(x[len(x)-1] - x[0])/float(y[len(y)-1]-y[0])
    except:
        print('continue..')
    
    comment(i.id,str(s1)) # analyze(tweet) 
    #comment(i,t) comment(i,u) -> t,u are extracted infos from other joners..
    gp1 = fav_time(i.id)
    g = sorted(gp1.items())
    x, y = zip(*g)
    slp=0
    try:
        slp = float(x[len(x)-1] - x[0])/float(y[len(y)-1]-y[0])
    except:
        print('continue..')
    r = 0
    slp+=1
    slp0+=1
    print(slp,slp0)
    try:
        r = slp/slp0
    except:
        print('continue..')
    if slp0<slp:
        comment(i.id,"prev comment Influencing the tweet with  "+str(r)+" units")
    if len(hashs):
        for tweet in tweepy.Cursor(api.search,q=hashs[0],count=10,lang="en").items():
            if tweet.id != i.id:
                gp = fav_time(tweet.id)
                g = sorted(gp.items())
                x, y = zip(*g)
                slp1 = 0
                try:
                    slp1 = float(x[len(x)-1] - x[0])/float(y[len(y)-1]-y[0])
                except:
                    print('continue..')
                if(slp1>slp):
                    comment(i.id,'Check @'+tweet.user.screen_name+" 's tweet on "+hashs[0]+' it is more influential than than ur tweet..')
                elif(slp1<slp):
                    comment(i.id,"Ur tweet is more influential than @"+tweet.user.screen_name+" 's tweet on "+hashs[0])
                else :
                    comment(i.id,"Ur tweet is going on par with @"+tweet.user.screen_name+" 's tweet on "+hashs[0])
                break

    
def d(user_entry):
    s = str(user_entry.get())
    stalk(s,model)

if __name__ == '__main__':
    root = Tk()
    root.minsize(200,200)
    user_label = tk.Label(root,text = "enter user name")
    user_entry = tk.Entry(root)
    stalk_buton = tk.Button(root,text = "stalk",command = partial(d,user_entry))
    user_label.pack()
    user_entry.pack()
    stalk_buton.pack()
    root.mainloop()

