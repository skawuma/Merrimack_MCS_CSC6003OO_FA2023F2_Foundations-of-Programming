from Personnel import Personnel


class Nurse(Personnel):
    """
       Child Class that Inherits from Parent Class (Personnel)

        Attributes:
        - name: String
            The name Associated witth the Nurse.
        - age: int
            The   age associated with the Nurse.
        - hourly_rate,: float
            The hourly_rate, associated with the Nurse
        - rank: String
            The rank, associated with the Nurse    
        Methods:
        SETTER AND GETTER:
        - set_rank() -> String:
         sets the rank of the Nurse
        - get_rank() -> String:
         gets the rank of the Nurse.
        - display() -> String:
         Calls super method Display in the Parent Class Personell. 
         Displays the Rank of the Nurse   
            
    """
    def __init__(self, name, age, hourly_rate,rank):
        super().__init__(name, age, hourly_rate)
        self.rank = rank

    def get_rank(self):
        return self.rank

    def set_rank(self, value):
        self.rank = value
        
    def display(self):
        """
        Calls super method Display in the Parent Class Personnell

        Returns:
        - String:
            The Rank of Nurse.
        """
        super().display()
        print (" And works as a Nurse ranked as", self.get_rank())
        
    def displayNurse(self):
        return self.display()
