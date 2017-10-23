import sys
import spotipy
import spotipy.util as util
import spotify.lib.search as search
import agency_scrapers.scraper as scrape

def main():
    scope = 'user-library-read';

    iniVals = getIniVals()

    username = iniVals["SPOTIFY_USERNAME"]

    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token);
        results = search.searchByArtistName(sp, 'Laura Stevenson');
        print(results);
        # Pass sp into other functions for desired functionality
    else:
        print("Can't get token for", username)

# Creates a map of all values in the main ini file
def getIniVals():
    file = open('./ini/main.ini', 'r')
    valueMap = {}
    for line in file:
        if len(line) > 2:
            lineParts = line.split("=")
            valueMap[lineParts[0]] = lineParts[1]
    return valueMap

main()
            
