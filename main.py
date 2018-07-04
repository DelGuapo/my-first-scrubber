# global dependencies
import os
import re

# internal dependencies
from assets.myConfig import Config,OtherClass
from assets.parser import Parser

# don't know what this is:


class Main:
    """
        this is a class
    """
    def __init__(self):
        self.counter = 0

    def parse(self, myDir):
        directory = os.fsencode(myDir)
        for file in os.listdir(directory):
            self.counter += 1
            filename = os.fsdecode(file)
            # Init DISCOG parser
            if self.counter == 1:
                discog = Parser()
                discog.go(filename,'discog')
            # else:
            #     print('Ignoring [' + filename + '] for development')
            continue
    
    def go(self):
        # need to find out how to execute this function lol
        c = Config()
        # print(c.myDir)
        self.parse(c.myDir)

if __name__ == "__main__":
    m = Main()
    m.go()