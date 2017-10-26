
def searchByArtistName(sp, artistName):
    results = sp.search(q='artist:'+artistName, type='artist')
    return results;

def searchByArtistId(sp, artistId):
    results = sp.artist(artistId)
    return results;
	
