from lxml import html
import requests

dbFile = open("C:\\Users\\Danny\\Desktop\\Computer Science\\Bandit\\agency_scrapers\\output\\apa-full-output.txt", "w")

page = requests.get('http://touring.apa-agency.com/roster/list', headers={'User-Agent':'test'})
tree = html.fromstring(page.content)

#This will create a list of artists:
artists = tree.xpath('//div[@class="work-meta"]/a/h4/text()')
print(artists)
for artist in artists:
    if len(artist) > 1:
        dbFile.write(artist+"\n");

dbFile.close()
