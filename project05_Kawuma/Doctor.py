from Personnel import Personnel


class Doctor (Personnel):
    def __init__(self, name, age, hourly_rate,speciality):
        super().__init__(name, age, hourly_rate)
        self.speciality=speciality

    def get_speciality(self):
        return self.speciality

    def set_speciality(self, value):
        self.speciality = value

    
    def display(self):
        super().display()
        print(" And  is a Doctor who Specializes as a",self.get_speciality())
    
    def displayDoctor(self):
        return self.display()
    
        