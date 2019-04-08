from tkinter import *
from tkinter import ttk


"""

"""
class TestDataOptionsFrame:
    def __init__(self):
        """

        """
        popup = Tk()
        popup.wm_title("Test Data Options")

        randomSelectButton = ttk.Button(popup, text="Random Selection")
        selectAllButton = ttk.Button(popup, text="Select All")
        deselectAllButton = ttk.Button(popup, text="Deselect All")
        doneButton = ttk.Button(popup, text="Done", command = popup.destroy)

        randomSelectButton.pack(fill=X)
        selectAllButton.pack(fill=X)
        deselectAllButton.pack(fill=X)
        doneButton.pack(fill=X, pady=10)

        popup.mainloop()
