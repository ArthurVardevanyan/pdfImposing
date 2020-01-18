# shuffle.py
__version__ = "v20200117"

import PyPDF2


def normalShuffle(doc, docR, str):

    output = PyPDF2.PdfFileWriter()
    #RULES = [int(s) for s in str.split() if s.isdigit()]
    RULES = list(str)[::2]
    RULE_MOD = list(str)[1::2]

    pages = []
    for iter in range(0, int(doc.getNumPages()), len(set(RULES))):

        for i in range(0, len(RULES)):
            if (RULE_MOD[i] == "*"):
                pages.append(docR.getPage(
                    iter+int(RULES[i])-1).rotateClockwise(180))
            else:
                pages.append(doc.getPage(iter+int(RULES[i])-1))

    for page in pages:
        output.addPage(page)

    return output


def stackShuffle(doc, str):

    output = PyPDF2.PdfFileWriter()
    RULES = [int(s) for s in str.split() if s.isdigit()]
    pages = []
    temp = PyPDF2.PdfFileWriter()
    for iter in range(0, (doc.getNumPages())):
        # print(iter)
        temp.addPage(doc.getPage(iter))
    doc = temp
    while((doc.getNumPages() % len(RULES))):
        doc.addPage(PyPDF2.pdf.PageObject.createBlankPage(doc.getPage(0), doc.getPage(
            0).mediaBox.getWidth(), doc.getPage(0).mediaBox.getHeight()))
    # print(doc.getNumPages())
    for iter in range(0, int(doc.getNumPages()/len(RULES))):
        # print(iter)
        for i in range(0, len(RULES)):
            pages.append(doc.getPage(
                iter+(int(RULES[i])-1)*int(doc.getNumPages()/len(RULES))))

    for page in pages:
        output.addPage(page)

    return output


def main():

    inFile = "sample/blackPage_scaled.pdf"
    doc = PyPDF2.PdfFileReader(open(inFile, "rb"))
    docR = PyPDF2.PdfFileReader(open(inFile, "rb"))

    # Space For No Modifier, * For 180 Flip
    output = normalShuffle(doc, docR, "1 1*")
    outputStream = open(inFile[:-4] + "_stackShuffled.pdf", "wb")
    output.write(outputStream)


if __name__ == "__main__":
    main()