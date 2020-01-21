# merge.py
__version__ = "v20200120"

import PyPDF2
import files


def merge(FOLDER, DUPLEX):

    output = PyPDF2.PdfFileWriter()
    pages = []

    FILES = files.file_list(FOLDER)

    for FILE in FILES:
        doc = PyPDF2.PdfFileReader(open(FOLDER + FILE, "rb"))
        for iter in range(0, int(doc.getNumPages())):
            pages.append(doc.getPage(iter))
    for page in pages:
        output.addPage(page)

    return output


def main():

    folder = ""

    output = merge(folder, False)
    outputStream = open("merged.pdf", "wb")
    output.write(outputStream)


if __name__ == "__main__":
    main()
