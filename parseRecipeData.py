import json
import csv
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier
import copy
import pickle as pkl
import random
import recipeUtil as recUt

featWeights = [0.4, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.4, 0.4, 0.8]

def transformFeats(dictList):
    parsedLen = len(dictList)
    featVals = []
    maxLen = 0

    f = open("recipeData/ingrList.json", "r")
    ingrList = json.load(f)
    f.close()  

    #first turn ingredients into IDs
    for i in range(len(dictList)):
        dictList[i]["ingrListIDs"] = []
        for ingr in dictList[i]["ingrList"]:
            ingrID = ingrList.index(ingr)
            dictList[i]["ingrListIDs"].append(ingrID)
        dictList[i].pop("ingrList")
        dictList[i].pop("diets")
        dictList[i].pop("cuisines")

    ingrStartIndex = 0
    #take out values from dict and put into array
    for d in dictList:
        recVals = []
        valsList = d.values()
        for val in valsList:
            if (type(val) == list):
                ingrStartIndex = len(recVals)
                for i in val:
                    recVals.append(i)
            else:
                recVals.append(val)
        featVals.append(copy.copy(recVals))
        if (len(recVals) > maxLen):
            maxLen = len(recVals)
    
    print(ingrStartIndex)
    print(dictList[0])

    evenFeatsArr = np.full((parsedLen, maxLen), None)

    # set all the array rows to the same amount of columns
    i = 0
    j = 0
    for featRow in featVals:
        j = 0
        for featVal in featRow:
            if (featVal == "True"):
                print("true")
                evenFeatsArr[i][j] = True
            elif (featVal == "False"):
                evenFeatsArr[i][j] = False
            elif (featVal == "None"):
                evenFeatsArr[i][j] = None
            else:    
                evenFeatsArr[i][j] = str(featVal)
            j += 1
        i += 1
        break
        # evenFeatsArr[i] = np.reshape(featVals[i], )
        

    return evenFeatsArr

def transformFeatsNoIngr(recList):
    dictList = copy.deepcopy(recList)
    parsedLen = len(dictList)
    # featVals = []
    maxLen = 0

    # print(dictList[0])
    featVals = np.full((parsedLen, 16), None)

    for i in range(len(dictList)):
        recVals = []
        dictList[i].pop("diets")
        dictList[i].pop("ingrList")
        dictList[i].pop("cuisines")

        if (dictList[i]["cookMins"] == "None"):
            dictList[i]["cookMins"] = dictList[i]["readyInMins"] / 2
        if (dictList[i]["prepMins"] == "None"):
            dictList[i]["prepMins"] = dictList[i]["readyInMins"] / 2
        if (dictList[i]["numSteps"] == "None"):
            dictList[i]["numSteps"] = dictList[i]["numIngrs"]
            
        valsList = dictList[i].values()

        j = 0
        for val in valsList:
            if (val == "True"):
                featVals[i][j] = 1
            elif (val == "False"):
                featVals[i][j] = 0
            else:
                featVals[i][j] = val
            j += 1
        # featVals.append(copy.copy(recVals))
        # if (len(recVals) > maxLen):
        #     maxLen = len(recVals)

    # print(featVals[0])
    # print(len(featVals[0]))
    return featVals

def idIngredients(recList):
    dictList = copy.deepcopy(recList)

    # f = open("recipeData/ingrList.txt")
    # ingrResponse = f.read()
    # f.close()

    # ingrList = ingrResponse.json()    
    repeatCount = 0
    ingrList = []

    for recipe in dictList:
        for ingr in recipe["ingrList"]:
            if (ingrList.count(ingr) == 0):
                ingrList.append(ingr)
            else:
                repeatCount += 1
    
    f = open("recipeData/ingrList.json", "w")
    json.dump(ingrList, f)
    f.close()

def getIngrs(recList):
    dictList = copy.deepcopy(recList)
    parsedLen = len(dictList)

    featVals = []
    ingrList = []
    maxLen = 0

    ingrList = np.full((parsedLen, 25), None)

    f = open("recipeData/ingrList.json", "r")
    allIngrList = json.load(f)
    f.close()  

    k = 0
    #first turn ingredients into IDs
    for i in range(len(dictList)):#
        k = 0
        for j in range(25):
            ingrID = allIngrList.index(dictList[i]["ingrList"][k])
            ingrList[i][j] = ingrID
            k += 1

            if (k == (len(dictList[i]["ingrList"]))):
                k = 0
    
    return ingrList

def getNaiveBayesIngrsPredictions(xAllFeats, xTrainFeats, yTargets):
    clf = MultinomialNB()
    clf.fit(xTrainFeats, yTargets)

    # print(xAllFeats)

    predictedVals = clf.predict(xAllFeats)
    posVals = []

    # print(predictedVals)
    # print(len(predictedVals))

    predictProbs = clf.predict_proba(xAllFeats)
    
    f = open("recipeData/predictProbs.txt", "w")
    for row in predictProbs:
        for val in row:
            f.write("%f," % val)
        f.write("\n")
    f.close()

    for i in range(len(predictedVals)):
        if (predictedVals[i] == 1):
            posVals.append(i)

    # print(posVals)

    f = open("recipeData/spoonacularRecDetails.txt", "r")
    fileText = f.read()
    f.close()

    parsed = json.loads(fileText)

    posRecDictList = []
    for valIndex in posVals:
        posRecDictList.append(parsed[valIndex])

    f = open("recipeData/predictedRecipesIngrs.json", "w")
    json.dump(posRecDictList, f)
    f.close()

    # print(posRecDictList)
    # print(len(posRecDictList))

    return predictedVals

f = open("recipeData/spoonacularRecDetails.txt", "r")
fileText = f.read()
f.close()

parsed = json.loads(fileText)
parsedLen = len(parsed)

idIngredients(parsed)

featsArr = transformFeatsNoIngr(parsed)

#remove ID and link
x = featsArr[:, 2:]

posTrainingIdxs = [10,17,159,164,164,211,227,251,334,353,355,378,380,380,388,390,390,407,479,479,522,551,564,577,585,601]
nextTrainIdxs = [3, 371, 470, 477, 548, 643]
y = []
trainIdxs = [] + posTrainingIdxs + nextTrainIdxs

for i in range(len(trainIdxs)):
    if (i < len(posTrainingIdxs)):
        y.append(1)
    else:
        y.append(2)

avoidClassCount = len(trainIdxs) * 2
for i in range(avoidClassCount):
    randIndx = random.randint(0, len(x))
    # pick random int, make sure it isn't already in the index array
    if (posTrainingIdxs.count(randIndx) == 0):
        trainIdxs.append(randIndx)
        y.append(0)
    else:
        i -= 1

# print(trainIdxs)
# print(y)

xIngr = getIngrs(parsed)
xIngrTrain = xIngr[trainIdxs, :]

print("ingredients")
print(xIngrTrain[:4])
print()

predictedYs = getNaiveBayesIngrsPredictions(xIngr, xIngrTrain,y)

#add in ingrpredict column to x data
xNew = np.column_stack((x, predictedYs))
# print(xNew)

xTrain = xNew[trainIdxs, :]

clf = AdaBoostClassifier()
clf.fit(xTrain, y)

predictedRecs = clf.predict(xNew)
predictRecProbs = clf.predict_proba(xNew)
for i in range(len(predictedRecs)):
    if (posTrainingIdxs.count(i) > 0):
        parsed[i]['origClass'] = 1
    elif (nextTrainIdxs.count(i) > 0):
        parsed[i]['origClass'] = 2
    else:
        parsed[i]['origClass'] = 0

    parsed[i]['PredictedClass'] = predictedRecs[i]
    for t in range(3):
        keyStr = "ProbClass%d" % t
        parsed[i][keyStr] = predictRecProbs[i][t]

# print(parsed)

recUt.convToCSV(parsed, "predictedRecs")


# Get metrics for orig vs predicted ideal class values
recommendRecsList = []
for rec in parsed:
    if (rec["PredictedClass"] == 1):
        recommendRecsList.append(rec)

print(len(recommendRecsList))

recUt.extractMetrics(recommendRecsList)

npParsed = np.array(parsed)
recList = npParsed[posTrainingIdxs]
recUt.extractMetrics(recList)

# Get metrics for orig vs predicted next class values

nextRecsList = []
for rec in parsed:
    if (rec["PredictedClass"] == 2):
        nextRecsList.append(rec)

recUt.extractMetrics(nextRecsList)

recList = npParsed[nextTrainIdxs]
recUt.extractMetrics(recList)