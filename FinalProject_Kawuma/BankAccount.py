import random


class BankAccount:
    account_name = ''
    balance=0.0
    count=0



    
    def __init__(self,account_name) :
          self.account_name=account_name
          self.account_num=self.generate_account_number()
          self.balance=0 
          self.display()
          self.count+=1
    
    #function generate account number of 8 digits long randomly 
          
    def generate_account_number(self):
     return 1 + random. randint (0, 10000) * 10000 + random. randint (0, 10000)      
 
 #function to get bank account from the list
    def get_account_number(self):
     return self.account_num
 #function to retrieve Account Balance
    def get_balance(self):
     return self.balance
 #function to retrieve Account Name
    def get_acc_name(self):
     return self.account_name
 
 #function to add amount to a bank account balance
    def add_amount (self,amount):
     self.balance+=amount

#function to withdraw an amount from a bank account balance 
    def withdraw_amount (self, amount):
     if (self. balance-amount>=0):
        self. balance-=amount 
     else:
        print("You do not have sufficient funds to make this withdraw!")
        
   #Display function to display a bank account info 
    def display(self):
       print("\nAccount_name: " + self.account_name +"\nAccount number: " + str(self.account_num) + "\nAccount Balance: $" + str(self.balance) + "\n")