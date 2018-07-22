# CORE Dependencies
import sys

# THIRD PARTY IMPORTS
from bs4 import BeautifulSoup

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

    def findDiscigAlbums(self):
        print('test')

    def findDiscogId(self):
        """
            First search with keyword 
        """
        print(' -- FETCHING DISCOG: [' + self.artist.name + '] --')
        discogTitle = self.artist.name.replace(' ','+')
        searchUrl = 'https://www.discogs.com/search/?q=' + discogTitle + '&type=master'
        
        soup = HTMLParser().pullDOMSoup()
        self.albums = []
        links = soup.findAll("a", {"class": "search_result_title"})

        for link in links:
            album = AlbumConfig()
            album.name = link.get('title')
            album.url = self.baseURL +  link.get('href')
            album.artistDir = self.artist.artistDir
            album.artist = self.artist.name
            # TODO: add TrackList logic.
            self.albums.append(album)
        
