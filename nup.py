# nup.py
__version__ = "v20200912"

import PyPDF2

# Starting Point https://github.com/mstamy2/PyPDF2/blob/master/Scripts/2-up.py


def resize(doc, w=None, h=None, margin=1):
    output = PyPDF2.PdfFileWriter()
    # TODO Intergrate

    for iter in range(0, doc.getNumPages()):
        page = doc.getPage(iter)
        pageWidth = float(page.mediaBox.getWidth())
        pageHeight = float(page.mediaBox.getHeight())

        if (w and h):
            width = w * 72
            height = h * 72
        else:
            width = pageWidth
            height = pageHeight

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


def nup(doc):
 # Still only does 2up from the adapted script.
    output = PyPDF2.PdfFileWriter()
    for iter in range(0, doc.getNumPages()-1, 2):
        # print(iter)
        lhs = doc.getPage(iter)
        rhs = doc.getPage(iter+1)
        rotationL = lhs.get('/Rotate')
        rotationR = rhs.get('/Rotate')

        if(rotationL == 180):
            lhs.mergeRotatedTranslatedPage(
                rhs, 180, 0,  int(lhs.mediaBox.getUpperRight_y()/2), True)

        elif(rotationR == 180):
            lhs.mergeRotatedTranslatedPage(
                rhs, 180, lhs.mediaBox.getUpperRight_x(),  int(lhs.mediaBox.getUpperRight_y()/2), True)

        if(rotationL == 90 and rotationR == 90):
            lhs.mergeTranslatedPage(
                rhs, 0, lhs.mediaBox.getUpperRight_y(), True)

        else:
            lhs.mergeTranslatedPage(
                rhs, lhs.mediaBox.getUpperRight_x(), 0, True)
        output.addPage(lhs)

    return output


def main():
    inFile = "sample/blackPage_scaled_normalShuffled.pdf"
    doc = PyPDF2.PdfFileReader(inFile, "rb")
    output = nup(doc)
    outputStream = open(inFile[:-4] + "_nup.pdf", "wb")
    output.write(outputStream)


if __name__ == "__main__":
    main()
