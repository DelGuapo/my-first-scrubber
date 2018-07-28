#Core
import time
import sys

def wait(nSeconds,printWait = True):
    for x in range (0,nSeconds):
        if printWait:
            sys.stdout.write('.')    
        time.sleep(1)
