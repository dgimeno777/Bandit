import sys
import spotipy
import spotipy.util as util

def main():
    scope = 'user-library-read';

    iniVals = getIniVals()

    username = iniVals["USERNAME"]

    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token);
        # Pass sp into other functions for desired functionality
    else:
        print("Can't get token for", username)

# Creates a map of all values in the main ini file
def getIniVals():
    file = open('main.ini', 'r')
    valueMap = {}
    for line in file:
        if len(line) > 2:
            lineParts = line.split("=")
            valueMap[lineParts[0]] = lineParts[1]
    return valueMap

main()
            
