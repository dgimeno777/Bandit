from lxml import html
import requests
import apa-full
import billions-full
import coda-full
import paradigm-full
import uta-full
import uta-usa
# @TODO: Add output file reading class

def scrapeAgency(agencyName, version):
	{
		'apa-full': apa-full.scrape()
	}[agencyName + '-' + version]
	