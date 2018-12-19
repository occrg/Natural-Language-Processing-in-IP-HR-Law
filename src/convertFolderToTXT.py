import sys
import os

from convertPDFtoTXT import pdfToTextVar
from lib.filesInOut import textVarToTXTfile

def PDFfolderToTXTfile(originFolder):
    for file in os.listdir(originFolder):
        filePath = os.path.join(originFolder, file)
        text = pdfToTextVar(filePath, 0, 0)
        first, rest = filePath.split('/', 1)
        first = 'TXTs'
        destinationWrongExt = os.path.join(first, rest)
        path, ext = destinationWrongExt.split('.')
        ext = 'txt'
        destination = '%s.%s' % (path, ext)
        textVarToTXTfile(text, destination)


def main():
    if (len(sys.argv) == 2):
        origin = sys.argv[1]
        PDFfolderToTXTfile(origin)
    else:
        raise ValueError("Wrong number of arguments (%i given). There should be 2 or 4 (excluding Python file name)." % (len(sys.argv) - 1))

if __name__ == '__main__':
    main()
