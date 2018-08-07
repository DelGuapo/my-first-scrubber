# CORE IMPORTS
import os
import re

# THIRD PARTY IMPORTS

# INTERNAL IMPORTS
from assets.myConfig import AppConfig,AlbumConfig,ArtistConfig
from assets.parser import Parser
from assets.discog import DiscogParser
from assets.html import HTMLParser
from assets.pyCommon import wait

class Main:
    """
        this the main class. 
    """
    def __init__(self):
        self.counter = 0
        self.missingAlbums = []
        self.csvReport = 'Artist|Album|URL|Exists Locally' + chr(10)

    def writeReport(self):
        self.reportStream.close()


    def parse(self, myDir):
        # IMPORTS myDir FROM CONFIG TO PARSE FOR ARTISTS
        directory = os.fsencode(myDir) # encode the directory into OS object
        for file in os.listdir(directory):
            self.counter += 1
            folderName = os.fsdecode(file) # decode file object into string (folder name)
            subDir = self.config.myDir + '\/' + folderName
            if not os.path.isdir(subDir): continue
            # PREPARE Discog Instance
            discog = Parser('discog')
            discog.prepare(subDir)

            # Get albums + Info from Discog instance
            if(discog.errors != None):
                print('Error retreiving albums')
                return

            remoteAlbums = list(map(
                lambda album: album.name
                ,discog.albums
                ))

            # Find local albums
            localAlbums = list(os.listdir(subDir))
            # print('local: ' + str(len(localAlbums)) + '; remote: ' + str(len(remoteAlbums)))

            # Find any missing albums
            alignedAlbums = self.listIntersect(remoteAlbums,localAlbums)

            for album in discog.albums:
                album.exists = album.name in alignedAlbums

            self.transpileAlbums(discog)

            misAlignedAlbums = [album for album in remoteAlbums if album not in alignedAlbums]
            
            # Add missing albums to master list to report to user
            for album in misAlignedAlbums:
                idx = remoteAlbums.index(album)
                self.missingAlbums.append(discog.albums[idx])
        
        self.writeReport()

    def transpileAlbums(self,parser):
        for album in parser.albums:
            s = (str(parser.artistConfig.id) or '') + '|'
            s += (album.artist or '') + '|'
            s += (album.name or '') + '|'
            # s += (album.image or '') + ','
            s += (album.url or '') + '|'
            s += str(album.exists)
            self.reportStream.write(s + chr(10))
            self.csvReport += s + chr(10)

    def go(self):
        # MAIN FUNCTION FOR MAIN CLASS
        self.config = AppConfig()
        fileName = self.config.myDir + '\/mac_report.txt'
        self.reportStream = open(fileName,"w",encoding='utf-8') # <<== until we figure how to encode correctly, force utf-8 encoding.
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

m = Main()
m.go()
print('Terminating')
wait(5)