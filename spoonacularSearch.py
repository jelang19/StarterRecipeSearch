import requests
import json
import copy

testRecDict = {'id': 715769, 'title': 'Broccolini Quinoa Pilaf', 'readyInMinutes': 30, 'servings': 2, 'sourceUrl': 'https://pickfreshfoods.com/broccolini-quinoa-pilaf/', 'image': 'https://img.spoonacular.com/recipes/715769-556x370.jpg', 'imageType': 'jpg', 'summary': 'Broccolini Quinoa Pilaf requires approximately <b>30 minutes</b> from start to finish. For <b>$4.14 per serving</b>, you get a main course that serves 2. One portion of this dish contains around <b>20g of protein</b>, <b>31g of fat</b>, and a total of <b>625 calories</b>. Head to the store and pick up vegetable broth, onion, olive oil, and a few other things to make it today. A few people made this recipe, and 94 would say it hit the spot. It is a <b>rather expensive</b> recipe for fans of Mediterranean food. It is a good option if you\'re following a <b>gluten free, dairy free, lacto ovo vegetarian, and vegan</b> diet. It is brought to you by Pick Fresh Foods. With a spoonacular <b>score of 98%</b>, this dish is excellent. Similar recipes are <a href="https://spoonacular.com/recipes/spring-broccolini-kale-quinoa-bowls-734866">Spring Broccolini & Kale Quinoa Bowls</a>, <a href="https://spoonacular.com/recipes/orange-sesame-salmon-with-quinoa-broccolini-839832">Orange-Sesame Salmon with Quinoa & Broccolini</a>, and <a href="https://spoonacular.com/recipes/black-pepper-goat-cheese-and-chard-quinoa-with-roasted-broccolini-625829">Black Pepper Goat Cheese and Chard Quinoa with Roasted Broccolini</a>.', 'cuisines': ['Mediterranean', 'Italian', 'European'], 'dishTypes': ['side dish', 'lunch', 'main course', 'main dish', 'dinner'], 'diets': ['gluten free', 'dairy free', 'lacto ovo vegetarian', 'vegan'], 'occasions': [], 'winePairing': {'pairedWines': ['chianti', 'verdicchio', 'trebbiano'], 'pairingText': 'Italian on the menu? Try pairing with Chianti, Verdicchio, and Trebbiano. Italians know food and they know wine. Trebbiano and Verdicchio are Italian white wines that pair well with fish and white meat, while Chianti is a great Italian red for heavier, bolder dishes. One wine you could try is Antinori Badian a Passignano Chianti Classico Gran Selezione. It has 4.6 out of 5 stars and a bottle costs about 60 dollars.', 'productMatches': [{'id': 436674, 'title': 'Antinori Badia a Passignano Chianti Classico Gran Selezione', 'description': 'The wine, one with an important impact, shows an intense ruby red in its tonality. It is complex on the nose with aromas of red berry fruit, raspberries, blackberries, and ripe cherries in addition to its notes of spice and licorice on the finish. The flavors are ripe and sweet and are sustained by substantial tannins, round and ample in support of the supple and velvety structure. Long and persistent, its tonic acidity is a classic characteristic of the Sangiovese cultivated at the Badia a Passignano.', 'price': '$59.99', 'imageUrl': 'https://img.spoonacular.com/products/436674-312x231.jpg', 'averageRating': 0.9200000166893005, 'ratingCount': 9.0, 'score': 0.8843, 'link': 'https://click.linksynergy.com/deeplink?id=*QCiIS6t4gA&mid=2025&murl=https%3A%2F%2Fwww.wine.com%2Fproduct%2Fantinori-badia-a-passignano-chianti-classico-gran-selezione-2008%2F129493'}]}, 'instructions': '<ol><li>In a large pan with lid heat olive oil over medium high heat. Add onions and cook for 1 minute. Add garlic and cook until onions are translucent and garlic is fragrant.</li><li>Add quinoa to pan, stir to combine. Slowly add in broth and bring to a boil.</li><li>Cover and reduce heat to low, cook for 15 minutes.</li><li>In the last 2-3 minutes of cooking add in broccolini on top of the quinoa (do not stir) and cover.</li><li>Uncover and toss broccolini and quinoa together.</li><li>Season to taste with salt and pepper.</li><li>Add walnuts and serve hot.</li></ol>', 'analyzedInstructions': [{'name': '', 'steps': [{'number': 1, 'step': 'In a large pan with lid heat olive oil over medium high heat.', 'ingredients': [{'id': 4053, 'name': 'olive oil', 'localizedName': 'olive oil', 'image': 'olive-oil.jpg'}], 'equipment': [{'id': 404645, 'name': 'frying pan', 'localizedName': 'frying pan', 'image': 'https://spoonacular.com/cdn/equipment_100x100/pan.png'}]}, {'number': 2, 'step': 'Add onions and cook for 1 minute.', 'ingredients': [{'id': 11282, 'name': 'onion', 'localizedName': 'onion', 'image': 'brown-onion.png'}], 'equipment': [], 'length': {'number': 1, 'unit': 'minutes'}}, {'number': 3, 'step': 'Add garlic and cook until onions are translucent and garlic is fragrant.', 'ingredients': [{'id': 11215, 'name': 'garlic', 'localizedName': 'garlic', 'image': 'garlic.png'}, {'id': 11282, 'name': 'onion', 'localizedName': 'onion', 'image': 'brown-onion.png'}], 'equipment': []}, {'number': 4, 'step': 'Add quinoa to pan, stir to combine. Slowly add in broth and bring to a boil.Cover and reduce heat to low, cook for 15 minutes.In the last 2-3 minutes of cooking add in broccolini on top of the quinoa (do not stir) and cover.Uncover and toss broccolini and quinoa together.Season to taste with salt and pepper.', 'ingredients': [{'id': 1102047, 'name': 'salt and pepper', 'localizedName': 'salt and pepper', 'image': 'salt-and-pepper.jpg'}, {'id': 98840, 'name': 'broccolini', 'localizedName': 'broccolini', 'image': 'broccolini.jpg'}, {'id': 20035, 'name': 'quinoa', 'localizedName': 'quinoa', 'image': 'uncooked-quinoa.png'}, {'id': 1006615, 'name': 'broth', 'localizedName': 'broth', 'image': 'chicken-broth.png'}], 'equipment': [{'id': 404645, 'name': 'frying pan', 'localizedName': 'frying pan', 'image': 'https://spoonacular.com/cdn/equipment_100x100/pan.png'}], 'length': {'number': 18, 'unit': 'minutes'}}, {'number': 5, 'step': 'Add walnuts and serve hot.', 'ingredients': [{'id': 12155, 'name': 'walnuts', 'localizedName': 'walnuts', 'image': 'walnuts.jpg'}], 'equipment': []}]}], 'originalId': None, 'spoonacularScore': 98.08477020263672, 'spoonacularSourceUrl': 'https://spoonacular.com/broccolini-quinoa-pilaf-715769'}, {'vegetarian': False, 'vegan': False, 'glutenFree': True, 'dairyFree': False, 'veryHealthy': True, 'cheap': False, 'veryPopular': False, 'sustainable': False, 'lowFodmap': False, 'weightWatcherSmartPoints': 2, 'gaps': 'no', 'preparationMinutes': None, 'cookingMinutes': None, 'aggregateLikes': 18, 'healthScore': 100, 'creditsText': 'Foodista.com – The Cooking Encyclopedia Everyone Can Edit', 'license': 'CC BY 3.0', 'sourceName': 'Foodista', 'pricePerServing': 340.39, 'extendedIngredients': [{'id': 11485, 'aisle': 'Produce', 'image': 'butternut-squash.jpg', 'consistency': 'SOLID', 'name': 'butternut squash', 'nameClean': 'butternut squash', 'original': '1 large butternut squash, peeled, seeded, thinly sliced (with a mandoline)', 'originalName': 'butternut squash, peeled, seeded, thinly sliced (with a mandoline)', 'amount': 1.0, 'unit': 'large', 'meta': ['with a mandoline)', 'peeled', 'seeded', 'thinly sliced'], 'measures': {'us': {'amount': 1.0, 'unitShort': 'large', 'unitLong': 'large'}, 'metric': {'amount': 1.0, 'unitShort': 'large', 'unitLong': 'large'}}}, {'id': 1159, 'aisle': 'Cheese', 'image': 'goat-cheese.jpg', 'consistency': 'SOLID', 'name': 'goat cheese', 'nameClean': 'goat cheese', 'original': '1/2 oz goat cheese', 'originalName': 'goat cheese', 'amount': 0.5, 'unit': 'oz', 'meta': [], 'measures': {'us': {'amount': 0.5, 'unitShort': 'oz', 'unitLong': 'ounces'}, 'metric': {'amount': 14.175, 'unitShort': 'g', 'unitLong': 'grams'}}}, {'id': 1226, 'aisle': 'Health Foods', 'image': 'liquid-egg-substitute.jpg', 'consistency': 'SOLID', 'name': 'liquid egg substitute', 'nameClean': 'egg substitute', 'original': '1/2 cup liquid egg substitute', 'originalName': 'liquid egg substitute', 'amount': 0.5, 'unit': 'cup', 'meta': [], 'measures': {'us': {'amount': 0.5, 'unitShort': 'cups', 'unitLong': 'cups'}, 'metric': {'amount': 120.0, 'unitShort': 'ml', 'unitLong': 'milliliters'}}}, {'id': 1085, 'aisle': 'Milk, Eggs, Other Dairy', 'image': 'img.spoonacular.', 'consistency': 'LIQUID', 'name': 'non-fat milk', 'nameClean': 'fat free milk', 'original': '2 tbsp. non-fat milk', 'originalName': 'non-fat milk', 'amount': 2.0, 'unit': 'tbsp', 'meta': [], 'measures': {'us': {'amount': 2.0, 'unitShort': 'Tbsps', 'unitLong': 'Tbsps'}, 'metric': {'amount': 2.0, 'unitShort': 'Tbsps', 'unitLong': 'Tbsps'}}}, {'id': 10211821, 'aisle': 'Produce', 'image': 'bell-pepper-orange.png', 'consistency': 'SOLID', 'name': 'bell pepper', 'nameClean': 'bell pepper', 'original': 'Pepper to taste', 'originalName': 'Pepper to taste', 'amount': 1.0, 'unit': 'serving', 'meta': ['to taste'], 'measures': {'us': {'amount': 1.0, 'unitShort': 'serving', 'unitLong': 'serving'}, 'metric': {'amount': 1.0, 'unitShort': 'serving', 'unitLong': 'serving'}}}]}

api_key = "?apiKey=5f7958c1414d412a920d8e937f3f1e10"
baseUrl = "https://api.spoonacular.com/recipes/complexSearch"

headers = {"x-api-key": "5f7958c1414d412a920d8e937f3f1e10"}

recDetailsBaseUrl = "https://api.spoonacular.com/recipes/informationBulk?ids="

def apiGetRecipes():
    results = requests.get(baseUrl + "?type=main course&number=45&offset=355&instructionsRequired&maxReadyTime=90&maxServings=8", headers=headers)
    data = results.json()
    # dataDict = data.loads(data)
    # print(type(data))
    # print(data)

    # f = open("spoonacularResponse.txt", 'w')
    # f.write(str(dataDict))
    # f.close()

    return data

def normText(strList):
    for wd in strList:#corresponds to each recipe dict
        for ingrStr in wd['ingrList']:
            ingrStr = ingrStr.replace("'", "")

def filterRecipeValues(dictData):
    retDict = {}
    retDictList = []
    for d in dictData:# newDict[""] = d[""]
        retDict["id"] = d["id"]
        retDict["url"] = d["sourceUrl"]
        retDict["servings"] = d["servings"]
        retDict["readyInMins"] = d["readyInMinutes"]
        retDict["cookMins"] = d["cookingMinutes"]
        retDict["prepMins"] = d["preparationMinutes"]
        retDict["pricePerServing"] = d["pricePerServing"]
        retDict["isCheap"] = d["cheap"]
        retDict["cuisines"] = d["cuisines"]
        retDict["diets"] = d["diets"]
        retDict["glutenFree"] = d["glutenFree"]
        # retDict["ketogenic"] = d["ketogenic"]
        retDict["lowFodmap"] = d["lowFodmap"]
        retDict["vegan"] = d["vegan"]
        retDict["vegetarian"] = d["vegetarian"]
        retDict["veryHealthy"] = d["veryHealthy"]
        retDict["veryPopular"] = d["veryPopular"]
        
        if (d["instructions"] != None):
            retDict["numSteps"] = max(d["instructions"].count("."), d["instructions"].count("\n"))
            if(retDict["numSteps"] == 0):
                retDict["numSteps"] = None
        else:
            retDict["numSteps"] = None
        
        
        if (d["extendedIngredients"] != None):
            retDict["numIngrs"] = len(d["extendedIngredients"])
            if(retDict["numIngrs"] == 0):
                retDict["numIngrs"] = None
        else:
            retDict["numIngrs"] = None
        
        if (d["extendedIngredients"] != None):
            retDict["ingrList"] = []
            for ingr in d["extendedIngredients"]:
                retDict["ingrList"].append(ingr["name"])
        else:
            retDict["ingrList"] = None
        
        
        retDictList.append(copy.copy(retDict))
        
    return retDictList

        


# recResult = requests.get(recDetailsUrl, headers=headers)
# data = recResult.json()
# f = open("spoonacularRecDetailsNew.txt", "a")
# f.write(str(data))
# f.close()

# print(data)



results = apiGetRecipes()
# print(results)

recIDList = []

recDetailsUrl = "" + recDetailsBaseUrl
for recDictLine in results['results']:
    recDetailsUrl += "%d," % recDictLine['id']
    recIDList.append(recDictLine['id'])

# print(str(recDetailsUrl))


recResult = requests.get(recDetailsUrl, headers=headers)
data = recResult.json()

newDict = filterRecipeValues(data)

# print(newDict)

f = open("recipeData/spoonacularRecDetailsNew2.txt", "a")
f.write("\n" + str(newDict))
f.close()
