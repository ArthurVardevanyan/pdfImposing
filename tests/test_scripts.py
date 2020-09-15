import PyPDF2
import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import files
import scripts


class Testing(unittest.TestCase):

    def test_booklet(self):
        path = "tests/input/100_halfPage.pdf"
        bookletFile = files.InputFiles(path)
        scripts.booklet([bookletFile], .96)
        path = "tests/expected/100_halfPage_96_booklet.pdf"
        with open(path, 'rb') as file:
            testFile = file.read()
        path = "tests/input/100_halfPage_booklet.pdf"
        with open(path, 'rb') as file:
            expectedFile = file.read()
        if os.path.exists(path):
            os.remove(path)
        self.assertEqual(testFile, expectedFile)
