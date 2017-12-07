import unittest
from sllist import sllist

class TestSllist(unittest.TestCase):
    
    def test_push(self):
        colors = sllist.SingleLinkedList()
        colors.push("Pthalo Blue")
        #assert colors.count() == 1
        #colors.push("Ultramarine Blue")
        #assert colors.count() == 2
        self.assertEqual(colors.count(),1)
        colors.push("Ultramarine Blue")
        self.assertEqual(colors.count(),2)
        
    def test_pop(self):
        colors = sllist.SingleLinkedList()
        colors.push("Magenta")
        colors.push("Alizarin")
        self.assertEqual(colors.pop(),"Alizarin")
        self.assertEqual(colors.pop(),"Magenta")
        self.assertEqual(colors.pop(),None)
        
        
if __name__ == '__main__':
    unittest.main()
