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

        selectAllButton = ttk.Button(popup, text="Select All")
        deselectAllButton = ttk.Button(popup, text="Deselect All")
        doneButton = ttk.Button(popup, text="Done", command = popup.destroy)

        doneButton.pack()

        popup.mainloop()
