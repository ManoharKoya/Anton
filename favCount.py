import tweepy
import time
import matplotlib.pylab as plt

consumer_key = 'Iuc6ILibSA5CfkDbt7TeWnXZD'
consumer_secret = 'GddSQvkSrnvnJ5jdeUc7ccQmk0nGmPh15o1Qi4bkCSgKzVN7Ix'
access_key = '823567681823522816-zevZd3cbpzej5MQVxxoCxGNh2TlEB33'
access_secret = 'bCZMkGIuwDgHyreBy56842dYySPouD6VKwsx6NC881NKI'
f_name = 'last_trend_id.txt'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api = tweepy.API(auth)

def driver1(tm,gp):  # testing driver code for plotting a time vs fav_count
    while(tm < 10):    
        mentions = api.user_timeline(screen_name='@TimesNow',tweet_mode='recent')
        for j in mentions:
            gp[tm]=j.favorite_count
            print(j.id)
            tm=tm+1 
            break
        print(gp)
        break
        time.sleep(1)
    gp1 = sorted(gp.items()) 
    x, y = zip(*gp1)
    plt.plot(x,y)
    plt.show()

def fav_time(id1): # give the tweet_id & an empty_dictionary as parameters..
    gp = {}
    tm = 0
    while(tm<10):
        mentions = api.get_status(id=id1)
        gp[tm] = mentions.favorite_count
        tm+=1
        time.sleep(1)
    gp1 = sorted(gp.items()) 
    x, y = zip(*gp1)
    plt.plot(x,y)
    plt.show()
    return gp

