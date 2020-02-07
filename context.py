# how to get a context from a tweet text.
# 1. format tweet text to normal text.
import nltk
from nltk.tag import pos_tag

names = []
hashs = []

def storeHashName(Ttxt):
    for i in Ttxt.split():
        if i[0]=='#':
            hashs.append(i)
        elif i[0]=='@':
            names.append(i)
    return

def formatTxt(Ttxt):
    Ntxt = ""
    storeHashName(Ttxt)
    for i in Ttxt:
        if i!='@' and i!='#' and i!='\n':
            Ntxt+=i
    return Ntxt

def getCxt(txt):
    ftxt = formatTxt(txt)
    print(ftxt)
    sp = nltk.word_tokenize(ftxt)
    print(sp)
    tagged = pos_tag(sp)
    print(tagged)
    p = []
    for i in tagged:
        if i[1]=='NN' or i[1]=='NNS' or i[1]=='NNP' or i[1]=='JJ':
            p.append(i[0])
    return p

# Ttxt = '''That was Amazing Fun !!! Singing RAJA KAIYA VACCHA along with Dear brother @thisisysr
#  at #SRGMP
# Thaanku for the Super Time 
# @ZeeTamil
#  Keep Rocking 😁🎹🎶🎵'''


# p = getCxt(Ttxt)

# print(p)
# print(hashs)
# print(names)





