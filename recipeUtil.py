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

def convToCSV(recDictsList, fileName):
    keys = recDictsList[0].keys()

    with open('recipeData/' + fileName + '.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(recDictsList)

def getBoolVal(bVal):
    if (bVal == "True"):
        return 1
    else:
        return 0

def extractMetrics(recDictList):
    #avgReadyTime, avgPrep, avgCook, %gluten, %fodmap, %vegan, %vegetarian, %healthy, %popular, avgNumSteps, avgNumIngrs, common ingrs
    metricsDict = {"readyTimeSum": 0, "avgPrepTime": 0, "avgCookTime": 0, "numGlutenFree": 0, "numLowFodmap": 0, "numVegan": 0,
                   "numVegetarian": 0, "numHealthy": 0, "numPopular": 0, "numStepsSum": 0, "numIngrsSum": 0}
    totalRecsUsed = len(recDictList)

    for rec in recDictList:
        metricsDict["readyTimeSum"] += rec["readyInMins"]
        if (rec["numSteps"] != 'None'):
            metricsDict["numStepsSum"] += rec["numSteps"]
        else:
            metricsDict["numStepsSum"] += rec["numIngrs"]

        metricsDict["numIngrsSum"] += rec["numIngrs"]

        metricsDict["numGlutenFree"] += getBoolVal(rec["glutenFree"])
        metricsDict["numLowFodmap"] += getBoolVal(rec["lowFodmap"])
        metricsDict["numVegan"] += getBoolVal(rec["vegan"])
        metricsDict["numVegetarian"] += getBoolVal(rec["vegetarian"])
        metricsDict["numHealthy"] += getBoolVal(rec["veryHealthy"])
        metricsDict["numPopular"] += getBoolVal(rec["veryPopular"])
    
    # print(metricsDict)
    calcMetricsDict = {"avgTimeSum": 0, "percentGlutenFree": 0, "percentLowFodmap": 0, "percentVegan": 0,
                   "percentVegetarian": 0, "percentHealthy": 0, "percentPopular": 0, "avgStepsSum": 0, "avgIngrsSum": 0}
    calcMetricsDict["avgTimeSum"] = metricsDict["readyTimeSum"] / float(totalRecsUsed)
    calcMetricsDict["avgStepsSum"] = metricsDict["numStepsSum"] / float(totalRecsUsed)
    calcMetricsDict["avgIngrsSum"] = metricsDict["numIngrsSum"] / float(totalRecsUsed)
    calcMetricsDict["percentGlutenFree"] = metricsDict["numGlutenFree"] / float(totalRecsUsed)
    calcMetricsDict["percentLowFodmap"] = metricsDict["numLowFodmap"] / float(totalRecsUsed)
    calcMetricsDict["percentVegan"] = metricsDict["numVegan"] / float(totalRecsUsed)
    calcMetricsDict["percentVegetarian"] = metricsDict["numVegetarian"] / float(totalRecsUsed)
    calcMetricsDict["percentHealthy"] = metricsDict["numHealthy"] / float(totalRecsUsed)
    calcMetricsDict["percentPopular"] = metricsDict["numPopular"] / float(totalRecsUsed)

    for key in calcMetricsDict.keys():
        calcMetricsDict[key] = round(calcMetricsDict[key], 2)

    print(calcMetricsDict)

def findRecsWithIngrs(recDictList, ingrsList, minReadyTime, maxReadyTime):
    goodList = []

    for d in recDictList:
        for ingr in ingrsList:
            if ((d["ingrList"].count(ingr) > 0) and 
                ((d['readyInMins'] <= maxReadyTime) and (d['readyInMins'] >= minReadyTime))):
                goodList.append(recDictList.index(d))  

    print(goodList)

def findIdxIngrsByStr(recDictList, searchTerm):
    recIdxWithTermDict = {}
    
    for i in range(len(recDictList)):
        for ingr in recDictList[i]["ingrList"]:
            if (ingr.count(searchTerm) > 0):
                if ingr not in recIdxWithTermDict:
                    recIdxWithTermDict[ingr] = 1
                else:
                    recIdxWithTermDict[ingr] += 1
                
                

    print(recIdxWithTermDict)