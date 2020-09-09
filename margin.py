# margin.py
__version__ = "v20200909"

import PyPDF2


def scale(doc, width, height, margin=.96):
    output = PyPDF2.PdfFileWriter()
    # TODO Intergrate
    for iter in range(0, doc.getNumPages()):
        width = width * 72
        height = height * 72
        page = doc.getPage(iter)
        pageWidth = page.mediaBox.getWidth()
        pageHeight = page.mediaBox.getHeight()
        short = width/pageWidth
        longer = height/pageHeight

        if short > longer:
            temp = short
            short = longer
            longer = temp
        marginScale = margin*(short)
        docS = PyPDF2.pdf.PageObject.createBlankPage(
            page, pageWidth * width/pageWidth,  pageHeight*height/pageHeight)
        leftmargin = (width - float(pageWidth * marginScale))/2
        bottommargin = (
            (height-float(pageHeight * marginScale))/2)
        docS.mergeScaledTranslatedPage(
            page, marginScale, leftmargin, bottommargin)
        output.addPage(docS)

    return output


def margin(doc):

    output = PyPDF2.PdfFileWriter()

    for iter in range(0, doc.getNumPages()):
        # print(iter)
        page = doc.getPage(iter)
        docS = PyPDF2.pdf.PageObject.createBlankPage(
            page, page.mediaBox.getWidth(),  page.mediaBox.getHeight())
        leftmargin = (float(page.mediaBox.getWidth()) * .04 / 2)
        bottommargin = (float(page.mediaBox.getHeight()) * .04 / 2)
        docS.mergeScaledTranslatedPage(page, .96, leftmargin, bottommargin)
        output.addPage(docS)

    return output


def main():
    inFile = "sample/1.pdf"
    doc = PyPDF2.PdfFileReader(inFile, "rb")
    output = scale(doc, 8, 10)
    outputStream = open(inFile[:-4] + "_imposed.pdf", "wb")
    output.write(outputStream)


if __name__ == "__main__":
    main()
