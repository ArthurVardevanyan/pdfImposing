# pdfImposer.py
__version__ = "v20200206"


import tkinter as tk
from tkinter import filedialog
import scripts

class pdfImposing:
    def __init__(self, master):
        self.master = master
        master.title("pdfImposing")

        self.label = tk.Label(master, text="PDF Imposing")
        self.label.pack()

        self.upload = tk.Button(root, text='Open', command=self.UploadAction)
        self.upload.pack()
        self.files = None

        self.bookletLabel = tk.Button(root, text='Create Booklet', command=self.booklet)
        self.bookletLabel.pack()


    def UploadAction(self):
        # https://stackoverflow.com/a/50135930
        filenames = filedialog.askopenfilenames()
        print('Selected:', filenames)
        self.files = filenames
        self.label = tk.Label(text=filenames)
        self.label.pack()

    def booklet(self):
        scripts.booklet(self.files[0])
        


root = tk.Tk()
my_gui = pdfImposing(root)
root.mainloop()
