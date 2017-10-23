
def searchByArtistName(sp, artistName):
    results = sp.search(q='artist:'+artistName, type='artist');
    return results;

def searchByArtistId():
    results = sp.search(q='', type='artist')
    return results;
