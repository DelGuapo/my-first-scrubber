# CORE IMPORTS
import requests
import os

# THIRD PARTY IMPORTS
from bs4 import BeautifulSoup

class Album:
    """
        object 
    """
    def __init__(self):
        self.name = ''
        self.url = ''
        self.about = ''
        self.artist = ''
        self.artistClean = ''
        self.tracklist = []

class Parser:
    """
    This class parses files on local directory
    """
    def __init__(self):
        self.startDate = 'NOW'
    
    def prepare(self, artist, source):
        # INTERFACE WITH MAIN.PY
        self.artistClean = artist
        self.artist = self.putTheInFront(artist)
        self.source = source
        
        if source.upper() == 'DISCOG':
            self.parseDiscog()
            # TODO: SETUP OTHER PARSERS
        elif source.upper() == 'OTHER':
            self.parseOther()

    def parseDiscog(self):
        print(' -- FETCHING DISCOG: [' + self.artist + '] --')
        discogTitle = self.artist.replace(' ','+')
        self.baseURL = 'https://www.discogs.com'
        self.URL = 'https://www.discogs.com/search/?q=' + discogTitle + '&type=master'
        soup = self.pullDOMSoup()
        self.albums = []
        links = soup.findAll("a", {"class": "search_result_title"})

        for link in links:
            album = Album()
            album.name = link.get('title')
            album.url = self.baseURL +  link.get('href')
            album.artistClean = self.artistClean
            album.artist = self.artist
            # TODO: add TrackList logic.
            self.albums.append(album)

    def parseOther(self):
        # PLACHOLDER FOR OTHER SOURCE SITES
        self.URL = 'OTHER URL'

    def putTheInFront(self, artist):
        # removes ', the' and puts it at the beginning for searches
        tmp = artist.lower().replace(', ',',')
        commaThe = tmp.lower().split(',the')
        if len(commaThe) > 1:
            return 'the ' + commaThe[0]
        else:
            return artist
    
    def putTheInBack(self,artist):
        if artist.upper()[:4] == 'THE ':
            return artist[4:] + ', The'
        else:
            return artist

    def pullDOMSoup(self):
        # PULLS HTML PAGE INFO FROM URL
        page = requests.get(self.URL)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            return soup
        else:
            return None