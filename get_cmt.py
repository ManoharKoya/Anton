from keyWords import *
from ExtractInfo import *
from sim_score import *

txt = '''
        Keyword extraction is the automated process of extracting the most relevant words and expressions from text.
With more than 290 billion emails sent and received on a daily basis, and half a million tweets posted every single minute, using machines to analyze huge sets of data and extract important information is definitely a game-changer.
'''

def getComment1(keys,model):
    lst_news=[]
    for i in keys:
        s = ExtractInfo(str(i))
        lst_news.append(s)
        print(s)
    sim_scores = []
    for i in lst_news:
        sim_scores.append(simScore(str(txt),str(i),model))
    print(sim_scores)
    idx = 0 
    mx = 0
    mxi = 0
    for i in sim_scores:
        if i>mx:
            mx = i
            mxi = idx
        idx+=1
    return lst_news[mxi]

