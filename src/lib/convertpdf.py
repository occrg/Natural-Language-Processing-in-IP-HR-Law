"""
Supplies functionality that converts a PDF to a string.
"""

import os

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO

def getPDFmetadata(path):
    """
    Attempts to retrieve the title and date of a PDF document.
    If a title cannot be retrieved, the path of its PDF is used as its
    title instead.
    If a date cannnot be retrieved, its date of its
    modification on the current filesystem is used (most often when it
    was downloaded).

    Arguments:
    path   (str) -- the path of the pdf file that needs its data
                    extracted

    Returns:
    date   (str) -- the creation date or, failing that, the
                    modification date of the PDF
    title  (str) -- the title or, failing that, the path of the
                    document's PDF
    """
    fp = open(path, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser)
    parser.set_document(doc)
    if 'CreationDate' in doc.info[0]:
        date = doc.info[0]['CreationDate']
        date = date.decode(encoding="utf-8", errors='ignore')
    else:
        date = os.path.getmtime(path)
    if 'Title' in doc.info[0]:
        title = doc.info[0]['Title']
        title = title.decode(encoding="utf-8", errors='ignore')
        title = title.replace(',', '')
    else:
        title = path
    return date, title

def pdfToString(path, start=0, end=0):
    """
    Converts a PDF to a plaintext txt file.

    Arguments:
    path   (str) -- the path of the pdf file that needs to be converted
    start  (int) -- the first page of the pdf document that should be
                    converted (default: 0)
    end    (int) -- the last page of the pdf document that should be
                    converted. 0 represents that last page of the
                    document here (default: 0)

    Returns:
    text   (str) -- the converted form of the PDF document
    """
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device =                                                                 \
        TextConverter(rsrcmgr, retstr, codec = codec, laparams = laparams)

    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    if (start == 0 and end == 0):
        for page in PDFPage.get_pages(                                       \
            fp, pagenos, maxpages = maxpages, password = password,           \
            caching = caching, check_extractable = True):
            interpreter.process_page(page)
    else:
        n = 1
        for page in PDFPage.get_pages(                                       \
            fp, pagenos, maxpages = maxpages, password = password,           \
            caching = caching, check_extractable = True):
            if n in range(start, end + 1):
                interpreter.process_page(page)
            n += 1

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()

    return text
