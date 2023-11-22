import unittest


from Rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    
    def test_positiveArea(self):
    #Test areas with positive atttributes 
     rectangle = Rectangle(2,3)
     self.assertEqual(rectangle.area(),6,"incorrect area")
    
    def test_negativeArea(self):
    #Test areas when values are negative
      rectangle = Rectangle(-1,3)
      self.assertEqual(rectangle.area(),-3,"incorrect area")
    def test_positivePerimeter(self):
    #Test areas with positive atttributes 
     rectangle = Rectangle(2,3)
     self.assertEqual(rectangle.perimeter(),10,"incorrect area")
if __name__ == "__main__":
    unittest.main()


