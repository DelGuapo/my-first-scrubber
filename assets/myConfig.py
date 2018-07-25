# Core Imports
import json
import sys
import datetime

class AppConfig:
    """
        Init Function (constructor);
    """
    def __init__(self):
        self.myDir = 'C:\/Users\/Nicholas Weaver'


class AlbumConfig:
    """
        object 
    """
    def __init__(self):
        self.name = None
        self.url = None
        self.about = None
        self.artist = None
        self.artistDir = None
        self.image = None
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
            self.dir = None
            self.date = None
        
        self.albums = []

    def timeStamp(self):
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
    def makeJson (self):
        return json.dumps(self.__dict__) 
