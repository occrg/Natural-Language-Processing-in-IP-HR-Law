import os


"""

"""
class FilesIO:

    _dataFolder = 'data/'
    _storeFolder = _dataFolder + 'store/'
    _detailsFile = _storeFolder + 'documentDetails.csv'
    _visualisationEvaluationFile =                                           \
        _storeFolder + 'visualisationEvaluationData.csv'
    _crossValEvauluationFile = _storeFolder + 'crossValEvaluationData.csv'
    _pdfFolder = _dataFolder + 'pdf/'
    _pretextFolder = _dataFolder + 'text/before/'
    _textFolder = _dataFolder + 'text/after/'
    _wordsFolder = _dataFolder + 'word/'
    _featureFolder = _wordsFolder + 'feature/'
    _countFolder = _wordsFolder + 'count/'
    _tfFolder = _wordsFolder + 'tf/'
    _idfFolder = _wordsFolder + 'idf/'
    _tfidfFolder = _wordsFolder + 'tfidf/'
    _tfidfcfFolder = _wordsFolder + 'tfidfcf/'


    def exportPoints(self, filepath, Xs, Ys, Zs):
        """


        Arguments:
        filepath (string)
            --
        Xs       ([float])
            --
        Ys       ([float])
            --
        Zs       ([float])
            --
        """
        table = []
        for p in range(len(Xs)):
            table.append("%f, %f, %f" % (Xs[p], Ys[p], Zs[p]))
        newFile = open(filename + '.csv', 'w', errors='replace')
        newFile.write("\n".join(table))
        newFile.close()


    def fillDocumentRecords(self, destination):
        """


        Arguments:
        destination (string)
            --
        """
        table = []
        table.append(                                                        \
            "filename,title,journal,date,test,hrRat,ipRat,userRat,creatorRat")
        filePaths = self.__loadListOfFilePaths(self._pdfFolder)
        for path in filePaths:
            root, filenameAndExt = path.rsplit('/', 1)
            filename, ext = filenameAndExt.split('.')
            table.append("%s,-,-,-,0,0.0,0.0,0.0,0.0" % filename)
        newFile = open(destination, 'w', errors='replace')
        newFile.write("\n".join(table))
        newFile.close()


    def __loadListOfFilePaths(self, folder):
        """


        Arguments:
        folder (string)
            --
        """
        filePaths = []
        for file in os.listdir(folder):
            if '.' in file:
                path = os.path.join(folder, file)
                filePaths.append(path)
        return filePaths


    def removeDocumentData(self, filename):
        """


        Arguments:
        filename (string)
            --
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


        Arguments:
        filename (string)
            --
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
            os.remove(self._featureFolder + filename + '.txt')
        except FileNotFoundError as err:
            print(err)
        try:
            os.remove(self._countFolder + filename + '.txt')
        except FileNotFoundError as err:
            print(err)
        try:
            os.remove(self._tfFolder + filename + '.txt')
        except FileNotFoundError as err:
            print(err)
        try:
            os.remove(self._idfFolder + filename + '.txt')
        except FileNotFoundError as err:
            print(err)
        try:
            os.remove(self._tfidfFolder + filename + '.txt')
        except FileNotFoundError as err:
            print(err)
        try:
            os.remove(self._tfidfcfFolder + filename + '.txt')
        except FileNotFoundError as err:
            print(err)


    def outputDocumentData(self, document):
        """


        Arguments:
        document (Document)
            --
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
            line = '%s,%s,%s,%s,%s,%s,%s,%s,%s' % (                          \
                document.getFilename(),                                      \
                document.getPDFmetadata().getTitle(),                        \
                document.getPDFmetadata().getJournal(),                      \
                document.getPDFmetadata().getDate(),                         \
                document.getClassInformation().getTest(),                    \
                document.getClassInformation().getHrRat(),                   \
                document.getClassInformation().getIpRat(),                   \
                document.getClassInformation().getUserRat(),                 \
                document.getClassInformation().getCreatorRat())
            table.append(line)
        newFile = open(self._detailsFile, 'w', errors='replace')
        newFile.write("\n".join(table))
        newFile.close()

    def outputVisualisationEvaluationData(self, classification):
        """


        Arguments:
        classification (Classification)
            --
        """
        testScore = classification.getTestScore()
        tp, tn, fp, fn = classification.getTFPNs()
        table = []
        table.append(str(testScore))
        table.append("%s,%s,%s,%s" % (tp, tn, fp, fn))
        newFile =                                                            \
            open(self._visualisationEvaluationFile, 'w', errors='replace')
        newFile.write("\n".join(table))
        newFile.close()

    def retrieveVisualisationEvaluationData(self):
        """


        Returns:
        testScore (float)
            --
        tp        (int)
            --
        tn        (int)
            --
        fp        (int)
            --
        fn        (int)
            --
        """
        crossValScore = []
        try:
            file = open(                                                     \
                self._visualisationEvaluationFile, 'r', errors='replace')
            lines = file.readlines()
            line0 = lines[0]
            testScore = float(line0.replace('\n', ''))
            line1 = lines[1]
            line1 = line1.replace('\n', '')
            tpStr, tnStr, fpStr, fnStr = line1.split(',')
            tp = int(tpStr)
            tn = int(tnStr)
            fp = int(fpStr)
            fn = int(fnStr)
        except FileNotFoundError as err:
            print(err)
            testScore = 0
            tp = 0
            tn = 0
            fp = 0
            fn = 0
        return testScore, tp, tn, fp, fn

    def outputCrossValEvaluationData(self, crossValidation):
        """


        Arguments:
        crossValidation (CrossValidation)
            --
        """
        table = []
        crossValScore = crossValidation.getCrossValScore()
        trendsCrossVal = crossValidation.getTrendsCrossVal()
        table.append(",".join(str(x) for x in crossValScore))
        for trend in trendsCrossVal:
            table.append(",".join(str(x) for x in trend))
        newFile = open(self._crossValEvauluationFile, 'w', errors='replace')
        newFile.write("\n".join(table))
        newFile.close()

    def retrieveCrossValEvaluationData(self):
        """


        Returns:
        crossValScore  (float)
            --
        trendsCrossVal ([float])
            --
        """
        crossValScore = []
        trendsCrossVal = []
        try:
            file = open(self._crossValEvauluationFile, 'r', errors='replace')
            lines = file.readlines()
            line0 = lines[0]
            line0 = line0.replace('\n', '')
            for val in line0.split(','):
                crossValScore.append(float(val))
            for line in lines[1:]:
                trend = []
                for val in line.split(','):
                    trend.append(float(val))
                trendsCrossVal.append(trend)

        except FileNotFoundError as err:
            print(err)
            crossValScore.append(0.0)
            trendsCrossVal.append([0.0])
            trendsCrossVal.append([0.0])
            trendsCrossVal.append([0.0])
            trendsCrossVal.append([0.0])
        return crossValScore, trendsCrossVal

    def txtFileToString(self, path):
        """


        Arguments:
        path (string)
            --

        Returns:
        text (string)
            --
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


        Arguments:
        path (string)
            --

        Returns:
        phrases ([string])
            --
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


        Arguments:
        text (string)
            --
        path (string)
            --
        """
        newFile = open(path, 'w', errors='replace')
        newFile.write(text + '\n')
        newFile.close()


    def getFileLinesAsList(self):
        """


        Returns:
        lines ([string])
            --
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


        Arguments:
        folder (string)
            --

        Returns:
        names (sting)
            -- 
        """
        names = []
        for file in os.listdir(folder):
            if '.' in file:
                path = os.path.join(folder, file)
                root, name = path.rsplit('/', 1)
                name, ext = name.split('.')
                names.append(name)
        return names
