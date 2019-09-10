from backend.FilesIO import FilesIO
from backend.DocumentList import DocumentList
from frontend.UI import UI

"""

"""
class App:

    io = FilesIO()

    def __init__(self):
        # self.io.fillDocumentRecords('data/store/documentDetails.csv')
        self._documentList = DocumentList()
        self._ui = UI('HR-IP Analysis', self._documentList)


def main():
    app = App()

if __name__ == '__main__':
    main()
