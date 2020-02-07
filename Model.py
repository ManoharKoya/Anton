import numpy as np

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

def getModel(model):
    if model==-1:
        model = loadGloveModel(file)
    return model