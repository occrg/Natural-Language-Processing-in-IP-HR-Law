import tkinter as tk
from tkinter import ttk

def populate(frame):
    for c in range(100):
        firstEntry = tk.Entry(frame)
        familyEntry = tk.Entry(frame)
        jobEntry = tk.Entry(frame)
        pathEntry = tk.Entry(frame)
        testCheck = tk.Checkbutton(frame)
        editButton = tk.Button(frame, text="Confirm Edit")
        removeButton = tk.Button(frame, text="Remove")
        openButton = tk.Button(frame, text="Open")

        firstEntry.grid(row=c, column=0, padx=15, pady=1)
        familyEntry.grid(row=c, column=1, padx=15, pady=1)
        jobEntry.grid(row=c, column=2, padx=15, pady=1)
        pathEntry.grid(row=c, column=3, padx=15, pady=1)
        testCheck.grid(row=c, column=4, padx=15, pady=1)
        editButton.grid(row=c, column=5, padx=15, pady=1)
        removeButton.grid(row=c, column=6, padx=15, pady=1)
        openButton.grid(row=c, column=7, padx=15, pady=1)


def topFrameLayout(frame):
    titleLabel = tk.Label(frame, text="Title")
    journalLabel = tk.Label(frame, text="Journal")
    dateLabel = tk.Label(frame, text="Date")
    pathLabel = tk.Label(frame, text="Path")

    titleLabel.grid(row=0, column=0, padx=15, pady=5)
    journalLabel.grid(row=0, column=1, padx=15, pady=5)
    dateLabel.grid(row=0, column=2, padx=15, pady=5)
    pathLabel.grid(row=0, column=3, padx=15, pady=1)

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def middleFrameLayout(frame):
    canvas = tk.Canvas(frame, borderwidth=0, background="blue")
    inFrame = tk.Frame(canvas, background="brown")
    vsb = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=inFrame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    populate(inFrame)

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
    middleFrameLayout(middleFrame)
    bottomFrameLayout(bottomFrame)


def main():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (screen_width, screen_height))

    tab_parent = ttk.Notebook(root)
    tab1 = ttk.Frame(tab_parent)
    tab2 = ttk.Frame(tab_parent)

    documentDetails = []

    formTabLayout(tab1, documentDetails)

    tab_parent.add(tab1, text="Documents")
    tab_parent.add(tab2, text="Results")


    tab_parent.pack(expand=1, fill='both')

    root.mainloop()


if __name__ == '__main__':
    main()
