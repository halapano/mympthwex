import unittest
from dllist import dllist

class TestDllist(unittest.TestCase):
    
    def test_push(self):
        colors = dllist.DoubleLinkedList()
        colors.push("Pthalo Blue")
        self.assertEqual(colors.count(),1)
        colors.push("Ultramarine Blue")
        self.assertEqual(colors.count(),2)
        
    def test_pop(self):
        colors = dllist.DoubleLinkedList()
        colors.push("Magenta")
        colors.push("Alizarin")
        self.assertEqual(colors.pop(),"Alizarin")
        self.assertEqual(colors.pop(),"Magenta")
        self.assertEqual(colors.pop(),None)



if __name__ == '__main__':
    unittest.main()
