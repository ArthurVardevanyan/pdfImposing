# pdfImposer.py
__version__ = "v20200911"


import tkinter as tk
from tkinter import filedialog
import scripts
import merge
import files


class pdfImposing:
    def __init__(self, master):
        self.master = master
        master.title("pdfImposing: " + __version__)

        self.label = tk.Label(master, text="PDF Imposing: " + __version__)
        self.label.pack()

        self.upload = tk.Button(root, text='Open', command=self.UploadAction)
        self.upload.pack()
        self.FILES = []
        self.files = None

        self.label = tk.Label(master, text=" ")  # TODO TEMP SPACE
        self.label.pack()

        self.label = tk.Label(text="Preset Templates")
        self.label.pack()

        self.SimplexMergeLabel = tk.Button(
            root, text='SimplexMerge', command=self.SimplexMerge)
        self.SimplexMergeLabel.pack()

        self.text = tk.Button(
            root, text='DuplexMerge', command=self.DuplexMerge)
        self.text.pack()

        self.label = tk.Label(master, text=" ")  # TODO TEMP SPACE
        self.label.pack()

        self.AddBlankPageLabel = tk.Button(
            root, text='AddBlankPage(s)', command=self.AddBlankPage)
        self.AddBlankPageLabel.pack()

        self.removePageLabel = tk.Button(
            root, text='removePage(s)', command=self.removePage)
        self.removePageLabel.pack()

        self.label = tk.Label(master, text=" ")  # TODO TEMP SPACE
        self.label.pack()

        self.bookletLabel = tk.Button(
            root, text='Create Booklet', command=self.booklet)
        self.bookletLabel.pack()

        self.label = tk.Label(master, text=" ")  # TODO TEMP SPACE
        self.label.pack()

        self.SimplexStackCutLabel = tk.Button(
            root, text='SimplexStackCut', command=self.SimplexStackCut)
        self.SimplexStackCutLabel.pack()

        self.DuplexStackCutLabel = tk.Button(
            root, text='DuplexStackCut', command=self.DuplexStackCut)
        self.DuplexStackCutLabel.pack()

        self.label = tk.Label(master, text=" ")  # TODO TEMP SPACE
        self.label.pack()

        self.ledgerSimplexTwoUpLabel = tk.Button(
            root, text='ledgerSimplexTwoUp', command=self.ledgerSimplexTwoUp)
        self.ledgerSimplexTwoUpLabel.pack()

        self.ledgerDuplexTwoUpSpinCutLabel = tk.Button(
            root, text='ledgerDuplexTwoUpSpinCut', command=self.ledgerDuplexTwoUpSpinCut)
        self.ledgerDuplexTwoUpSpinCutLabel.pack()

        self.ledgerSimplexTwoUpSpinCutLabel = tk.Button(
            root, text='ledgerSimplexTwoUpSpinCut', command=self.ledgerSimplexTwoUpSpinCut)
        self.ledgerSimplexTwoUpSpinCutLabel.pack()

    def UploadAction(self):
        # https://stackoverflow.com/a/50135930
        filenames = filedialog.askopenfilenames()
        print('Selected:', filenames)
        for path in filenames:
            F = files.InputFiles(path)
            self.FILES.append(F)
        self.files = filenames
        self.label = tk.Label(text=filenames)
        self.label.pack()

    def SimplexMerge(self):
        merge.mergeScript(self.files, False)

    def DuplexMerge(self):
        merge.mergeScript(self.files, True)

    def AddBlankPage(self):
        self.SaveLabel = tk.Button(
            root, text='Save', command=self.addSave)
        self.SaveLabel.pack()
        self.pageNumbers = tk.Entry()
        self.pageNumbers.pack()

    def removePage(self):
        self.SaveLabel = tk.Button(
            root, text='Save', command=self.removeSave)
        self.SaveLabel.pack()
        self.pageNumbers = tk.Entry()
        self.pageNumbers.pack()

    def addSave(self):
        scripts.addBlankPage(self.FILES, self.pageNumbers.get())
        print("done")

    def removeSave(self):
        scripts.removePage(self.FILES, self.pageNumbers.get())
        print("done")

    def booklet(self):
        scripts.booklet(self.FILES)
        print("done")

    def SimplexStackCut(self):
        scripts.SimplexStackCut(self.files[0])

    def DuplexStackCut(self):
        scripts.DuplexStackCut(self.files[0])

    def ledgerSimplexTwoUp(self):
        scripts.ledgerSimplexTwoUp(self.files[0])

    def ledgerSimplexTwoUpSpinCut(self):
        scripts.ledgerSimplexTwoUpSpinCut(self.files[0])

    def ledgerDuplexTwoUpSpinCut(self):
        scripts.ledgerDuplexTwoUpSpinCut(self.files[0])


root = tk.Tk()
my_gui = pdfImposing(root)
root.mainloop()
