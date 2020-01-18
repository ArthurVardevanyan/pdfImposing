# pdfImposer.py
__version__ = "v20200117"

import PyPDF2
import os
import sys
import margin
import shuffle
import nup


def ledgerDuplexTwoUpSpinCut(inFile):

    doc = PyPDF2.PdfFileReader(open(inFile, "rb"))
    print("Margins")
    output = margin.margin(doc)
    temp = "sample/temp.pdf"
    outputStream = open(temp, "wb")
    output.write(outputStream)
    outputStream.close()
    print("Shuffle")
    docR = PyPDF2.PdfFileReader(open(temp, "rb"))
    output = shuffle.normalShuffle(output, docR, "1 1*")
    print("Nup")
    output = nup.nup(output)
    outputStream = open(inFile[:-4] + "_scaled.pdf", "wb")
    output.write(outputStream)

    filePath = "sample/temp.pdf"
    if os.path.exists(filePath):
        os.remove(filePath)


def main():
    inFile = sys.argv[1]
    #inFile = "sample/blackPage.pdf"
    ledgerDuplexTwoUpSpinCut(inFile)
    
    

if __name__ == "__main__":
    main()
