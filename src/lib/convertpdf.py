"""
Supplies functionality that converts a PDF to a string.
"""

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO


def pdfToString(path, start=0, end=0):
    """
    Converts a PDF to a string.

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
