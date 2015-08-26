# python -m unittest <testFile>
# -s Directory to start discovery (. default)
# -p Pattern to match test files  (test*.py default)


import unittest
from book import Book

class BookTest(unittest.TestCase):

	def test_create_book(self):
		book = Book()
	
	def test_lookup_book(self):
		book = Book()
		book.add("0xgi","09633")
		self.assertEqual("09633", book.lookup("0xgi"))
		
if __name__ == '__main__':
	unittest.main()