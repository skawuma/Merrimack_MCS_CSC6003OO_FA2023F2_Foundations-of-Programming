
class Personnel:
    """
       Base  Class for  (Personnel)

        Attributes:
        - name: String
            The name associated with the Personnel.
        - age: int
            The age  associated with the Personnel.
        - hourly_rate: float
            The hourly_rate associated with the Personnel.
        Methods:
        
        SETTER AND GETTER:
        - set_name() -> String:
         sets the name of the Personnel
        - set_age() -> int:
         sets the age of the Personnel
        - set_hourly_rate() -> float:
         sets the hourly_rate of the Personnel
        - get_name() -> String:
         gets the name of the Personnel.
       - get_age() -> int:
         gets the age of the Personnel.
       - get_hourly_rate() -> float:
         gets the hourly_rate of the Personnel.
        - display() -> String:
         Calls super method Display in the Parent Class Personell. 
         Displays the name ,age, and hourly_rata  of the Personnel.  
            
    """

    def __init__(self,name,age,hourly_rate):
      """
        Constructor to instantiate the Personnel class.

        Parameters:
        - name: String
            The name associated with the Personnel.
        - age: int
            The age  associated with the Personnel.
        - hourly_rate: float
            The hourly_rate associated with the Personnel.
    
      """    
      self.name =name
      self.age=age
      self.hourly_rate=hourly_rate

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_age(self):
        return self.age

    def set_age(self, value):
        self.age = value

    def get_hourly_rate(self):
        return self.hourly_rate

    def set_(self, value):
        self.hourly_rate = value

    
    
    
    def display(self):
        
        """
        Displays the name ,age, and hourly_rata of the Personnel 

        Returns:
        - float:
            The  name ,age, and hourly_rata  of the Personnel.
        """
        
        print(self.get_name() ,"is ",self.get_age(),"years Old", "with an hourly rate of ", self.get_hourly_rate())  
    