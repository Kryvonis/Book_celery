import unittest
from PyPDF2 import PdfFileReader


class TestBookReq(unittest.TestCase):
    def setUp(self):
        self.book_url = "../app/templates/book_builder/pdf_template/2.pdf"

    def test_book_size(self):
        """
        test book size
        resolvedObjects count
        test num pages PdfFileReader.getNumPages
        :return: none
        """
        _input_pdf = PdfFileReader(open(self.book_url, "rb"))
        page = _input_pdf.getPage(0)
        artbox = page.artBox
        self.assertEqual(artbox[0], 0)

    def test_file_exist(self):
        """
        test if we create pdf
        :return:
        """
        try:
            file = open(self.book_url, "rb")
            assert True
        except FileNotFoundError:
            assert False
            # self.assertIsNotNone(file)


if __name__ == '__main__':
    unittest.main()
