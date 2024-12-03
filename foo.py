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
import recipeUtil as recUt

f = open("recipeData/spoonacularRecDetails.txt", "r")
fileText = f.read()
f.close()

parsed = json.loads(fileText)
parsedLen = len(parsed)

print("\nIdeal Recipes")
ingrList = ["chicken breast", "chicken", "chicken breasts", "roast chicken", "egg", "eggs", "brown rice", "rice"]
recUt.findRecsWithIngrs(parsed, ingrList, 0, 30)

print("\nNext Range Recipes")
ingrList = ["chicken breast", "chicken", "chicken breasts", "roast chicken", "egg", "eggs", "brown rice", "rice"]
recUt.findRecsWithIngrs(parsed, ingrList, 31, 40)

# recUt.findIdxIngrsByStr(parsed, "rice")

