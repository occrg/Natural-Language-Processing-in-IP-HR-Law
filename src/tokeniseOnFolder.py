import sys
import os

from tokeniseTXT import openTXTfile
from tokeniseTXT import varToCSVwordCount

def tokeniseOnFolder(origin, destinationFolder):
    files = []
    for file in os.listdir(origin):
        filePath = os.path.join(origin, file)
        text = openTXTfile(filePath)
        destination = "%s/%s" % (destinationFolder, file)
        varToCSVwordCount(text, destination)

def main():
        origin = sys.argv[1]
        destination = sys.argv[2]
        if(len(sys.argv) != 3):
            raise ValueError("Wrong number of arguments. There should be 2 (excluding Python file name).")
        tokeniseOnFolder(origin, destination)

if __name__ == '__main__':
    main()
