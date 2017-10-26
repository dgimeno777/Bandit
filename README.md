# Bandit
Tool to gather agency roster lists and compare artist popularity statistics

## Scraping 
This project uses lxml web scraping in python to collect the names of artists on agency rosters

## Spotipy
This project uses Spotipy to retrieve artist popularity data to sort and filter artists

## Other Plans
I am also planning to use facebook to get likes of artists and google trends to get graphs and search information on artists

# Setup
1) Install the latest version of Python (https://www.python.org/)
2) In terminal, run 'pip install sys' (you may not have to do this), 'pip install spotipy', 'pip install lxml'
3) Setup Spotipy env vars on your machine to connect to spotify api (quick google should show you how to do this on both windows and mac)
   - SPOTIPY_CLIENT_ID      = Spotify API Client_ID
   - SPOTIPY_CLIENT_SECRET  = Spotify API Client_Secret
   - SPOTIPY_REDIRECT_URI   = Spotify API Redirect_URI

4) Copy this repo to your machine or download as a zip and unzip
5) Using Python Idle (installed in step 1), open the 'main.py' file from the downloaded Bandit project and run the module.
6) Bandit should now be running (to the extent that it can).

# Workflows
## Get report for agency roster
1. Run main.py
1.5. You may have to give Bandit access to your spotify in a web window and copy-paste the url after done
2. Enter 'report'
3. Enter 'agency' (check AgencyRoster_todo for finished rosters)
4. Enter 'roster' (usually 'full' but currently uta also has a 'usa' one)

