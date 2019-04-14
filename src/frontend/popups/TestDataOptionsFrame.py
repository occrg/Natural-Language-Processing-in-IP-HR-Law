from tkinter import *
from tkinter import ttk

from backend.FilesIO import FilesIO


"""

"""
class TestDataOptionsFrame:


    def __init__(self, entryObj, documentList):
        """

        """
        popup = Tk()
        popup.wm_title("Test Data Options")

        popup.grid_columnconfigure(0, weight=1)
        popup.grid_rowconfigure(0, weight=1)
        popup.grid_rowconfigure(1, weight=1)
        popup.grid_rowconfigure(2, weight=1)
        popup.grid_rowconfigure(3, weight=1)
        popup.grid_rowconfigure(4, weight=1)



        randomSelectButton = ttk.Button(popup, text="Random Selection", command=lambda: entryObj.assignTestInstances(0.25))
        selectAllButton = ttk.Button(popup, text="Select All", command=lambda: entryObj.assignTestInstances(1))
        deselectAllButton = ttk.Button(popup, text="Deselect All", command=lambda: entryObj.assignTestInstances(0))
        doneButton = ttk.Button(popup, text="Done", command = popup.destroy)

        randomSelectButton.grid(row=0, sticky="n")
        selectAllButton.grid(row=1, sticky="n")
        deselectAllButton.grid(row=2, sticky="n")
        doneButton.grid(row=4, sticky="s")

        popup.mainloop()
