# CORE IMPORTS
import os
import re

# THIRD PARTY IMPORTS

# INTERNAL IMPORTS
from assets.myConfig import Config,OtherClass
from assets.parser import Parser

class Main:
    """
        this the main class. 
    """
    def __init__(self):
        self.counter = 0

    def parse(self, myDir):
        # IMPORTS myDir FROM CONFIG TO PARSE FOR ARTISTS
        directory = os.fsencode(myDir)
        for file in os.listdir(directory):
            self.counter += 1
            filename = os.fsdecode(file)
            # Init DISCOG parser
            if self.counter == 1:
                discog = Parser()
                discog.go(filename,'discog')
            # else: # COMMENTING OUT FOR DEV PURPOSES.
            #     print('Ignoring [' + filename + '] for development')
            continue
    
    def go(self):
        # MAIN FUNCTION FOR MAIN CLASS
        c = Config()
        self.parse(c.myDir)

# MAIN ROUTE TO INTERFACE WITH THE TERMINAL
if __name__ == "__main__":
    m = Main()
    m.go()