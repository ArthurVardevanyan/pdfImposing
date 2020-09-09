# merge.py
__version__ = "v20200201"

import PyPDF2
import files


def mergeScript(FILES, DUPLEX):

    output = merge(FILES, DUPLEX)
    outputStream = open("merged.pdf", "wb")
    output.write(outputStream)


def merge(FILES, DUPLEX):

    output = PyPDF2.PdfFileWriter()

    #FILES = files.file_list(FOLDER)

    for FILE in FILES:
        pages = []
        test = open(FILE, "rb")  # FOLDER +
        doc = PyPDF2.PdfFileReader(test)
        pageCount = int(doc.getNumPages())
        for iter in range(0, pageCount):
            pages.append(doc.getPage(iter))
        for page in pages:
            output.addPage(page)
        if(DUPLEX and pageCount % 2):
            output.addPage(PyPDF2.pdf.PageObject.createBlankPage(output.getPage(0), output.getPage(
                0).mediaBox.getWidth(), output.getPage(0).mediaBox.getHeight()))

    return output


def main():

    #folder = ""
    folder = ""

    output = merge(folder, True)
    outputStream = open("merged.pdf", "wb")
    output.write(outputStream)


if __name__ == "__main__":
    main()
