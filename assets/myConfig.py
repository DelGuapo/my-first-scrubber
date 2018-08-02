# Core Imports
import json
import sys
import datetime

class AppConfig:
    """
        Init Function (constructor);
    """
    def __init__(self):
        # Nick's Drive
        self.myDir = 'C:\/Users\/Nicholas Weaver\/_My Music'
        # Mike's Drive 
        # self.myDir = 'D:\/My Music'


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
        self.exists = False
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
        obj = self.__dict__
        obj['albums'] = [] # <<-- until i learn to JSON serialize a nested object
        return json.dumps(obj) 
