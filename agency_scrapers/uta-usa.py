from lxml import html
import requests

page = requests.get('http://music.utatouring.com/usa-roster/', headers={'User-Agent':'test'})
tree = html.fromstring(page.content)

#Creates a list of artists:
artists = tree.xpath('//div[@class="ut-one-third"]/div/a/text()')
artistsScrubbed = "";
for artist in artists:
    if len(artist) > 1:
        artistsScrubbed += artist + ", ";

artistsScrubbed = artistsScrubbed[:len(artistsScrubbed)-2];

print (artistsScrubbed)
