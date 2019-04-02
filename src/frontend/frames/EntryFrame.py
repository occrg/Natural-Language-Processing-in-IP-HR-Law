from tkinter import *
from tkinter import ttk

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
        self._canvas.bind("<Configure>", self.__FrameWidth)

        self._inFrame.grid_columnconfigure(0, weight=1)
        self._inFrame.grid_columnconfigure(1, weight=1)
        self._inFrame.grid_columnconfigure(2, weight=1)
        self._inFrame.grid_columnconfigure(3, weight=1)
        self._inFrame.grid_columnconfigure(4, weight=1)
        self._inFrame.grid_columnconfigure(5, weight=1)
        self._inFrame.grid_columnconfigure(6, weight=1)
        self._inFrame.grid_columnconfigure(7, weight=1)




        for (r, document) in enumerate(documentList.getDocuments()):
            entryRow = EntryRow(self._inFrame, r, document)



    def __onFrameConfigure(self, event):
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))


    def __FrameWidth(self, event):
        canvas_width = event.width
        self._canvas.itemconfig(self._canvasFrame, width = canvas_width)
