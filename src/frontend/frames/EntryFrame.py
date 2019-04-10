from tkinter import *
from tkinter import ttk

import random

from frontend.components.EntryRow import EntryRow


"""

"""
class EntryFrame:
    def __init__(self, master, documentList):
        """

        """
        self._master = master


        self._canvas = Canvas(self._master, borderwidth=0, background="blue")
        self._inFrame = Frame(self._canvas)
        vsb = Scrollbar(self._master, orient="vertical", command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=vsb.set)

        vsb.pack(side="right", fill="y")
        self._canvas.pack(side="left", fill="both", expand=True)
        self._canvasFrame = self._canvas.create_window((4,4), window=self._inFrame, anchor="nw")

        self._inFrame.bind("<Configure>", self.__onFrameConfigure)
        self._canvas.bind("<Configure>", self.__frameWidth)

        self._rows = []
        self._rowObjs = []

        self.addDocumentListRows(documentList)


    def removeRowFromList(self, row):
        """

        """
        self._rows.remove(row)

    def addDocumentListRows(self, documentList):
        """

        """
        for document in documentList.getDocuments():
            self.addDocumentRow(document, documentList)

    def addDocumentRow(self, document, documentList):
        """

        """
        row = Frame(self._inFrame)
        row.grid(row=len(self._rows), column=0, sticky="nesw")
        row.grid_columnconfigure(0, weight=18)
        row.grid_columnconfigure(1, weight=17)
        row.grid_columnconfigure(2, weight=4)
        row.grid_columnconfigure(3, weight=2)
        row.grid_columnconfigure(4, weight=20)
        row.grid_columnconfigure(5, weight=7)
        row.grid_columnconfigure(6, weight=7)
        row.grid_columnconfigure(7, weight=7)
        entryRow = EntryRow(row, self, document, documentList)
        self._rows.append(row)
        self._rowObjs.append(entryRow)

    def assignTestInstances(self, prop):
        """

        """
        total = len(self._rowObjs)
        testNum = int(prop * total)
        trainNum = total - testNum
        ones = [1] * testNum
        zeros = [0] * trainNum
        listOfTests = []
        listOfTests.extend(ones)
        listOfTests.extend(zeros)
        random.shuffle(listOfTests)
        for c, rowObj in enumerate(self._rowObjs):
            rowObj.setTestVar(listOfTests[c])
            rowObj.confirmEntry()

    def __onFrameConfigure(self, event):
        """

        """
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))


    def __frameWidth(self, event):
        """

        """
        canvas_width = event.width
        self._canvas.itemconfig(self._canvasFrame, width = canvas_width)
