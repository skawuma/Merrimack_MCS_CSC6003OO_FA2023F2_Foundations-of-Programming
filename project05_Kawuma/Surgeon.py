from Personnel import Personnel


class Surgeon(Personnel):
    """
       Child Class that Inherits from Parent Class (Personnel)

        Attributes:
        - name: String
            The name Associated witth the Surgeon.
        - age: int
            The   age associated with the Surgeon.
        - hourly_rate,: float
            The hourly_rate, associated with the Surgeon
        - board_certified: String 
            Either a Suregeon is board_certified.   
        Methods:
        SETTER AND GETTER:
        - set_board_certified() -> String:
         sets board Certificatio of the the Surgeon
        - get_boardCertified() -> String:
         gets board Ceertification of the Surgeon.
        - display() -> String:
         Calls super method Display in the Parent Class Personell. 
         Displays the Board Certification of the Surgeon 
            
    """
    def __init__(self, name, age, hourly_rate,board_certified):
        super().__init__(name, age, hourly_rate)
        self.board_certified =board_certified

    def get_boardCertified(self):
       
        return self.board_certified

    def set_board_certified(self, value):
        self.board_certified = value




    def display(self):
        """
        Calls super method Display in the Parent Class Personnell

        Returns:
        - String:
            Board Certification of the Surgeon.
        """
        super().display()
    
    def displaySurgeon(self):
        return self.display()