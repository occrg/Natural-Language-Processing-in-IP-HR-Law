import sys

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO

def pdfToTextVar(path, start, end):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec = codec, laparams = laparams)

    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    if (start == 0 and end == 0):
        for page in PDFPage.get_pages(fp, pagenos, maxpages = maxpages, password = password, caching = caching, check_extractable = True):
            interpreter.process_page(page)
    else:
        n = 1
        for page in PDFPage.get_pages(fp, pagenos, maxpages = maxpages, password = password, caching = caching, check_extractable = True):
            if n in range(start, end + 1):
                interpreter.process_page(page)
            n += 1

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()

    return text

def textVarToTXTfile(text, file):
    filename, format = file.split(".")
    newFile = open('%s.txt' % filename, 'w')
    newFile.write('%s' % text + '\n')
    newFile.close()

def main():
    file = sys.argv[1]
    origin = 'PDFs/%s' % file
    destination = 'TXTs/%s' % file
    try:
        text = pdfToTextVar(origin, int(sys.argv[2]), int(sys.argv[3]))
    except IndexError:
        text = pdfToTextVar(origin, 0, 0)
    textVarToTXTfile(text, destination)

if __name__ == '__main__':
    main()
