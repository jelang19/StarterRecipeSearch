import json
import csv

f = open("recipeData/spoonacularRecDetails.txt", "r")
fileText = f.read()
f.close()

parsed = json.loads(fileText)

print(type(parsed[0]))

# for recipe in parsed:
#     if (recipe["id"] == 638626):
#         print(recipe)
#         break
#638626

# keys = parsed[0].keys()

# with open('recipeData/recipesSheet2.csv', 'w', newline='') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(parsed)