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
        'Other: Intellectual Property', '-' }


    def __init__(self, master, entryObj, document, documentList):
        """

        """
        self._master = master

        self._document = document


        self._titleVar = StringVar(self._master)
        self._titleVar.set(self._document.getPDFmetadata().getTitle())
        titleEntry = Entry(self._master, width=50, textvariable=self._titleVar)

        self._journalVar = StringVar(self._master)
        self._journalVar.set(self._document.getPDFmetadata().getJournal())
        journalEntry = OptionMenu(self._master, self._journalVar, *self._journalOptions)

        self._dateVar = StringVar(self._master)
        self._dateVar.set(self._document.getPDFmetadata().getDate())
        dateEntry = Entry(self._master, width=10, textvariable=self._dateVar)

        pathEntry = Label(self._master, text="%s" % self._document.getFilename())

        self._testVar = IntVar()
        testCheck = Checkbutton(self._master, var=self._testVar)
        if self._document.getClassInformation().getTest():
            testCheck.select()
        testCheck.bind("<Button-1>", lambda event, testVar=self._testVar:self.__getInt(event, testVar))

        confirmButton = Button(self._master, text="Confirm Changes", command=lambda: self.confirmEntry())
        removeButton = Button(self._master, text="Remove", command=lambda: self.__removeEntry(entryObj, documentList))
        openButton = Button(self._master, text="Open", command=lambda: self.__openPDF('data/pdf/' + self._document.getFilename() + '.pdf'))

        titleEntry.grid(row=0, column=0, padx=15, pady=1)
        journalEntry.grid(row=0, column=1, padx=15, pady=1)
        dateEntry.grid(row=0, column=2, padx=15, pady=1)
        testCheck.grid(row=0, column=3, padx=15, pady=1)
        pathEntry.grid(row=0, column=4, padx=15, pady=1)
        confirmButton.grid(row=0, column=5, padx=15, pady=1)
        removeButton.grid(row=0, column=6, padx=15, pady=1)
        openButton.grid(row=0, column=7, padx=15, pady=1)

    def setTestVar(self, val):
        """

        """
        self._testVar.set(val)

    def __getInt(self, event, var):
        return var.get()

    def confirmEntry(self):
        self._document.makeFormChanges(self._titleVar.get(), self._dateVar.get(), self._journalVar.get(), self._testVar.get())

    def __removeEntry(self, entryObj, documentList):
        documentList.removeDocument(self._document)
        self._document.removeData()
        entryObj.removeRowFromList(self._master)
        self._master.destroy()

    def __openPDF(self, pdfPath):
        os.system('xdg-open %s' % pdfPath)
