from bs4 import BeautifulSoup
from urllib.request import urlopen
from config import config
from parse import parse
import re

class macgyver:
    """
        this is a class
    """
    def parse(myDir):
        directory = os.fsencode(myDir)
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".asm") or filename.endswith(".py"): 
                # print(os.path.join(directory, filename))
                print ("HELLO")
                continue
            else:
                print (filename)
                continue
    def pullInfo(url):
        html = urlopen(url).read().decode('utf-8')
        soup = BeautifulSoup(html,'html.parser')
        print('\n',soup.p)
        print(soup.h1)

    def main():
        # need to find out how to execute this function lol
        go(config.myDir)