# CORE IMPORTS
import os

# APP DEPENDENCIEES
from .discog import DiscogParser
from .myConfig import ArtistConfig,AlbumConfig


class Parser:
    """
    This class parses files on local directory
    """
    def __init__(self,source):
        self.startDate = 'NOW'
        self.source = source
        self.albums = []
        self.errors = None
    
    def prepare(self, artistDir):
        # INTERFACE WITH MAIN.PY
        self.artistDir = artistDir
        artist = artistDir.split('\/')[-1]
        self.artist = self.putTheInFront(artist)

        # Try to read config:
        tmp = self.readConfig()
        if(tmp):
            self.artistConfig = ArtistConfig(tmp)
        else:
            cfg = ArtistConfig(None)
            cfg.name = self.artist
            cfg.source = self.source
            cfg.dir = self.artistDir
            self.artistConfig = cfg
        if self.source.upper() == 'DISCOG':
            webParser = DiscogParser(self.artistConfig)
            webParser.findAlbums()
            self.artistConfig = webParser.artist

        self.albums = webParser.artist.albums
        self.writeConfig()

    def throwError(self,err):
        if(self.errors == None):
            self.errors = []
        self.errors.append(err)

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
        f = open(fileName,"w")
        # self.artistConfig.dir = self.artistDir
        f.write(self.artistConfig.makeJson())
        f.close()

    def readConfig(self):
        fileName = self.artistDir + '\/config.'+ self.source
        if(os.path.isfile(fileName)):
            f = open(fileName, 'r') 
            return f.read()
        return False