from Personnel import Personnel


class Surgeon(Personnel):
    def __init__(self, name, age, hourly_rate,board_certified):
        super().__init__(name, age, hourly_rate)
        self.board_certified =board_certified

    def get_boardCertified(self):
       
        return self.board_certified

    def set_board_certified(self, value):
        self.board_certified = value




    def display(self):
        super().display()
        # print("and is, ", self.get_boardCertified())
    
    def displaySurgeon(self):
        return self.display()