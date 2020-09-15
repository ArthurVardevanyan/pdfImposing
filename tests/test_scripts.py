__version__ = "v20200915"
import PyPDF2
import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import tests.test_common as c
import scripts
import files


class Testing(unittest.TestCase):
    def bookletTest(self, input, expected, temp, margin=1):
        bookletFile = files.InputFiles(input)
        scripts.booklet([bookletFile], margin)
        with open(expected, 'rb') as file:
            testFile = file.read()
        with open(temp, 'rb') as file:
            expectedFile = file.read()
        if os.path.exists(temp):
            os.remove(temp)
        self.assertEqual(c.cleanup(testFile), c.cleanup(expectedFile))

    def test_halfpage_booklet_1(self):
        self.bookletTest("tests/input/100_halfPage.pdf",
                         "tests/expected/100_halfPage_1_booklet.pdf", "tests/input/100_halfPage_booklet.pdf")

    def test_halfpage_booklet_96(self):
        self.bookletTest("tests/input/100_halfPage.pdf", "tests/expected/100_halfPage_96_booklet.pdf",
                         "tests/input/100_halfPage_booklet.pdf", .96)

    def test_letter_booklet_1(self):
        self.bookletTest("tests/input/8page_letter.pdf",
                         "tests/expected/8page_letter_1_booklet.pdf", "tests/input/8page_letter_booklet.pdf")

    def test_letter_booklet_96(self):
        self.bookletTest("tests/input/8page_letter.pdf", "tests/expected/8page_letter_96_booklet.pdf",
                         "tests/input/8page_letter_booklet.pdf", .96)

    def mergeTest(self, input, expected, temp, DUPLEX="False"):
        mergeFile = []
        for i in input:
            F = files.InputFiles(i)
            mergeFile.append(F)
        scripts.mergeScript(mergeFile, DUPLEX, "test")
        with open(expected, 'rb') as file:
            testFile = file.read()
        with open(temp, 'rb') as file:
            expectedFile = file.read()
        if os.path.exists(temp):
            os.remove(temp)
        # self.assertEqual(c.cleanup(testFile), c.cleanup(expectedFile))
        self.assertEqual(testFile, expectedFile)

    def test_simplex_merge(self):
        self.mergeTest(["tests/input/black.pdf", "tests/input/sample.pdf"], "tests/expected/simplex_merged.pdf",
                       "tests/input/test_merged.pdf")

    def test_duplex_merge(self):
        self.mergeTest(["tests/input/black.pdf", "tests/input/sample.pdf"], "tests/expected/duplex_merged.pdf",
                       "tests/input/test_merged.pdf", "True")

    def blankTest(self, input, expected, temp, CSV, OPERATION):
        scripts.blankScript([files.InputFiles(input)], CSV, OPERATION)
        with open(expected, 'rb') as file:
            testFile = file.read()
        with open(temp, 'rb') as file:
            expectedFile = file.read()
        if os.path.exists(temp):
            os.remove(temp)
        # self.assertEqual(c.cleanup(testFile), c.cleanup(expectedFile))
        self.assertEqual(testFile, expectedFile)

    def test_blank_add(self):
        self.blankTest("tests/input/8page_letter.pdf", "tests/expected/8page_letter_add_modified.pdf",
                       "tests/input/8page_letter_modified.pdf", "1,7,8,9", "add")

    def test_blank_remove(self):
        self.blankTest("tests/input/8page_letter.pdf", "tests/expected/8page_letter_remove_modified.pdf",
                       "tests/input/8page_letter_modified.pdf", "1,7,8", "remove")
