import sys
import os
from lib.countTXT import folderOfTXTsToCSVs
from lib.combineCSVs import folderToCombined


def tokeniseAll(typesOfDocument, areasOfLaw):
    originFolder = 'TXTs'
    destinationFolder = 'wordCounts'
    for t in typesOfDocument:
        for a in areasOfLaw:
            origin = '%s/%s/%s' % (originFolder, t, a)
            destination = '%s/%s/%s' % (destinationFolder, t, a)
            folderOfTXTsToCSVs(origin, destination)

def combineAll(typesOfDocument, areasOfLaw):
    originFolder = 'wordCounts'
    for t in typesOfDocument:
        for a in areasOfLaw:
            origin = '%s/%s/%s' % (originFolder, t, a)
            folderToCombined(origin)

def main():
    typesOfDocument = ['journals', 'treaties']
    areasOfLaw = ['hr', 'ip']
    if(len(sys.argv) != 1):
        raise ValueError("There should be no arguments (excluding Python file name).")
    tokeniseAll(typesOfDocument, areasOfLaw)
    combineAll(typesOfDocument, areasOfLaw)

if __name__ == '__main__':
    main()
