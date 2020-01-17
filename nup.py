# nup.py
__version__ = "v20200117"

import PyPDF2

# Starting Point https://github.com/mstamy2/PyPDF2/blob/master/Scripts/2-up.py

def nup(inFile):
 #Still only does 2up from the adapted script.
    doc = PyPDF2.PdfFileReader(inFile, "rb")
    output = PyPDF2.PdfFileWriter()
    for iter in range(0, doc.getNumPages()-1, 2):
        lhs = doc.getPage(iter)
        rhs = doc.getPage(iter+1)
        lhs.mergeTranslatedPage(rhs, lhs.mediaBox.getUpperRight_x(), 0, True)
        output.addPage(lhs)

    outputStream = open(inFile[:-4] + "_nup.pdf", "wb")
    output.write(outputStream)


def main():

    nup("sample/8page_stackShuffled.pdf")


if __name__ == "__main__":
    main()
