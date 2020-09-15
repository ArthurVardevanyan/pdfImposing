
__version__ = "v20200915"
import os
import sys
import PyPDF2
import time
import shuffle
import nup
import files


def mergeScript(FILES, DUPLEX, newName):

    output = files.ExportFiles(FILES[0].path+newName, shuffle.merge(
        FILES, DUPLEX), extension="merged")
    output.export()


def blankScript(FILES, pages, operation):
    for f in FILES:
        output = files.ExportFiles(
            f.filePath(), shuffle.blank(f.doc, pages, operation))
        output.export()


def booklet(FILES, margin=1):
    for f in FILES:
        output = files.ExportFiles(f.filePath(), extension="booklet")
        print("Margins")
        output.doc = nup.resize(f.doc, margin=margin)
        output.doc = shuffle.bookletShuffle(output.doc)
        print("Booklet Shuffle 2")
        temp = "temp.pdf"
        outputStream = open(temp, "wb")
        output.doc.write(outputStream)
        outputStream.close()
        inFileR = open(temp, "rb")
        docR = PyPDF2.PdfFileReader(inFileR)
        output.doc = shuffle.normalShuffle(output.doc, docR, "1 2 4 3 ")
        print("Nup")

        output.doc = nup.nup(output.doc)
        output.export()

        inFileR.close()
        outputStream.close()

        filePath = "temp.pdf"
        if os.path.exists(filePath):
            os.remove(filePath)


def ledgerDuplexTwoUpSpinCut(inFile, outFile=None):
    if outFile == None:
        outFile = inFile
        append = "_modified.pdf"
    else:
        append = ".pdf"

    doc = PyPDF2.PdfFileReader(open(inFile, "rb"))
    print("Margins")
    output = nup.resize(doc)
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
    output = nup.resize(doc)
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
    output = nup.resize(doc)
    print("Shuffle")
    output = shuffle.normalShuffle(output, output, "1*1 ")
    print("Nup")
    output = nup.nup(output)
    outputStream = open(outFile[:-4] + append, "wb")
    output.write(outputStream)

    outputStream.close()


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
