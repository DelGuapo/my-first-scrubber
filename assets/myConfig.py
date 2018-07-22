# Core Imports
import json
import sys

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
