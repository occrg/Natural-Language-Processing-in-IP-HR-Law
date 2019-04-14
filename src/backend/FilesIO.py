import os


"""

"""
class FilesIO:

    _dataFolder = 'data/'
    _storeFolder = _dataFolder + 'store/'
    _detailsFile = _storeFolder + 'documentDetails.csv'
    _evaluationsFile = _storeFolder + 'evaluations.csv'
    _pdfFolder = _dataFolder + 'pdf/'
    _pretextFolder = _dataFolder + 'text/before/'
    _textFolder = _dataFolder + 'text/after/'
    _wordsFolder = _dataFolder + 'word/list/'
    _countFolder = _dataFolder + 'word/count/'
    _frequenciesFolder = _dataFolder + 'word/frequency/'


    def exportPoints(self, filepath, Xs, Ys, Zs):
        """

        """
        table = []
        for p in range(len(Xs)):
            table.append("%f, %f, %f" % (Xs[p], Ys[p], Zs[p]))
        newFile = open(filename + '.csv', 'w', errors='replace')
        newFile.write("\n".join(table))
        newFile.close()


    def fillDocumentRecords(self, destination):
        """

        """
        table = []
        table.append("filename,title,journal,date,test,hrRat,ipRat,userRat,creatorRat")
        filePaths = self.__loadListOfFilePaths('data/pdf/')
        for path in filePaths:
            root, filenameAndExt = path.rsplit('/', 1)
            filename, ext = filenameAndExt.split('.')
            table.append("%s,-,-,-,0,0.0,0.0,0.0,0.0" % filename)
        newFile = open(destination, 'w', errors='replace')
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


    def removeDocumentData(self, filename):
        """

        """
        file = open(self._detailsFile, 'r', errors='replace')
        table = []
        for line in file.readlines():
            line = line.replace('\n', '')
            lineFilename, rest = line.split(',', 1)
            if lineFilename != filename:
                table.append(line)
        newFile = open(self._detailsFile, 'w', errors='replace')
        newFile.write("\n".join(table))
        newFile.close()

    def removeAssociatedFiles(self, filename):
        """

        """
        try:
            os.remove(self._pdfFolder + filename + '.pdf')
        except FileNotFoundError as err:
            print(err)
        try:
            os.remove(self._pretextFolder + filename + '.txt')
        except FileNotFoundError as err:
            print(err)
        try:
            os.remove(self._textFolder + filename + '.txt')
        except FileNotFoundError as err:
            print(err)
        try:
            os.remove(self._wordsFolder + filename + '.txt')
        except FileNotFoundError as err:
            print(err)
        try:
            os.remove(self._countFolder + filename + '.txt')
        except FileNotFoundError as err:
            print(err)
        try:
            os.remove(self._frequenciesFolder + filename + '.txt')
        except FileNotFoundError as err:
            print(err)


    def outputDocumentData(self, document):
        """

        """
        file = open(self._detailsFile, 'r', errors='replace')
        table = []
        alreadyLogged = False
        for line in file.readlines():
            line = line.replace('\n', '')
            lineFilename, rest = line.split(',', 1)
            if lineFilename == document.getFilename():
                alreadyLogged = True
                title, journal, date, test, hrRat, ipRat, userRat, creatorRat\
                    = rest.split(',')
                line = '%s,%s,%s,%s,%s,%s,%s,%s,%s' % (                      \
                    document.getFilename(),                                  \
                    document.getPDFmetadata().getTitle(),                    \
                    document.getPDFmetadata().getJournal(),                  \
                    document.getPDFmetadata().getDate(),                     \
                    document.getClassInformation().getTest(),                \
                    document.getClassInformation().getHrRat(),               \
                    document.getClassInformation().getIpRat(),               \
                    document.getClassInformation().getUserRat(),             \
                    document.getClassInformation().getCreatorRat())
            table.append(line)
        if alreadyLogged == False:
            line = '%s,%s,%s,%s,%s,%s,%s,%s,%s' % (                      \
                document.getFilename(),                                  \
                document.getPDFmetadata().getTitle(),                    \
                document.getPDFmetadata().getJournal(),                  \
                document.getPDFmetadata().getDate(),                     \
                document.getClassInformation().getTest(),                \
                document.getClassInformation().getHrRat(),               \
                document.getClassInformation().getIpRat(),               \
                document.getClassInformation().getUserRat(),             \
                document.getClassInformation().getCreatorRat())
            table.append(line)
        newFile = open(self._detailsFile, 'w', errors='replace')
        newFile.write("\n".join(table))
        newFile.close()

    def outputEvaluationData(self, classification):
        """

        """
        testScore = classification.getTestScore()
        crossValScore = classification.getCrossValScore()
        table = []
        table.append(str(testScore))
        table.append(",".join(str(x) for x in crossValScore))
        newFile = open(self._evaluationsFile, 'w', errors='replace')
        newFile.write("\n".join(table))
        newFile.close()

    def retrieveEvaluationData(self):
        """

        """
        crossValScore = []
        try:
            file = open(self._evaluationsFile, 'r', errors='replace')
            lines = file.readlines()
            line0 = lines[0]
            testScore = float(line0.replace('\n', ''))
            line1 = lines[1]
            line1 = line1.replace('\n', '')
            for val in line1.split(','):
                crossValScore.append(float(val))
        except FileNotFoundError as err:
            print(err)
            testScore = 0
            crossValScore.append(0.0)
        return testScore, crossValScore


    def txtFileToString(self, path):
        """

        """
        try:
            file = open('%s' % path, 'r', errors='replace')
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
            file = open(path, 'r', errors='replace')
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
        newFile = open(path, 'w', errors='replace')
        phrases = list(map(str, phrases))
        newFile.write("\n".join(phrases))
        newFile.close()

    def stringToTXTfile(self, text, path):
        """

        """
        newFile = open(path, 'w', errors='replace')
        newFile.write(text + '\n')
        newFile.close()


    def getFileLinesAsList(self):
        """

        """
        file = open(self._detailsFile, 'r', errors='replace')
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
