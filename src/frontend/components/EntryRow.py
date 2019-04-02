from tkinter import *
from tkinter import ttk

import os


"""

"""
class EntryRow:
    def __init__(self, master, r, document):
        """

        """
        self._master = master


        journalOptions = { 'International Journal of Heritage Studies',          \
            'International Journal of Cultural Property', 'Other: Human Rights', \
            'Journal of Intellectual Property Law',                              \
            'Journal of World Intellectual Property',                            \
            'Other: Intellectual Property' }


        titleEntry = Entry(self._master, width=50)
        titleEntry.insert(0, "%s" % document.getPDFmetadata().getTitle())
        journalsVar = StringVar(self._master, '%s' % document.getPDFmetadata().getJournal())
        journalEntry = OptionMenu(self._master, journalsVar, *journalOptions)
        dateEntry = Entry(self._master, width=10)
        dateEntry.insert(0, '%s' % document.getPDFmetadata().getDate())
        pathEntry = Label(self._master, text="%s" % document.getFilename())
        testVar = IntVar(self._master, 1)
        testCheck = Checkbutton(self._master, var=testVar)
        confirmButton = Button(self._master, text="Confirm Changes")
        removeButton = Button(self._master, text="Remove")
        openButton = Button(self._master, text="Open", command=lambda: self.__openPDF('data/pdf/' + document.getFilename() + '.pdf'))

        titleEntry.grid(row=r, column=0, padx=15, pady=1)
        journalEntry.grid(row=r, column=1, padx=15, pady=1)
        dateEntry.grid(row=r, column=2, padx=15, pady=1)
        testCheck.grid(row=r, column=3, padx=15, pady=1)
        pathEntry.grid(row=r, column=4, padx=15, pady=1)
        confirmButton.grid(row=r, column=5, padx=15, pady=1)
        removeButton.grid(row=r, column=6, padx=15, pady=1)
        openButton.grid(row=r, column=7, padx=15, pady=1)


    def __openPDF(self, pdfPath):
        os.system('xdg-open %s' % pdfPath)
