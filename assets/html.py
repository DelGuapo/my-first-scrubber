# CORE
import urllib.request
import time

# THIRD PARTY IMPORTS
from bs4 import BeautifulSoup

# local dependencies
from .pyCommon import wait

class HTMLParser:
    def __init__(self,URL = None):
        self.URL = URL
        self.retryCount = 0
        
    def pullDOMSoup(self):
        # PULLS HTML PAGE INFO FROM URL
        if(self.URL == None or self.URL == ''):
            return None

        response = urllib.request.urlopen(self.URL,timeout=10)
        if response.getcode() == 200:
            soup = BeautifulSoup(response.read(), 'html.parser')
            wait(15,False) # <<-- adding in until I learn to handle http-429  response.
            return soup
        elif response.getcode() == 429:
            if self.retryCount > 5:
                return None
            else:
                self.retryCount += 1
                print ('.... HTTP code 429. Retry in ' + str(self.retryCount * 5))
                time.sleep(self.retryCount * 5)
                return self.pullDOMSoup()
        else:
            return None