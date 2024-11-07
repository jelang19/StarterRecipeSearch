import requests
import csv
from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import PorterStemmer

baseEdamamUrl = "https://api.edamam.com/api/recipes/v2"

MEAS_LIST_STEMMED = ['pound', 'tablespoon', 'teaspoon', 'kilogram', 'gram', 'ounce', 'cup', 'pinch', 'dash', 'liter', 'milliliter', 'quart', 'gallon', 'pint', 
                     'pounds', 'tablespoons', 'teaspoons', 'kilograms', 'grams', 'ounces', 'cups', 'pinchs', 'dashs', 'liters', 'milliliters', 'quarts', 'gallons', 'pints',]

def recipeSearch():
    app_id = "20071b56"
    app_key = "5c7c5e36409bce9825d978ee7fd820ae"

    results = requests.get(baseEdamamUrl + "?type=public&q=chicken&app_id=" + app_id + "&app_key=" + app_key)
    data = results.json()

    return data['hits']

def save_to_csv(recipes, ingredient):
    if recipes:
      file_name = f"{ingredient}_recipes.csv"

      with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Recipe', 'URL', 'Ingredients'])

            for recipe in recipes:
                recipe_info = recipe['recipe']
                recipe_name = recipe_info['label']
                recipe_url = recipe_info['url']
                ingredients = "\n".join(recipe_info['ingredientLines'])
                writer.writerow([recipe_name, recipe_url, ingredients])
                writer.writerow([])

      print(f"Recipes saved to recipes.csv")
    else:
        print("No recipes found")


def filterIngredients(recipeLines):
    ingredList = []

    for recLine in recipeLines:
        wordList = word_tokenize(recLine)
        taggedWords = nltk.pos_tag(wordList)
        # print(taggedWords)

        for tup in taggedWords:
            if ((tup[1] == 'NN') or (tup[1] == 'NNS')) and (tup[0] not in MEAS_LIST_STEMMED):
                ingredList.append(tup[0])

        stemmer = PorterStemmer()
        st_wordList = [stemmer.stem(word) for word in wordList]

    return ingredList


# ------------------------------------------ Main ----------------------------------------------------- 
recipes = recipeSearch()
# save_to_csv(recipes, 'foo')
recNum = 1

for k,v in recipes[recNum]['recipe'].items():
    print(k, v)
    print("\n")

recipeFeats = []

# String values
recipeFeats.extend(recipes[recNum]['recipe']['dietLabels'])
recipeFeats.extend(recipes[recNum]['recipe']['healthLabels'])
recipeFeats.extend(recipes[recNum]['recipe']['mealType'])
recipeFeats.extend(recipes[recNum]['recipe']['dishType'])
recipeFeats.extend(recipes[recNum]['recipe']['cuisineType'])
recipeFeats.extend(filterIngredients(recipes[recNum]['recipe']['ingredientLines']))

# Numeric Values
recipeFeats.append(recipes[recNum]['recipe']['totalTime'])



print(recipeFeats)


