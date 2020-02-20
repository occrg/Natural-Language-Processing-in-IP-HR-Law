from tkinter import *


"""

"""
class ButtonsFrame:


    def __init__(self, master, documentList, infoObj):
        """


        Arguments:
        master       ()
            --
        documentList (DocumentList)
            --
        infoObj      ()
            --
        """
        self._master = master

        self._master.grid_rowconfigure(0, weight=1)
        self._master.grid_rowconfigure(1, weight=1)
        self._master.grid_rowconfigure(2, weight=1)
        self._master.grid_columnconfigure(0, weight=1)

        crossValidateButton = Button(self._master, text="Cross-Validate",    \
            command=lambda: self.__crossValidate(documentList, infoObj))

        crossValidateButton.grid(row=1, column=1, padx=15, sticky = "nse")


    def __crossValidate(self, documentList, infoObj):
        """


        Arguments:
        documentList ()
            --
        infoObj      ()
            --
        """
        documentList.getCrossValidation().crossValidateAll(documentList, 4)
        infoObj.update(documentList)
