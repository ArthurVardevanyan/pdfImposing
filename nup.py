# nup.py
__version__ = "v20200121"

import PyPDF2

# Starting Point https://github.com/mstamy2/PyPDF2/blob/master/Scripts/2-up.py


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
