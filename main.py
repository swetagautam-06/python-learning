dicti = {"animal": "dog",
       "flower": "rose",
       "food": "momo"}
print(dicti["food"]) #retriving items from the dictionary

#adding new items to doctionary
dicti["vehicle"]= "car"
print(dicti)

#creating empty dictionary
empty_dictionary ={}

#wipe an existing distionary
# dicit = {}
# print(dicit)

#edit an item in adictionary
dicti["vehicle"] = "bike"
print(dicti)

#loop through a dictionary
for key in dicti:
       # print(key)
       print(dicti[key])