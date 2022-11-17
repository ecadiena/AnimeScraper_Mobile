import json

with open('data.json') as json_data:
    jsonData = json.load(json_data)

for i in jsonData["Manga"]:
    if "Chainsaw Man" in i['title']:
        print(i['title'])
        print(i['image'])
        print(i['date'])
        print(i['tags'])
        print(i['episodes'])
        break