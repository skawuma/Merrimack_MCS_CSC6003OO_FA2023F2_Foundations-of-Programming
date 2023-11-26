class Personnel:
    
    
    def __init__(self,name,age,hourly_rate):
        
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
        
       print(self.get_name()   ,"is ",self.get_age(),"years Old")  
    