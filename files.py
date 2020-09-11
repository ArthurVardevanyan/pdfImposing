# files.py
__version__ = "v20200911"

import os
import glob
import PyPDF2


class Files:
    def __init__(self, path=None):
        self.path = path
        self.name = self.__loadName()

    def __loadName(self):
        return (self.path.split("/"))[-1]


class InputFiles(Files):
    def __init__(self, path):
        super().__init__(path)
        self.doc = self.__loadFile()

    def __loadFile(self):
        return PyPDF2.PdfFileReader(open(self.path, "rb"))


class ExportFiles(Files):
    def __init__(self, path, doc=PyPDF2.PdfFileWriter(), extension="modified"):
        super().__init__(path)
        self.doc = doc
        self.extension = extension
        self.__outputStream = None

    def export(self):
        self.__outputStream = self.__exportData()
        self.__exportFile()

    def __exportData(self):
        return open(self.path[:-4] + "_"+self.extension+".pdf", "wb")

    def __exportFile(self):
        self.doc.write(self.__outputStream)
