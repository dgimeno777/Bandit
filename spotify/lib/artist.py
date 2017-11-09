def getTopSongs(sp, artistId):
	urn = 'spotify:artist:'+artistId
	results = sp.artist_top_tracks(urn)

# Spotify does not have this data available
# def getTopSongsAverageListens(sp, artistId):
	