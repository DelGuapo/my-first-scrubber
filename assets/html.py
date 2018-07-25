# CORE
import requests


# THIRD PARTY IMPORTS
from bs4 import BeautifulSoup

class HTMLParser:
    def __init__(self,URL = None):
        self.URL = URL

    def pullDOMSoup(self):
        # PULLS HTML PAGE INFO FROM URL
        if(self.URL == None or self.URL == ''):
            return None

        page = requests.get(self.URL)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            return soup
        else:
            return None