import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read';

username = 'dannygmoe'

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token);
    results = sp.search(q='artist:Laura Stevenson', type='artist');
    print(results['artists']['items'][0])
else:
    print("Can't get token for", username)


