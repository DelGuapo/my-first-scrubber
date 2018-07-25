# CORE Dependencies
import sys
import re

# THIRD PARTY IMPORTS
from bs4 import BeautifulSoup
from collections import Counter
import numpy

# APP Dependencies
from .html import HTMLParser
from .myConfig import AlbumConfig,ArtistConfig

class DiscogParser:
    """
        Config object 
    """
    def __init__(self,artistConfig):
        self.artist = artistConfig
        self.baseURL = 'https://www.discogs.com'
        self.artistDir = None
        self.albums = []
        self.errors = None
        if not self.hasArtistId():
            self.findDiscogId()

    def hasArtistId(self):
        return hasattr(self.artist,'id') and self.artist.id != -1 and self.artist.id != None

    def findAlbums(self):
        if not self.hasArtistId():
            print(' -- Missing Artist ID for [' + self.artist.name + ']')
            return False
        print(' -- FETCHING DISCOG [' + self.artist.name + '] --')
        searchUrl = 'https://www.discogs.com/artist/' + str(self.artist.id)
        
        soup = HTMLParser(searchUrl).pullDOMSoup()
        if(soup == None):
            self.throwError('Could not pull Info')
            return False
            
        albumLinks = soup.find('table', {'id' : 'artist'}).find_all("tr")

        for link in albumLinks:
            print(link)
            album = AlbumConfig()
            album.name = link.get('title')
            # album.url = self.baseURL +  link.get('href')
            album.artistDir = self.artist.dir 
            album.artist = self.artist.name
            # TODO: add TrackList logic.
            self.albums.append(album)
        
        self.artist.timeStamp()

        return True

    def throwError(self,errorString):
        if(self.errors == None):
            self.errors = []
        self.errors.append(errorString)

    def findDiscogId(self):
        """
            Search the website with a generic keyword search to find the artist ID
        """
        print(' -- Finding Discog artist ID for [' + self.artist.name + '] --')
        discogTitle = self.artist.name.replace(' ','+')
        searchUrl = 'https://www.discogs.com/search/?q=' + discogTitle + '&type=master'
        
        soup = HTMLParser(searchUrl).pullDOMSoup()
        if(soup == None):
            self.throwError('Could not pull Info')
            return False

        self.albums = []

        artistLinks = soup.findAll(href=re.compile('/artist/'))
        foundIds = []
        for link in artistLinks:
            tmpContent = link.contents
            tmpId = link.get('href').replace('/artist/','').split('-')[0]
            tmpArtist = tmpContent[0].upper() if len(tmpContent) > 0 else ''
            if self.artist.name.upper() == tmpArtist and tmpId.isnumeric():
                foundIds.append(int(tmpId))
        

        if len(foundIds) > 0:
            # s = Counter(foundIds)
            # print(s.most_common()[0])
            self.artist.id = max(set(foundIds), key=foundIds.count)
        
        # arr = numpy.array(foundIds)
        # stdev = numpy.std(arr,0)
        # print(stdev)
        # if(len(arr) > 0 and stdev == 0):
        #     self.artist.id = foundIds[0]
        #     return self.artist.id
        # else:
        #     return None
