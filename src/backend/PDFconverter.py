import re
import datetime

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO


"""

"""
class PDFconverter:

    _dataFolder = 'data/'
    _pdfFolder = _dataFolder + 'pdf/'


    def pdfToString(self, filename):
        """

        """
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(                                              \
            rsrcmgr, retstr, codec = codec, laparams = laparams)

        fp = open(self._pdfFolder + filename + '.pdf', 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()

        for page in PDFPage.get_pages(                                       \
            fp, pagenos, maxpages = maxpages, password = password,           \
            caching = caching, check_extractable = True):
            interpreter.process_page(page)

        text = retstr.getvalue()

        fp.close()
        device.close()
        retstr.close()

        return text


    def removeMetadataFromText(self, text, journal):
        """

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
            text = re.sub(r'(IJCP[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
        elif journal == "Journal of World Intellectual Property":
            text = re.sub(r'(\d{4} The Author. Journal Compilation)', '', text, flags=re.IGNORECASE)
            text = re.sub(r'(\d{4} Blackwell Publishing Ltd[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
            text = re.sub(r'(JOURNAL OF WORLD INTELLECTUAL PROPERTY)', '', text, flags=re.IGNORECASE)
        elif journal == "Journal of Intellectual Property Law":
            text = re.sub(r'(\nl\n\nD\no\nw\nn[\w\W]+?[\n ]{7})', '', text, flags=re.IGNORECASE)
            text = re.sub(r'(Journal of Intellectual Property Law & Practice[\n ,\d]*?Vol.[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
            text = re.sub(r'(doi[\w\W]*?[\n]*?Advance Access Publication[\w\W]*?\n\n)', '', text, flags=re.IGNORECASE)
        return text

    def substituteKerning(self, text):
        """

        """
        text = text.replace('ﬁ ', 'fi')
        text = text.replace('(cid:222)', 'fi')
        text = text.replace('(cid:223)', 'fl')
        text = text.replace('ﬁ ', 'fi')
        text = text.replace('ﬂ ', 'fl')
        text = text.replace('ﬀ ', 'ff')
        return text


    def extractJournalFromText(self, journal, text, filename):
        """

        """
        if journal == "-":
            if re.match(r'^International Journal of Heritage Studies', text):
                journal = "International Journal of Heritage Studies"
                period = "97-"
            elif re.search(r'International Cultural Property Society', text):
                journal = "International Journal of Cultural Property"
                period = "98-"
            elif re.search(r'Downloaded from https://www.cambridge.org/core.[\w\W]+, subject to the Cambridge Core terms of', text) != None:
                journal = "International Journal of Cultural Property"
                period = "92-97"
            elif re.search(r'JOURNAL OF WORLD INTELLECTUAL PROPERTY', text) != None:
                journal = "Journal of World Intellectual Property"
                period = "98-05"
            elif re.search(r'The Journal of World Intellectual Property', text) != None:
                journal = "Journal of World Intellectual Property"
                period = "06-"
            elif re.search(r'Journal of Intellectual Property Law & Practice', text) != None:
                journal = "Journal of Intellectual Property Law"
                period = "05-"
            else:
                period = "-"
        else:
            if re.match(r'^International Journal of Heritage Studies', text):
                period = "97-"
            elif re.search(r'International Cultural Property Society', text):
                period = "98-"
            elif re.search(r'Downloaded from https://www.cambridge.org/core.[\w\W]+, subject to the Cambridge Core terms of', text) != None:
                period = "92-97"
            elif re.search(r'JOURNAL OF WORLD INTELLECTUAL PROPERTY', text) != None:
                period = "98-05"
            elif re.search(r'The Journal of World Intellectual Property', text) != None:
                period = "06-"
            elif re.search(r'Journal of Intellectual Property Law & Practice', text) != None:
                period = "05-"
            else:
                period = "-"
        return journal, period


    def extractTitleFromText(self, journal, period, text):
        """

        """
        try:
            title = "-"
            if journal == "International Journal of Heritage Studies":
                titleSearch = re.search(r'To cite this article:[\w\W]+?\) (.+?),[\n ]*?International', text, flags=re.DOTALL)
                title = titleSearch.group(1)
            elif journal == "International Journal of Cultural Property":
                if period == "92-97":
                    title = "-"
                if period == "98-":
                    title = "-"
            elif journal == "Journal of World Intellectual Property":
                if period == "98-05":
                    title = "-"
                if period == "06-":
                    title = "-"
            elif journal == "Journal of Intellectual Property Law":
                titleSearch = re.search(r'\n[\w\W]*?\d+\n\n(.+?\*)', text, flags=re.DOTALL)
                title = titleSearch.group(1)
        except AttributeError as err:
            print(err)
        return title

    def getTitleFromPDFmetadata(self, filename):
        """

        """
        fp = open(self._pdfFolder + filename + '.pdf', 'rb')
        parser = PDFParser(fp)
        doc = PDFDocument(parser)
        parser.set_document(doc)
        if 'Title' in doc.info[0]:
            title = doc.info[0]['Title']
            title = title.decode(encoding="utf-8", errors='ignore')
            title = title.replace(',', '')
            if title == "No Job Name" or title == "untitled"                 \
                or title == "None" or title == "" or '.' in title:
                title = "-"
        else:
            title = "-"
        fp.close()
        return title

    def extractDateFromText(self, journal, period, text):
        """

        """
        try:
            date = "-"
            if journal == "International Journal of Heritage Studies":
                dateSearch = re.search(r'To cite this article:[\w\W]*?\((\d{4})\)\s', text, flags=re.DOTALL)
                dateString = dateSearch.group(1)
                date = datetime.datetime(int(dateString), 6, 15).date()
            elif journal == "International Journal of Cultural Property":
                if period == "92-97":
                    date = "-1"
                if period == "98-":
                    dateSearch = re.search(r'(\d{4}) International Cultural Property Society', text)
                    dateString = dateSearch.group(1)
                    date = datetime.datetime(int(dateString), 6, 15).date()
            elif journal == "Journal of World Intellectual Property":
                if period == "98-05":
                    date = "-1"
                if period == "06-":
                    date = "-"
            elif journal == "Journal of Intellectual Property Law":
                date = "-"
            else:
                date = "-1"
        except AttributeError as err:
            print(err)
        return date

    def getDateFromPDFmetadata(self, filename, date, journal):
        """

        """
        if date == "-":
            updateDate = True
        elif date == "-1":
            updateDate = False
            date = "-"
        else:
            rightDatesIJHS = journal == "International Journal of Heritage Studies" and date > datetime.datetime(2001, 1, 1).date()
            rightDatesIJCP = journal == "International Journal of Cultural Property" and date > datetime.datetime(2001, 1, 1).date()
            updateDate = rightDatesIJHS or rightDatesIJCP
        if updateDate:
            fp = open(self._pdfFolder + filename + '.pdf', 'rb')
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
            fp.close()
        return date
