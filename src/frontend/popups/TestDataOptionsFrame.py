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

        randomSelectButton = ttk.Button(popup, text="Random Selection", command=lambda: entryObj.assignTestInstances(0.25))
        selectAllButton = ttk.Button(popup, text="Select All", command=lambda: entryObj.assignTestInstances(1))
        deselectAllButton = ttk.Button(popup, text="Deselect All", command=lambda: entryObj.assignTestInstances(0))
        doneButton = ttk.Button(popup, text="Done", command = popup.destroy)

        randomSelectButton.pack(fill=X)
        selectAllButton.pack(fill=X)
        deselectAllButton.pack(fill=X)
        doneButton.pack(fill=X, pady=10)

        popup.mainloop()
