from lxml import html
import requests

def scrape():
	dbFile = open(".\\output\\billions-full-output.txt", "w")

	page = requests.get('http://billions.com/news/', headers={'User-Agent':'test'})
	tree = html.fromstring(page.content)

	#This will create a list of artists:
	artists = tree.xpath('//div[@class="artists tabcontent"]/ul/li/a/text()')
	
	for artist in artists:
		if len(artist) > 1:
			dbFile.write(artist+"\n");

	dbFile.close()
