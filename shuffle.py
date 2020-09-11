# shuffle.py
__version__ = "v20200910"

import PyPDF2


def shuffleEvenOdd(doc, docR):
    # TODO
    return False


def reverseShuffleEvenOdd(doc, docR):
    # TODO
    return False


def addBlank(doc, pages):
    output = PyPDF2.PdfFileWriter()
    pages = pages.replace(" ", "")
    pages = [int(n) for n in list(pages.split(","))]
    pages.sort()
    additional = 0
    for iter in range(0, doc.getNumPages()):
        output.addPage(doc.getPage(iter))
    for page in pages:
        if page >= doc.getNumPages():
            blank = PyPDF2.pdf.PageObject.createBlankPage(doc)
            output.addPage(blank)
        else:
            output.insertBlankPage(index=page+additional)
            additional += 1
    return output


def removePage(doc, pages):
    output = PyPDF2.PdfFileWriter()
    pages = pages.replace(" ", "")
    pages = [int(n) for n in list(pages.split(","))]
    pages.sort()
    additional = 0
    for iter in range(0, doc.getNumPages()):
        if(len(pages)):
            if pages[0] == iter + 1:
                pages.pop(0)
            else:
                output.addPage(doc.getPage(iter))
        else:
            output.addPage(doc.getPage(iter))
    for page in pages:
        if page >= doc.getNumPages():
            blank = PyPDF2.pdf.PageObject.createBlankPage(doc)
            output.addPage(blank)
        else:
            output.insertBlankPage(index=page+additional)
            additional += 1
    return output


def normalShuffle(doc, docR, str):

    output = PyPDF2.PdfFileWriter()
    # RULES = [int(s) for s in str.split() if s.isdigit()]
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


def bookletShuffle(doc):

    output = PyPDF2.PdfFileWriter()
    pages = []

    # print(doc.getNumPages())
    for iter in range(0, int(doc.getNumPages()/2)):
        pages.append(doc.getPage(int(doc.getNumPages()-1 - iter)))
        pages.append(doc.getPage(iter))

    for page in pages:
        output.addPage(page)

    return output


def main():

    inFile = "sample/100.pdf"
    doc = PyPDF2.PdfFileReader(open(inFile, "rb"))
    # docR = PyPDF2.PdfFileReader(open(inFile, "rb"))

    # Space For No Modifier, * For 180 Flip
    output = stackShuffle(doc, "1 2")
    outputStream = open(inFile[:-4] + "_stackShuffled.pdf", "wb")
    output.write(outputStream)


if __name__ == "__main__":
    main()
