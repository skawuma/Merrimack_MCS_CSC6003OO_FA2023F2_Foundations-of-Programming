import unittest
from Rectangle import Rectangle
from Parallelepiped import Parallelepiped


class TestParallelepiped(unittest.TestCase):
    
    def test_positiveVolume(self):
    #Test areas with positive atttributes 
     para = Parallelepiped(2,3,4)
     self.assertEqual(para.volume(),24,"incorrect Volume")

     para = Parallelepiped(5,3,4)
     self.assertEqual(para.volume(),60,"correct Volume")
    
    def test_negativeVolume(self):
    #Test areas when values are negative
      para =Parallelepiped(-3,3,1)
      self.assertEqual(para.volume(),-9,"incorrect volume")
      
if __name__ == "__main__":
    unittest.main()