from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json

html = Request('https://www.livechart.me/fall-2022/all', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(html)
soup = BeautifulSoup(page, 'html.parser')
anime_list = soup.find_all('article', attrs={'class': 'anime'})
jsonObject = {
    "Original": [], 
    "Novel": [], 
    "Light Novel": [], 
    "Visual Novel": [], 
    "Manga": [], 
    "Game": [], 
    "Media Mix Project": [],
    "Otome Game": [],
    "Music": [],
    "Children's Game": [],
    "Media Franchise": []
}
anime_Arr = []

for anime in anime_list: 
    title = anime.find("h3", class_="main-title")
    date = anime.find("div", class_="anime-date")
    image = anime.find("img")
    tags = anime.find("ol", class_="anime-tags")
    episodes = anime.find("div", class_="anime-episodes")
    source = anime.find("div", class_="anime-source")
    anime_Object = {
        "title": title.text.strip(),
        "date": date.text.strip(),
        "image": image['src'],
        "tags": tags.text.strip(),
        "episodes": episodes.text.strip()
    }
    # anime_Arr.append(anime_Object)
    if source.text.strip() == "Original": 
        jsonObject["Original"].append(anime_Object)
    if source.text.strip() == "Novel": 
        jsonObject["Novel"].append(anime_Object)
    if source.text.strip() == "Light Novel": 
        jsonObject["Light Novel"].append(anime_Object)
    if source.text.strip() == "Visual Novel": 
        jsonObject["Visual Novel"].append(anime_Object)
    if source.text.strip() == "Manga": 
        jsonObject["Manga"].append(anime_Object)
    if source.text.strip() == "Game": 
        jsonObject["Game"].append(anime_Object)
    if source.text.strip() == "Media Mix Project": 
        jsonObject["Media Mix Project"].append(anime_Object)
    if source.text.strip() == "Otome Game": 
        jsonObject["Otome Game"].append(anime_Object)
    if source.text.strip() == "Music": 
        jsonObject["Music"].append(anime_Object)
    if source.text.strip() == "Children's Game": 
        jsonObject["Children's Game"].append(anime_Object)
    if source.text.strip() == "Media Franchise": 
        jsonObject["Media Franchise"].append(anime_Object)
    # print(title.text.strip())
    # print(image['src'])
    # print(date.text.strip())
    # print(tags.text.strip())
    # print(episodes.text.strip())
    # print()

with open('data.json', 'w') as output_file:
    json.dump(jsonObject, output_file)

'''
Resources: 
https://hackernoon.com/building-a-web-scraper-from-start-to-finish-bb6b95388184
https://stackoverflow.com/questions/55210950/python-beautifulsoup-extracting-strings-from-tags-based-on-items-in-list
https://www.geeksforgeeks.org/image-scraping-with-python/
'''