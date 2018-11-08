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

def pdfToTextVar(path):
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

    for page in PDFPage.get_pages(fp, pagenos, maxpages = maxpages, password = password, caching = caching, check_extractable = True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()

    return text

def textVarToTXTfile(text, path):
    filename, format = path.split(".")
    newFile = open('%s.txt' % filename, 'w')
    newFile.write('%s' % text + '\n')
    newFile.close()

def main():
    path = sys.argv[1]
    text = pdfToTextVar(path)
    textVarToTXTfile(text, path)

if __name__ == '__main__':
    main()
