# CORE IMPORTS
import requests
import os

# THIRD PARTY IMPORTS
from bs4 import BeautifulSoup

class Parser:
    """
    This class parses files on local directory
    """
    def __init__(self):
        self.startDate = 'NOW'
    
    def go(self, artist, source):
        # INTERFACE WITH MAIN.PY
        self.artist = artist
        self.source = source

        if source.upper() == 'DISCOG':
            self.parseDiscog()
            # TODO: SETUP OTHER PARSERS
        elif source.upper() == 'OTHER':
            self.parseOther()

    def parseDiscog(self):
        print(' -- FETCHING DISCOG: [' + self.artist + '] --')
        self.URL = 'https://www.discogs.com/search/?q=pink+floyd&type=master'
        DOM = self.pullDOM()
        tags = [item for item in list(DOM.children) if type(item) != 'bs4.element.Tag']
        print(len(tags))
    def parseOther(self):
        # PLACHOLDER FOR OTHER SOURCE SITES
        self.URL = 'OTHER URL'

    def pullDOM(self):
        # PULLS HTML PAGE INFO FROM URL
        page = requests.get(self.URL)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            return soup
        else:
            return None