import unittest
from stack import stack

class TestStack(unittest.TestCase):

    def test_push(self):
        """test push"""
        books = stack.Stack()
        books.push('python the hard way')
        self.assertEqual(books.count(),1)
        books.push('Python CookBook')
        self.assertEqual(books.count(),2)

    def test_pop(self):
        books = stack.Stack()
        books.push('python the hard way')
        books.push('Python CookBook')
        self.assertEqual(books.count(),2)
        self.assertEqual(books.pop(),'Python CookBook')
        self.assertEqual(books.count(),1)
        self.assertEqual(books.pop(),'python the hard way')
        self.assertEqual(books.count(),0)
        self.assertEqual(books.pop(),None)


if __name__ == '__main__':
    unittest.main()



