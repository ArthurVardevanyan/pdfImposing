# pdfImposer.py
__version__ = "v20200120"

import PyPDF2
import os
import sys
import time
import margin
import shuffle
import nup


def ledgerDuplexTwoUpSpinCut(inFile):

    doc = PyPDF2.PdfFileReader(open(inFile, "rb"))
    print("Margins")
    output = margin.margin(doc)
    temp = "temp.pdf"
    outputStream = open(temp, "wb")
    output.write(outputStream)
    outputStream.close()
    print("Shuffle")
    inFileR = open(temp, "rb")
    docR = PyPDF2.PdfFileReader(inFileR)
    output = shuffle.normalShuffle(output, docR, "1*1 2 2*")
    print("Nup")
    output = nup.nup(output)
    outputStream = open(inFile[:-4] + "_scaled.pdf", "wb")
    output.write(outputStream)

    inFileR.close()
    outputStream.close()

    filePath = "temp.pdf"
    if os.path.exists(filePath):
        os.remove(filePath)


def booklet(inFile):
    doc = PyPDF2.PdfFileReader(open(inFile, "rb"))
    print("Margins")
    output = margin.margin(doc)
    print("Booklet Shuffle 1")
    output = shuffle.bookletShuffle(output)
    print("Booklet Shuffle 2")
    temp = "temp.pdf"
    outputStream = open(temp, "wb")
    output.write(outputStream)
    outputStream.close()
    inFileR = open(temp, "rb")
    docR = PyPDF2.PdfFileReader(inFileR)
    output = shuffle.normalShuffle(output, docR, "1 2 4 3 ")
    print("Nup")
    output = nup.nup(output)
    outputStream = open(inFile[:-4] + "_booklet.pdf", "wb")
    output.write(outputStream)

    inFileR.close()
    outputStream.close()

    filePath = "temp.pdf"
    if os.path.exists(filePath):
        os.remove(filePath)


def SimplexStackCut(inFile):

    print("StackShuffle")
    doc = PyPDF2.PdfFileReader(open(inFile, "rb"))
    output = shuffle.normalShuffle(doc, doc, "1 2 4 3 ")
    output = shuffle.stackShuffle(doc, "1 2")
    print("Nup")
    output = nup.nup(output)
    outputStream = open(inFile[:-4] + "_simplexStackShuffledNup.pdf", "wb")
    output.write(outputStream)



def DuplexStackCut(inFile):

    doc = PyPDF2.PdfFileReader(open(inFile, "rb"))
    docR = PyPDF2.PdfFileReader(open(inFile, "rb"))
    print("Duplex Shuffle")
    output = shuffle.normalShuffle(doc, docR, "1 2 4 3 ")
    print("StackShuffle")
    output = shuffle.stackShuffle(output, "1 2")
    print("Nup")
    output = nup.nup(output)
    outputStream = open(inFile[:-4] + "_DuplexStackShuffledNup.pdf", "wb")
    output.write(outputStream)



def main():
    inFile = sys.argv[1]

    SimplexStackCut(inFile)
    # inFile = "sample/blackPage.pdf"
    # ledgerDuplexTwoUpSpinCut(inFile)
    # booklet(inFile)


if __name__ == "__main__":
    main()
