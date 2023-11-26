from Personnel import Personnel


class Nurse(Personnel):
    def __init__(self, name, age, hourly_rate,rank):
        super().__init__(name, age, hourly_rate)
        self.rank = rank

    def get_rank(self):
        return self.rank

    def set_rank(self, value):
        self.rank = value
        
    def display(self):
        super().display()
        print (" And is A Nurse ranked as", self.get_rank())
        
    def displayNurse(self):
        return self.display()
