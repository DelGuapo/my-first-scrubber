from bs4 import BeautifulSoup
import requests


import os

class Parser:
    """
    This class parses files on local directory
    """
    def __init__(self):
        self.startDate = 'NOW'
    
    def go(self, artist, source):
        self.artist = artist
        self.source = source
        if source.upper() == 'DISCOG':
            self.parseDiscog()
        elif source.upper() == 'OTHER':
            self.parseOther()

    def parseDiscog(self):
        print(' -- FETCHING DISCOG: [' + self.artist + '] --')
        self.URL = 'https://www.discogs.com/search/?q=pink+floyd&type=master'
        DOM = self.pullDOM()

    def parseOther(self):
        self.URL = 'OTHER URL'

    def pullDOM(self):
        page = requests.get(self.URL)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            return soup
        else:
            return None
        # soup = BeautifulSoup(html,'html.parser')

        
