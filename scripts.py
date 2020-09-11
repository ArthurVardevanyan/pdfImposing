
__version__ = "v20200910"
import os
import sys
import PyPDF2
import time
import margin
import shuffle
import nup


def ledgerDuplexTwoUpSpinCut(inFile, outFile=None):
    if outFile == None:
        outFile = inFile
        append = "_modified.pdf"
    else:
        append = ".pdf"

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
    outputStream = open(outFile[:-4] + append, "wb")
    output.write(outputStream)

    inFileR.close()
    outputStream.close()

    filePath = "temp.pdf"
    if os.path.exists(filePath):
        os.remove(filePath)


def ledgerSimplexTwoUp(inFile, outFile=None):
    if outFile == None:
        outFile = inFile
        append = "_modified.pdf"
    else:
        append = ".pdf"

    doc = PyPDF2.PdfFileReader(open(inFile, "rb"))
    print("Margins")
    output = margin.margin(doc)
    print("Shuffle")
    output = shuffle.normalShuffle(output, output, "1 1 ")
    print("Nup")
    output = nup.nup(output)
    outputStream = open(outFile[:-4] + append, "wb")
    output.write(outputStream)

    outputStream.close()


def ledgerSimplexTwoUpSpinCut(inFile, outFile=None):
    if outFile == None:
        outFile = inFile
        append = "_modified.pdf"
    else:
        append = ".pdf"

    doc = PyPDF2.PdfFileReader(open(inFile, "rb"))
    print("Margins")
    output = margin.margin(doc)
    print("Shuffle")
    output = shuffle.normalShuffle(output, output, "1*1 ")
    print("Nup")
    output = nup.nup(output)
    outputStream = open(outFile[:-4] + append, "wb")
    output.write(outputStream)

    outputStream.close()


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


def addBlankPage(inFile, pages):

    print("addBlankPage")
    doc = PyPDF2.PdfFileReader(open(inFile, "rb"))
    output = shuffle.addBlank(doc, pages)
    outputStream = open(inFile[:-4] + "_modified.pdf", "wb")
    output.write(outputStream)



def removePage(inFile, pages):

    print("addBlankPage")
    doc = PyPDF2.PdfFileReader(open(inFile, "rb"))
    output = shuffle.removePage(doc, pages)
    outputStream = open(inFile[:-4] + "_modified.pdf", "wb")
    output.write(outputStream)

