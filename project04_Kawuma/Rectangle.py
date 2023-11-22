class Rectangle:
    
    
    """
       Base  Class for  (Rectangle)

        Attributes:
        - length: float
            The length associated with the length of the Rectangle.
        - width: float
            The width associated with the width of the Rectangle.
      
        Methods:
        -area() -> float:
        Calculates area  of the Rectangle.
        -perimeter() -> float:
        Calculates perimeter of the Rectangle.
        - display() -> float: 
         Displays the Area, Perimeter of the Rectangle    
            
    """
    def __init__(self,length,width):
        """
        Constructor to instantiate the Rectangle class.

        Parameters:
        - length: float
            The length associated with the length of the Rectangle.
        - width: float
            The width associated with the width of the Rectangle.
    
        """ 
        self.length=length
        self.width=width
    #
   
    
    def perimeter(self):
        
        """
        Calculates perimeter  of the Rectangle.

        Returns:
        - float:
            The perimter  of the Rectangle.
        """
        return 2 *( self.length + self.width)
    
        
    def area(self):
        """
        Calculates perimeter  of the Rectangle.

        Returns:
        - float:
            The perimter  of the Rectangle.
        """
        
        return self.length*self.width
    
    def display(self):
        
         """
        Displays the Perimter and area of the Rectangle 

        Returns:
        - float:
            The perimter  of the Rectangle.
        """
        
        print("\nA Rectangle of length" ,self.length,"and Width",self.width,"has a", "\nPerimeter of ",self.perimeter(),"and"," \nArea of:" ,self.area(),"\n")
 