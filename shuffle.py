# shuffle.py
__version__ = "v20200117"

import PyPDF2
import sys


def normalShuffle(inFile, str):

    doc = PyPDF2.PdfFileReader(open(inFile, "rb"))
    output = PyPDF2.PdfFileWriter()
    RULES = [int(s) for s in str.split() if s.isdigit()]
    pages = []
    for iter in range(0, int(doc.getNumPages()), len(RULES)):

        for i in range(0, len(RULES)):
            pages.append(doc.getPage(iter+int(RULES[i])-1))

    for page in pages:
        output.addPage(page)

    outputStream = open(inFile[:-4] + "_normalShuffled.pdf", "wb")
    output.write(outputStream)


def stackShuffle(inFile, str):

    doc = PyPDF2.PdfFileReader(open(inFile, "rb"))
    output = PyPDF2.PdfFileWriter()
    RULES = [int(s) for s in str.split() if s.isdigit()]
    pages = []
    for iter in range(0, int(doc.getNumPages()/len(RULES))):
        for i in range(0, len(RULES)):
            pages.append(doc.getPage(
                iter+(int(RULES[i])-1)*int(doc.getNumPages()/len(RULES))))

    for page in pages:
        output.addPage(page)

    outputStream = open(inFile[:-4] + "_stackShuffled.pdf", "wb")
    output.write(outputStream)


def main():

    stackShuffle("sample/8page.pdf", "1 2")


if __name__ == "__main__":
    main()
