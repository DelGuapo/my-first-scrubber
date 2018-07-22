# CORE IMPORTS
import requests
import os
import json
import sys

# THIRD PARTY IMPORTS
from bs4 import BeautifulSoup

class Album:
    """
        object 
    """
    def __init__(self):
        self.name = None
        self.url = None
        self.about = None
        self.artist = None
        self.artistDir = None
        self.tracklist = []

class ArtistConfig:
    """
        Config object 
    """
    def __init__(self,jsonString):
        if(jsonString != None):
            self.__dict__ = json.loads(jsonString)
        else:
            self.name = None
            self.id = None
            self.source = None
            self.url = None    
    def makeJson (self):
        return json.dumps(self.__dict__) 



class Parser:
    """
    This class parses files on local directory
    """
    def __init__(self):
        self.startDate = 'NOW'
    
    def prepare(self, artistDir, source):
        # INTERFACE WITH MAIN.PY
        self.artistDir = artistDir
        artist = artistDir.split('\/')[-1]
        self.artist = self.putTheInFront(artist)
        self.source = source
        
        if source.upper() == 'DISCOG':
            self.parseDiscog()
            # TODO: SETUP OTHER PARSERS

        # Try to read config:
        tmp = self.readConfig()

        if(tmp):
            self.artistConfig = ArtistConfig(tmp)
        else:
            cfg = ArtistConfig(None)
            cfg.name = self.artist
            cfg.source = self.source
            self.artistConfig = cfg
            self.writeConfig()

    def parseDiscog(self):
        """
            First search with keyword 
        """
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
            album.artistDir = self.artistDir
            album.artist = self.artist
            # TODO: add TrackList logic.
            self.albums.append(album)

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

    def writeConfig(self):
        fileName = self.artistDir + '\/config.'+ self.source
        fileName = 'C:\/Users\/Nicholas Weaver\/Documents\/config.'+ self.source
        print(fileName)
        f = open(fileName,"w")
        f.write(self.artistConfig.makeJson())
        f.close()

    def readConfig(self):
        fileName = self.artistDir + '\/config.'+ self.source
        fileName = 'C:\/Users\/Nicholas Weaver\/Documents\/config.'+ self.source
        if(os.path.isfile(fileName)):
            f = open(fileName, 'r') 
            return f.read()
        return False

    def pullDOMSoup(self):
        # PULLS HTML PAGE INFO FROM URL
        page = requests.get(self.URL)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            return soup
        else:
            return None