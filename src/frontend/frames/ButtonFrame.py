from tkinter import *
from tkinter import ttk, filedialog

import shutil

from frontend.tabs.VisualisationTab import VisualisationTab
# from frontend.popups.TestDataOptionsFrame import TestDataOptionsFrame
from backend.Document import Document


"""

"""
class ButtonFrame:

    _dataFolder = 'data/'
    _pdfFolder = _dataFolder + 'pdf/'


    def __init__(self, master, entryObj, uiObj, documentList):
        """

        """
        self._master = master

        self._master.grid_rowconfigure(0, weight=1)
        self._master.grid_rowconfigure(1, weight=1)
        self._master.grid_rowconfigure(2, weight=1)
        self._master.grid_columnconfigure(0, weight=1)


        addButton = Button(self._master, text="Add Document", command=lambda: self.__addDocument(documentList, entryObj, uiObj))
        # testButton = Button(self._master, text="Change Test Data", command=lambda: TestDataOptionsFrame())
        trainButton = Button(self._master, text="Train Data", command=lambda: self.__trainDataCall(documentList, uiObj))

        addButton.grid(row=1, column=1, padx=15, sticky = "nse")
        # testButton.grid(row=1, column=2, padx=15, sticky = "nse")
        trainButton.grid(row=1, column=3, padx=15, sticky = "nse")


    def __addDocument(self, documentList, entryObj, uiObj):
        """

        """
        filePath = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
        rest, filenameAndExt = filePath.rsplit('/', 1)
        shutil.copy2(filePath, self._pdfFolder + filenameAndExt)
        filename, ext = filenameAndExt.split('.')
        document = Document(filename, "-", "-", "-", 1, -1.0, -1.0, -1.0, -1.0)
        documentList.addDocument(document)
        entryObj.addDocumentRow(document, documentList)
        

    def __trainDataCall(self, documentList, uiObj):
        """

        """
        documentList.performClassifications()
        documentList.performVisualisations()
        notebook = uiObj.getNotebook()
        notebook.forget(0)
        VisualisationTab(uiObj.addTab('Visualisations'), documentList.getGraphs())
        notebook.select(1)
