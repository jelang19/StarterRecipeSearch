import requests
import csv
from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import PorterStemmer
import pandas as pd
import pickle as pkl
import numpy as np
import json
import copy

f = open("recipeData/spoonacularRecDetails.txt", "r")
fileText = f.read()
f.close()

parsed = json.loads(fileText)

featVals = []
maxLen = 0

for d in parsed:
    recVals = []
    valsList = d.values()
    for val in valsList:
        if (type(val) == list):
            for i in val:
                recVals.append(i)
        else:
            recVals.append(val)
    featVals.append(copy.copy(recVals))
    if (len(recVals) > maxLen):
        maxLen = len(recVals)

print(maxLen)

for row in featVals:
    oldLen = len(row)

# featValsArr = np.array(featVals)

# keepFeatVals = featValsArr[:, 2:5]

# print(keepFeatVals[0])

# testLabels = []