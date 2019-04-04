import os


"""

"""
class FilesIO:

    _dataFolder = 'data/'
    _detailsFile = _dataFolder + 'documentDetails.csv'


    def fillDocumentRecords(self, destination):
        table = []
        table.append("filename,title,journal,date,test,hrRat,ipRat,userRat,creatorRat")
        filePaths = self.__loadListOfFilePaths('data/pdf/')
        for path in filePaths:
            root, filenameAndExt = path.rsplit('/', 1)
            filename, ext = filenameAndExt.split('.')
            table.append("%s,-,-,-,-,-,-,-,-" % filename)
        newFile = open(destination, 'w')
        newFile.write("\n".join(table))
        newFile.close()


    def __loadListOfFilePaths(self, folder):
        """

        """
        filePaths = []
        for file in os.listdir(folder):
            if '.' in file:
                path = os.path.join(folder, file)
                filePaths.append(path)
        return filePaths

    def outputDocumentData(self, filename, document):
        """

        """
        file = open(self._detailsFile, 'r')
        table = []
        for line in file.readlines():
            line = line.replace('\n', '')
            lineFilename, rest = line.split(',', 1)
            if lineFilename == filename:
                title, journal, date, test, hrRat, ipRat, userRat, creatorRat\
                    = rest.split(',')
                line = '%s,%s,%s,%s,%s,%s,%s,%s,%s' % (filename,             \
                    document.getPDFmetadata().getTitle(),                    \
                    document.getPDFmetadata().getJournal(),                  \
                    document.getPDFmetadata().getDate(),                     \
                    document.getClassInformation().getTest(),                \
                    document.getClassInformation().getHrRat(),               \
                    document.getClassInformation().getIpRat(),               \
                    document.getClassInformation().getUserRat(),             \
                    document.getClassInformation().getCreatorRat())
            table.append(line)
        newFile = open(self._detailsFile, 'w')
        newFile.write("\n".join(table))
        newFile.close()


    def txtFileToString(self, path):
        """

        """
        try:
            file = open('%s' % path, 'r')
            lines = []
            for line in file.readlines():
                lines.append(line)
                text = ''.join(lines)
                file.close()
        except FileNotFoundError:
            text = "-"
        return text

    def lineSeparatedToList(self, path):
        """

        """
        try:
            file = open(path, 'r')
            phrases = []
            for line in file.readlines():
                newline = line.replace('\n', '')
                phrases.append(newline)
            file.close()
        except FileNotFoundError:
            phrases = []
        return phrases

    def listToLineSeparated(self, phrases, path):
        """

        """
        newFile = open(path, 'w')
        phrases = list(map(str, phrases))
        newFile.write("\n".join(phrases))
        newFile.close()

    def stringToTXTfile(self, text, path):
        """

        """
        newFile = open(path, 'w')
        newFile.write(text + '\n')
        newFile.close()


    def getFileLinesAsList(self):
        """

        """
        file = open(self._detailsFile, 'r')
        lines = []
        for line in file.readlines():
            line = line.replace('\n', '')
            lines.append(line)
        file.close()
        return lines

    def __loadListOfFilenames(self, folder):
        """

        """
        names = []
        for file in os.listdir(folder):
            if '.' in file:
                path = os.path.join(folder, file)
                root, name = path.rsplit('/', 1)
                name, ext = name.split('.')
                names.append(name)
        return names
