import random
class BankAccounts:
   customer_name = ''
   balance=0.0
   count=0

   def __init__(self, customer_name):
     self.customer_name=customer_name 
     self.account_num=self.generateAccountNumber()
     self.balance=0 
     self.display()
     self.count+=1
#function generate account number of 8 digits long randomly 
   def generateAccountNumber(self):
     return 1 + random. randint (0, 10000) * 10000 + random. randint (0, 10000)

#function to get bank account from the list
   def getAccountNumber (self):
     return self.account_num
#function to add amount to a bank account balance
   def addAmount (self,amount):
     self.balance+=amount
#function to withdraw an amount from a bank account balance 
   def withdrawAmount (self, amount):
    if (self. balance-amount>=0):
       self. balance-=amount 
    else:
        print("You do not have sufficient funds to make this withdraw!")
#Display function to display a bank account info 
   def display(self):
       print("\nCustomer name: " + self.customer_name + "\nAccount number: " + str(self.account_num) + "\nAccount Balance: $" + str(self.balance) + "\n")