# files.py
__version__ = "v20200911"

import os
import glob
import PyPDF2


class Files:
    def __init__(self, path=None,):
        self.path = self.__loadPath(path)
        self.name = self.__loadName(path)

    def __loadName(self, path):
        return (path.split("/"))[-1].replace(".pdf", "")

    def __loadPath(self, path):
        pos = path.rfind("/")
        path = path[0:pos+1]
        return path

    def filePath(self):
        return self.path + self.name


class InputFiles(Files):
    def __init__(self, path):
        super().__init__(path)
        self.doc = self.__loadFile()

    def __loadFile(self):
        return PyPDF2.PdfFileReader(open(self.filePath() + ".pdf", "rb"))


class ExportFiles(Files):
    def __init__(self, path, doc=PyPDF2.PdfFileWriter(), extension="modified", ):
        super().__init__(path)
        self.doc = doc
        self.extension = extension
        self.__outputStream = None

    def export(self):
        self.__outputStream = self.__exportData()
        self.__exportFile()

    def __exportData(self):
        return open(self.filePath() + "_"+self.extension+".pdf", "wb")

    def __exportFile(self):
        self.doc.write(self.__outputStream)
        self.__outputStream.close()
