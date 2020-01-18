# margin.py
__version__ = "v20200117"

import PyPDF2


def margin(doc):

    output = PyPDF2.PdfFileWriter()

    for iter in range(0, doc.getNumPages()):
        # print(iter)
        page = doc.getPage(iter)
        docS = PyPDF2.pdf.PageObject.createBlankPage(
            page, page.mediaBox.getWidth(),  page.mediaBox.getHeight())
        leftmargin = (float(page.mediaBox.getWidth()) * .03 / 2)
        bottommargin = (float(page.mediaBox.getHeight()) * .03 / 2)
        docS.mergeScaledTranslatedPage(page, .97, leftmargin, bottommargin)
        output.addPage(docS)

    return output


def main():
    inFile = "sample/blackPage.pdf"
    doc = PyPDF2.PdfFileReader(inFile, "rb")
    output = margin(doc)
    outputStream = open(inFile[:-4] + "_imposed.pdf", "wb")
    output.write(outputStream)


if __name__ == "__main__":
    main()
