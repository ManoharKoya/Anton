# this is to Extract information by almost 4 types after getting context from the tweet text. 

# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')

# # /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# # /v2/sources
# sources = newsapi.get_sources()

from newsapi import NewsApiClient
from GoogleNews import GoogleNews
import pandas as pd


ApiKey = '3ec3227410fa4dc795454ad9c93b41bc'
newsapi = NewsApiClient(api_key=ApiKey)

def ExtractInfo(ctxt):
    top_headlines = newsapi.get_everything(q=ctxt)
    arts = top_headlines['articles']
    # for i in arts:
    #     print(i['description'], i['publishedAt'])
    if len(arts):
        return arts[0]['description']
    else :
        return None






