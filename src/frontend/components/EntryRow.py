from tkinter import *
from tkinter import ttk

import os


"""

"""
class EntryRow:

    _journalOptions = { 'International Journal of Heritage Studies',         \
        'International Journal of Cultural Property', 'Other: Human Rights', \
        'Journal of Intellectual Property Law',                              \
        'Journal of World Intellectual Property',                            \
        'Other: Intellectual Property' }


    def __init__(self, master, entryObj, document, documentList):
        """

        """
        self._master = master


        titleVar = StringVar(self._master)
        titleVar.set(document.getPDFmetadata().getTitle())
        titleEntry = Entry(self._master, width=50, textvariable=titleVar)

        journalVar = StringVar(self._master)
        journalVar.set(document.getPDFmetadata().getJournal())
        journalEntry = OptionMenu(self._master, journalVar, *self._journalOptions)

        dateVar = StringVar(self._master)
        dateVar.set(document.getPDFmetadata().getDate())
        dateEntry = Entry(self._master, width=10, textvariable=dateVar)

        pathEntry = Label(self._master, text="%s" % document.getFilename())

        testVar = IntVar()
        testCheck = Checkbutton(self._master, var=testVar)
        if document.getClassInformation().getTest():
            testCheck.select()
        testCheck.bind("<Button-1>", lambda event, testVar=testVar:self.__getInt(event, testVar))

        confirmButton = Button(self._master, text="Confirm Changes", command=lambda: self.__confirmEntry(titleVar, dateVar, journalVar, testVar, document))
        removeButton = Button(self._master, text="Remove", command=lambda: self.__removeEntry(entryObj, document, documentList))
        openButton = Button(self._master, text="Open", command=lambda: self.__openPDF('data/pdf/' + document.getFilename() + '.pdf'))

        titleEntry.grid(row=0, column=0, padx=15, pady=1)
        journalEntry.grid(row=0, column=1, padx=15, pady=1)
        dateEntry.grid(row=0, column=2, padx=15, pady=1)
        testCheck.grid(row=0, column=3, padx=15, pady=1)
        pathEntry.grid(row=0, column=4, padx=15, pady=1)
        confirmButton.grid(row=0, column=5, padx=15, pady=1)
        removeButton.grid(row=0, column=6, padx=15, pady=1)
        openButton.grid(row=0, column=7, padx=15, pady=1)


    def __getInt(self, event, var):
        return var.get()

    def __confirmEntry(self, titleVar, dateVar, journalVar, testVar, document):
        document.makeFormChanges(titleVar.get(), dateVar.get(), journalVar.get(), testVar.get())

    def __removeEntry(self, entryObj, document, documentList):
        documentList.removeDocument(document)
        document.removeData()
        self._master.destroy()
        entryObj.decrementRows()

    def __openPDF(self, pdfPath):
        os.system('xdg-open %s' % pdfPath)
