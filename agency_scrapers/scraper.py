from lxml import html
import requests
import agency_scrapers.apa_full
import agency_scrapers.billions_full 
import agency_scrapers.coda_full
import agency_scrapers.paradigm_full
import agency_scrapers.uta_full
import agency_scrapers.uta_usa

def scrapeAgency(agencyName, version):
	roster = agencyName.lower() + '_' + version.lower()
	
	if roster == 'apa_full':
		agency_scrapers.apa_full.scrape(),
	elif roster == 'billions_full': 
		agency_scrapers.billions_full.scrape(),
	elif roster == 'coda_full': 
		agency_scrapers.coda_full.scrape(),
	elif roster == 'paradigm_full': 
		agency_scrapers.paradigm_full.scrape(),
	elif roster == 'uta_full': 
		agency_scrapers.uta_full.scrape(),
	elif roster == 'uta_usa': 
		agency_scrapers.uta_usa.scrape()
	