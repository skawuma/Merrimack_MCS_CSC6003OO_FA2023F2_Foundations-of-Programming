from Personnel import Personnel


class Doctor (Personnel):
    """
       Child Class that Inherits from Parent Class (Personnel)

        Attributes:
        - name: String
            The name Associated witth the Doctor.
        - age: int
            The   age associated with the Doctor.
        - hourly_rate,: float
            The hourly_rate, associated with the Doctor
        - speciality: String
            The Speciality, associated with the Doctor    
        Methods:
        SETTER AND GETTER:
        - set_speciality() -> String:
         sets the speciality of the Doctor
        - get_speciality() -> String:
         gets the  speciality of the Doctor.
        - display() -> String:
         Calls super method Display in the Parent Class Personell. 
         Displays the Speciality of the Doctor   
            
    """
    def __init__(self, name, age, hourly_rate,speciality):
        super().__init__(name, age, hourly_rate)
        self.speciality=speciality

    def get_speciality(self):
        return self.speciality

    def set_speciality(self, value):
        self.speciality = value

    
    def display(self):
        """
        Calls super method Display in the Parent Class Personnell

        Returns:
        - String:
            The Speciality of Doctor.
        """
        super().display()
        print("And is a Doctor who Specializes as a",self.get_speciality())
    
    def displayDoctor(self):
        """
        Calls super method Display  but Specific to Doctor because it comprises their Speciality

        Returns:
        - String:
            The  Doctors Demographics and their Speciality.
        """
        return self.display()
    
        