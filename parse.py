import os

class parse:
    """
    This class parses files on local directory
    """
    def go(myDir):
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
