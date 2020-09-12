# pdfImposer.py
__version__ = "v20200912"


import tkinter as tk
from tkinter import filedialog
import scripts
import files


class pdfImposing:
    def __init__(self, root):
        self.root = root
        root.title("pdfImposing: " + __version__)

        tk.Label(root, text="PDF Imposing: " +
                 __version__).grid(row=0, column=1, padx=5, pady=2)

        tk.Button(root, text='Open Files(s)',
                  command=self.UploadAction).grid(row=1, column=1, padx=5, pady=2)

        self.FILES = []
        self.files = None
        self.fileLabel = tk.Label()

        self.duplex = tk.StringVar(value="False")
        tk.Label(root, text="File Name:").grid(row=3, column=0, padx=5, pady=2)
        self.newName = tk.Entry(root)
        self.newName.grid(row=4, column=0, padx=5, pady=0)
        tk.Radiobutton(root, text='Simplex',
                       variable=self.duplex, value="False").grid(row=5, column=0, padx=5, pady=0)

        tk.Radiobutton(root, text='Duplex',
                       variable=self.duplex, value="True").grid(row=6, column=0, padx=5, pady=0)

        tk.Button(root, text='FileMerge',
                  command=self.fileMerge).grid(row=7, column=0, padx=5, pady=1)

        tk.Label(root, text="CSV:").grid(row=3, column=2, padx=5, pady=0)
        self.pageNumbers = tk.Entry()
        self.pageNumbers.grid(row=4, column=2, padx=5, pady=1)

        tk.Button(root, text='AddBlankPage(s)', command=self.addSave).grid(
            row=5, column=2, padx=5, pady=0)
        tk.Button(root, text='removePage(s)', command=self.removeSave).grid(
            row=6, column=2, padx=5, pady=0)
        tk.Label(root, text="Margin Decimal Percent:").grid(
            row=3, column=1, padx=5, pady=0)
        self.margin = tk.Entry()
        self.margin.insert(0, ".96")
        self.margin.grid(row=4, column=1, padx=5, pady=0)
        tk.Button(root, text='Create Booklet', command=self.booklet).grid(
            row=5, column=1, padx=5, pady=3)
        
        
        tk.Button(
            root, text='SimplexStackCut', command=self.SimplexStackCut).grid(row=7, column=1, padx=5, pady=0)

        tk.Button(
            root, text='DuplexStackCut', command=self.DuplexStackCut).grid(row=8, column=1, padx=5, pady=(0, 15))
        tk.Button(root, text='ledgerSimplexTwoUp',
                  command=self.ledgerSimplexTwoUp).grid(row=9, column=1, padx=5, pady=0)
        tk.Button(root, text='ledgerDuplexTwoUpSpinCut',
                  command=self.ledgerDuplexTwoUpSpinCut).grid(row=10, column=1, padx=5, pady=0)
        tk.Button(root, text='ledgerSimplexTwoUpSpinCut',
                  command=self.ledgerSimplexTwoUpSpinCut).grid(row=11, column=1, padx=5, pady=0)

    def UploadAction(self):
        # https://stackoverflow.com/a/50135930
        filenames = filedialog.askopenfilenames()
        print('Selected:', filenames)
        self.files = filenames
        fileNames = ""
        for path in filenames:
            F = files.InputFiles(path)
            self.FILES.append(F)
            fileNames += F.name + ".pdf" + "\n"
        self.fileLabel['text'] = fileNames
        self.fileLabel.grid(row=2, column=1)

    def fileMerge(self):
        scripts.mergeScript(self.FILES, self.duplex.get(), self.newName.get())
        print("done")

    def addSave(self):
        scripts.addBlankPage(self.FILES, self.pageNumbers.get())
        print("done")

    def removeSave(self):
        scripts.removePage(self.FILES, self.pageNumbers.get())
        print("done")

    def booklet(self):
        scripts.booklet(self.FILES, float(self.margin.get()))
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
