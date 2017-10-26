import sys
import datetime
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
        #results = search.searchByArtistName(sp, 'Laura Stevenson');
        while True:
            response = input("Please enter a command (report):");
            if response == 'report':
                makeReport(sp)
            else:
                displayHelp()
        # Pass sp into other functions for desired functionality
    else:
        print("Can't get token for", username)

def makeReport(sp):
    agency = input("Enter the agency: ")
    roster = input("Enter the roster(full): ")
    doScrape(agency, roster);
    dbFile = open('./scraper_output/'+agency+'_'+roster+'-output.txt', 'r')
    now = datetime.datetime.now()
    print('Creating report for ' + agency + '_' + roster + '...')
    reportFile = open('./reports/'+
                      'report_'+
                      now.strftime("%Y-%m-%d")+
                      '_'+
                      now.strftime("%H-%M-%S")+
                      '_'+
                      agency + '-' + roster, 'w+')
    reportFile.write('"ArtistName",TotalSpotifyFollowers\n')
    delim = ','
    for artist in dbFile:
        artist = artist.strip()
        spotifyInfo = search.searchByArtistName(sp, artist)
        print(artist)
        if spotifyInfo["artists"]["items"]:
            reportFile.write('"'+artist+'"'+delim+
                             str(spotifyInfo["artists"]["items"][0]["followers"]["total"])+
                             '\n')
        else:
            reportFile.write('No information found for: '+artist+'\n')
    reportFile.close()
    dbFile.close()
    

def doScrape(agency, roster):
    print('Scraping for ' + agency + '_' + roster + '...')
    scrape.scrapeAgency(agency, roster)
    
def displayHelp():
    print('Welcome to Bandit! You can currently use the "report" or "help" functions')

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
            
