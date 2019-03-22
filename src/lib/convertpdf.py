"""
Supplies functionality that converts a PDF to a string.
"""

import re
import os
import datetime

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
    path   (str)  -- the path of the pdf file that needs its data
                     extracted

    Returns:
    date   (date) -- the creation date or, failing that, the
                     modification date of the PDF
    title  (str)  -- the title or, failing that, the path of the
                     document's PDF
    """
    fp = open(path, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser)
    parser.set_document(doc)
    if 'CreationDate' in doc.info[0]:
        date = doc.info[0]['CreationDate']
        date = date.decode(encoding="utf-8", errors='ignore')
        year = date[2:6]
        month = date[6:8]
        day = date[8:10]
        stringDate = day + month + year
        date = datetime.datetime.strptime(stringDate, '%d%m%Y').date()
    else:
        dateEpoch = os.path.getmtime(path)
        stringDate = datetime.datetime.fromtimestamp(dateEpoch).strftime('%Y-%m-%d %H:%M:%S')
        date = datetime.datetime.strptime(stringDate, '%Y-%m-%d %H:%M:%S').date()

    if 'Title' in doc.info[0]:
        title = doc.info[0]['Title']
        title = title.decode(encoding="utf-8", errors='ignore')
        title = title.replace(',', '')
        if title == "No Job Name":
            title = "-"
        if '.' in title:
            title = "-"
    else:
        title = "-"
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

def extractMetadataFromText(path, text, date, title):
    """
    Extracts metadata from the text itself when the metadata from the
    PDF is innacurate.

    Arguments:
    path     (str)
            -- the path of the PDF file that's information is to be
               extracted. This is used to highlight which files have
               not been categorised.
    text     (str)
            -- the text of the PDF file that's information is to be
               extracted.
    date     (datetime)
            -- the date that the PDF file had in its metadata
    title    (str)
            -- the title that the PDF file had in its metadata

    Returns:
    date     (datetime)
            -- if the argument ${date} appeared to be correct, then the
               argument is returned as it is. If not, a year is
               extracted from the text of the file and YEAR-01-01 is
               returned
    title    (str)
            -- if the argument ${title} is not "-", then the
               argument is returned as it is. If it is "-", a title is
               extracted from the text of the file
    journal  (str)
            -- a journal is assigned to the document based on the
               typical format of documents in each journal
    """
    journal = "-"
    try:
        if re.match(r'^International Journal of Heritage Studies', text):
            journal = "International Journal of Heritage Studies"
            titleSearch = re.search(r'To cite this article:[\w\W]+?\) (.+?),[\n ]*?International', text, flags=re.DOTALL)
            title = titleSearch.group(1)
            if date < datetime.datetime(2003, 1, 1).date():
                dateSearch = re.search(r'To cite this article:[\w\W]*? \((\d{4})\)\s', text, flags=re.DOTALL)
                dateString = dateSearch.group(1)
                date = datetime.datetime(int(dateString), 1, 1).date()
        elif re.search(r'International Cultural Property Society', text):
            journal = "International Journal of Cultural Property"
            if date < datetime.datetime(2005, 1, 1).date():
                dateSearch = re.search(r'(\d{4}) International Cultural Property Society', text)
                dateString = dateSearch.group(1)
                date = datetime.datetime(int(dateString), 1, 1).date()
        elif re.search(r'Downloaded from https://www.cambridge.org/core.[\w\W]+, subject to the Cambridge Core terms of', text) != None:
            journal = "International Journal of Cultural Property"
            date = "-"
        elif re.search(r'JOURNAL OF WORLD INTELLECTUAL PROPERTY', text) != None:
            journal = "Journal of World Intellectual Property"
            date = "-"
        elif re.search(r'The Journal of World Intellectual Property', text) != None:
            journal = "Journal of World Intellectual Property"
        elif re.search(r'Journal of Intellectual Property Law & Practice', text) != None:
            journal = "Journal of Intellectual Property Law"
            titleSearch = re.search(r'\n[\w\W]*?\d+\n\n(.+?\*)', text, flags=re.DOTALL)
            title = titleSearch.group(1)
    except AttributeError as error:
        print('Path:', path)
        print(error)


    title = title.replace(',', '')
    title = title.replace('\n ', ' ')
    title = title.replace('\n', '')
    return date, title, journal

def removeMetadataFromText(text, journal):
    """
    Remvoes text from a document that is not part of the main body of
    the text and that could give away what class the document is based
    on the format of the document alone.

    Arguments:
    text     (str)
            -- the text that is to have parts removed
    journal  (str)
            -- the journal that the text has come from. Used to
               indicate what text should be removed

    Returns:
    text     (str)
            -- the text with parts removed
    """
    if journal == "International Journal of Heritage Studies":
        text = re.sub(r'([\w\W]*?Full Terms[\w\W]*?https[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
        text = re.sub(r'(ISSN[\w\W]*?\n\n)', '', text)
        text = re.sub(r'(International Journal of Heritage Studies[\n ,\d]*?Vol.[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
        text = re.sub(r'(International Journal of Heritage Studies)', '', text, flags=re.IGNORECASE)
        text = re.sub(r'(KEYWORDS[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
        text = re.sub(r'(ARTICLE HISTORY[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
        text = re.sub(r'([\w\W]*?IJHS[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
    elif journal == "International Journal of Cultural Property":
        text = re.sub(r'(Downloaded from https://www.cambridge.org/core.[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
        text = re.sub(r'(International Journal of Cultural Property[\n ,\d]*?Vol.[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
        text = re.sub(r'(International Cultural Property Society[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
        text = re.sub(r'(International Journal of Cultural Property)', '', text, flags=re.IGNORECASE)
        text = re.sub(r'([\w\W]*?IJCP[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
    elif journal == "Journal of World Intellectual Property":
        text = re.sub(r'(\d{4} The Author. Journal Compilation)', '', text, flags=re.IGNORECASE)
        text = re.sub(r'(\d{4} Blackwell Publishing Ltd[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
        text = re.sub(r'(JOURNAL OF WORLD INTELLECTUAL PROPERTY)', '', text, flags=re.IGNORECASE)
    elif journal == "Journal of Intellectual Property Law":
        text = re.sub(r'(\nl\n\nD\no\nw\nn[\w\W]+?[\n ]{7})', '', text, flags=re.IGNORECASE)
        text = re.sub(r'(Journal of Intellectual Property Law & Practice[\n ,\d]*?Vol.[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
        text = re.sub(r'(doi[\w\W]*?[\n]*?Advance Access Publication[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
    return text
