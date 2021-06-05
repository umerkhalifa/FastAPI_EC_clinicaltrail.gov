import requests
from bs4 import BeautifulSoup
import re

def trial_scrape(NCTnumber):
    url = 'https://clinicaltrials.gov/ct2/show/' + NCTnumber
    ClinicalTrialpage = requests.get(url)
    soup = BeautifulSoup(ClinicalTrialpage.text, 'html.parser')
    data = soup.select('div.tr-indent2 p + ul')
    study_title = ''.join([row.text for row in soup.select('h1.tr-h1.ct-sans-serif')])
    inclusion = [sentence.text for sentence in data[0].find_all('li')]
    exclusion = [sentence.text for sentence in data[1].find_all('li')]
    sponsor = ''.join([row.text for row in soup.select('div#sponsor.tr-info-text')])
    collaborator = ''.join([row.text for row in soup.select('div#sponsor1.tr-info-text')])
    result = {
        'study title': study_title, 'inclusion': inclusion, 'exclusion': exclusion, 
        'sponsor':sponsor, 'collaborator':collaborator}
    return result


