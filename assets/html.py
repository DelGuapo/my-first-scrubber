# CORE
import requests


# THIRD PARTY IMPORTS
from bs4 import BeautifulSoup

class HTMLParser:
    def pullDOMSoup(self,URL = None):
        # PULLS HTML PAGE INFO FROM URL
        if(URL == None or URL == ''):
            return None

        page = requests.get(URL)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            return soup
        else:
            return None