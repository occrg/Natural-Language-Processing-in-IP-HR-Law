import os

import tkinter as tk
from tkinter import ttk

from lib.filesio import csvFileToDocumentDetails


def openPDF(pdfPath):
    os.system('xdg-open %s' % pdfPath)

def populate(frame, documentDetails):
    journalOptions = { 'International Journal of Heritage Studies',          \
        'International Journal of Cultural Property',                        \
        'Journal of Intellectual Property Law',                              \
        'Journal of World Intellectual Property', '-' }
    for c, d in enumerate(documentDetails[:10]):
        titleEntry = tk.Entry(frame, width=50)
        titleEntry.insert(0, "%s" % d['title'])
        journalsVar = tk.StringVar(frame, '%s' % d['journal'])
        journalEntry = tk.OptionMenu(frame, journalsVar, *journalOptions)
        dateEntry = tk.Entry(frame, width=10)
        dateEntry.insert(0, '%s' % d['date'])
        pathEntry = tk.Label(frame, text="%s" % d['pdfPath'])
        testVar = tk.IntVar(frame, 1)
        testCheck = tk.Checkbutton(frame, var=testVar)
        confirmButton = tk.Button(frame, text="Confirm Changes")
        removeButton = tk.Button(frame, text="Remove")
        openButton = tk.Button(frame, text="Open", command=lambda: openPDF(d['pdfPath']))

        titleEntry.grid(row=c, column=0, padx=15, pady=1)
        journalEntry.grid(row=c, column=1, padx=15, pady=1)
        dateEntry.grid(row=c, column=2, padx=15, pady=1)
        testCheck.grid(row=c, column=3, padx=15, pady=1)
        pathEntry.grid(row=c, column=4, padx=15, pady=1)
        confirmButton.grid(row=c, column=5, padx=15, pady=1)
        removeButton.grid(row=c, column=6, padx=15, pady=1)
        openButton.grid(row=c, column=7, padx=15, pady=1)


def topFrameLayout(frame):
    titleLabel = tk.Label(frame, text="Title")
    journalLabel = tk.Label(frame, text="Journal")
    dateLabel = tk.Label(frame, text="Date")
    testLabel = tk.Label(frame, text="Test")
    pathLabel = tk.Label(frame, text="Path")

    titleLabel.grid(row=0, column=0, padx=15, pady=5)
    journalLabel.grid(row=0, column=1, padx=15, pady=5)
    dateLabel.grid(row=0, column=2, padx=15, pady=5)
    testLabel.grid(row=0, column=3, padx=15, pady=1)
    pathLabel.grid(row=0, column=4, padx=15, pady=1)

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def middleFrameLayout(frame, documentDetails):
    canvas = tk.Canvas(frame, borderwidth=0, background="blue")
    inFrame = tk.Frame(canvas)
    vsb = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=inFrame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    populate(inFrame, documentDetails)

def bottomFrameLayout(frame):
    addButton = tk.Button(frame, text="Add Document")
    testButton = tk.Button(frame, text="Change Test Data")
    trainButton = tk.Button(frame, text="Confirm & Train")

    addButton.grid(row=0, column=0, padx=15, pady=15)
    testButton.grid(row=0, column=1, padx=15, pady=15)
    trainButton.grid(row=0, column=2, padx=15, pady=15)

def formTabLayout(tab, documentDetails):
    tab_width = tab.winfo_screenwidth()
    tab_height = tab.winfo_screenheight()

    topFrameHeight = (int)(0.03*tab_height)
    middleFrameHeight = (int)(0.92*tab_height)
    bottomFrameHeight = (int)(0.05*tab_height)

    topFrame = tk.Frame(tab, width=tab_width, height=topFrameHeight, background="red")
    middleFrame = tk.Frame(tab, width=tab_width, height=middleFrameHeight, background="blue")
    bottomFrame = tk.Frame(tab, width=tab_width, height=bottomFrameHeight, background="green")

    tab.grid_rowconfigure(1, weight=1)
    tab.grid_columnconfigure(0, weight=1)

    topFrame.grid(row=0, sticky="ew")
    middleFrame.grid(row=1, sticky="nsew")
    bottomFrame.grid(row=2, sticky="ew")

    topFrame.grid_propagate(False)
    middleFrame.grid_propagate(False)
    bottomFrame.grid_propagate(False)

    topFrameLayout(topFrame)
    middleFrameLayout(middleFrame, documentDetails)
    bottomFrameLayout(bottomFrame)


def main():
    path = 'data/documentDetails.csv'
    documentDetails = csvFileToDocumentDetails(path)

    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (screen_width, screen_height))

    tab_parent = ttk.Notebook(root)
    tab1 = ttk.Frame(tab_parent)
    tab2 = ttk.Frame(tab_parent)


    formTabLayout(tab1, documentDetails)

    tab_parent.add(tab1, text="Documents")
    tab_parent.add(tab2, text="Results")


    tab_parent.pack(expand=1, fill='both')

    root.mainloop()


if __name__ == '__main__':
    main()
