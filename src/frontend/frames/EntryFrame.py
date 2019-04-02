from tkinter import *
from tkinter import ttk


"""

"""
class EntryFrame:
    def __init__(self, master, documentList):
        """

        """
        self._master = master



        canvas = Canvas(self._master, borderwidth=0, background="blue")
        inFrame = Frame(canvas)
        vsb = Scrollbar(self._master, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)

        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((4,4), window=inFrame, anchor="nw")

        self._master.bind("<Configure>", lambda event, canvas=canvas: self.__onFrameConfigure(canvas))



    def __onFrameConfigure(self, canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))
