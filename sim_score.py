import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import scipy

stopWords = set(stopwords.words('english'))

def preprocess(s):
    words = word_tokenize(s)
    wordsFiltered = []
    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)
    return wordsFiltered


def simScore(s1, s2, model):
    try:
        v1 = []
        for w in preprocess(s1):
            if w in model.keys():
                v1.append(model[w])

        v2 = []
        for w in preprocess(s2):
            if w in model.keys():
                v2.append(model[w])
            
                
        vector_1 = np.mean(v1,axis=0)
        vector_2 = np.mean(v2,axis=0)
        print('vector1 is ',vector_1)
        # vector_1 = np.mean([model[word] for word in preprocess(s1)],axis=0)
        # vector_2 = np.mean([model[word] for word in preprocess(s2)],axis=0)
        cosine = scipy.spatial.distance.cosine(vector_1, vector_2)
        print(cosine)
        print('Word Embedding method with a cosine distance asses that our two sentences are similar to',round((1-cosine)*100,2),'%')
    except:
        return 50.0
    return round((1-cosine)*100,2)

# s1 = "anakin skywalker turns evil."
# s2 = "obi wan kanobi tried to train his aprentice but he turned evil."

# simScore(s1,s2)

