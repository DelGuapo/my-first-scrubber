# CORE IMPORTS
import os
import re

# THIRD PARTY IMPORTS

# INTERNAL IMPORTS
from assets.myConfig import Config,OtherClass
from assets.parser import Parser,Album

class Main:
    """
        this the main class. 
    """
    def __init__(self):
        self.counter = 0
        self.missingAlbums = []

    def parse(self, myDir):
        # IMPORTS myDir FROM CONFIG TO PARSE FOR ARTISTS
        directory = os.fsencode(myDir) # encode the directory into OS object
        for file in os.listdir(directory):
            self.counter += 1
            folderName = os.fsdecode(file) # decode file object into string (folder name)
            subDir = self.config.myDir + '\/' + folderName
            folderName = 'crocodiles'
            # Init DISCOG parser
            if self.counter == 28: ## remove after development

                # PREPARE Discog Instance
                discog = Parser()
                discog.prepare(subDir,'discog')

                # Get albums + Info from Discog instance
                remoteAlbums = list(map(
                    lambda album: album.name
                    ,discog.albums
                    ))

                # Find local albums
                localAlbums = list(os.listdir(subDir))
                localAlbums.append(remoteAlbums[1])

                # Find any missing albums
                alignedAlbums = self.listIntersect(remoteAlbums,localAlbums)
                misAlignedAlbums = [album for album in remoteAlbums if album not in alignedAlbums]

                # Add missing albums to master list to report to user
                for album in misAlignedAlbums:
                    idx = remoteAlbums.index(album)
                    self.missingAlbums.append(discog.albums[idx])
            continue

    def go(self):
        # MAIN FUNCTION FOR MAIN CLASS
        self.config = Config()
        self.parse(self.config.myDir)
    
    # Python program to illustrate the intersection
    # of two lists in most simple way
    def listIntersect(self, lst1, lst2):
        list2 = list(map(
            lambda item: item.upper()
            ,lst2
        ))
        return [value for value in lst1 if value.upper() in list2]

# MAIN ROUTE TO INTERFACE WITH THE TERMINAL
if __name__ == "__main__":
    m = Main()
    m.go()