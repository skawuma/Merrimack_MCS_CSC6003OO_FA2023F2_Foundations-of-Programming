from Rectangle import Rectangle

class Parallelepiped (Rectangle):
  
    """
       Child Class that Inherits from Parent Class (Rectangle)

        Attributes:
        - length: float
            The length associated with the length of the Parallelepiped.
        - width: float
            The width associated with the width of the Parallelepiped.
        - height: float
            The height associated with the height of the Parallelepiped.
        Methods:
        - volume() -> float:
        Calculates volume  of the Parallelepiped.
        - display() -> float:
         Calls super method Display in the Parent Class Rectangle. 
         Displays the Area, Perimeter and volume of the Parallelepiped    
            
    """
  
    def  __init__(self,length,width,height):
        """
        Constructor to instantiate the Parallelepiped class.

        Parameters:
        - length: float
            The length associated with the length of the Parallelepiped.
        - width: float
            The width associated with the width of the Parallelepiped.
        - height: float
            The height associated with the height of the Parallelepiped.
        """
    
        super().__init__(length,width)
        self.height = height
    
    def volume(self):
      
        """
        Calculates volume  of the Parallelepiped.

        Returns:
        - float:
            The volume  of the Parallelepiped.
        """
      
        return self.length*self.width*self.height
     
    def display(self):
      
        """
       Calls super method Display in the Parent Class Rectangle

        Returns:
        - float:
            The volume  of the Parallelepiped.
        """
      
        super().display
        print("\nThe Parallelepiped has a Volume of:",self.volume(),"\n")
     
