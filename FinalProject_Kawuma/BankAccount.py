import random


class BankAccount:
    
    """
       Base  Class for  (BankAccount)

        Attributes:
        - account_name: String
            The name associated with the Bank.
        -count int
            Keeps count of how many Bank Account being created.
        - balance: float
            The balance associated with the Bank Account.
        Methods:
        
        Methods:
       
       - generate_account_number() -> int:
         generate a random account_number for a specified Accountt created.
       - get_account_number() -> int:
         gets an account_number associated with an Account.
       - get_balance() -> float:
         Retrieve  the Account Balance.
       - add_amount (amount)-> float:
         Adds amount to a bank account balance     
       - get_withdraw_amount(amount) -> float:
         Withdraw an amount from a bank account balance.
       - display() -> String:
         Displays the account_name ,Account_number, and Account Balance  of the Account.  
            
    """
    
    account_name = ''
    balance=0.0
    count=0



    
    def __init__(self,account_name) :
          """
           Constructor to instantiate the BankAccount class.

           Parameters:
             - account_name: String
            The name associated with the Bank.
            -count int
            Keeps count of how many Bank Account being created.
            - balance: float
            The balance associated with the Bank Account.
            - display() -> String:
              Displays the account_name ,Account_number, and Account Balance  of the Account.  
            
          """    
          self.account_name=account_name
          self.account_num=self.generate_account_number()
          self.balance=0.0 
          self.display()
          self.count+=1
    
    
          
    def generate_account_number(self):
     """
        function generate account number of 8 digits long randomly 

        Returns:
        - int:
            The Account Number of a specified Account created.
    """
     return 1 + random. randint (0, 10000) * 10000 + random. randint (0, 10000)      
 
 
    def get_account_number(self):
     """
        function to get bank account from the list 

        Returns:
        - int:
            The Account Number of a specified Account.
     """
     return self.account_num
 
    def get_balance(self):

     """
       function to retrieve Account Balance

        Returns:
        - float:
            The Balance of an Account.
     """
     return self.balance
 
    def get_acc_name(self):
     """
       function to retrieve Account Name

        Returns:
        - string:
            The Account_Name of Account.
     """
     return self.account_name
  
    def add_amount (self,amount):
     """
        
      function to add amount to a bank account balance

        Returns:
        - int:
            The Account_Name of Account.
     """
     self.balance+=amount

 
    def withdraw_amount (self, amount):
     """
        
      function to withdraw an amount from a bank account balance

        Returns:
        - float:
            The Balance of Account after withdraw amount is taken out.
        -String:
           When Balance is less than withdraw amount, then print statement of you dont have sufficient Amount 
     """
     if (self. balance-amount>=0):
        self. balance-=amount 
     else:
        print("\033[1;31;40mYou do not have sufficient funds to make this withdraw!\033[0m")
        
    
    def display(self):
       """
        Displays the bank account information of the Account 

        Returns:
        - String:
            The Account_name,ccount_number and Account_Balance of the Account.
      """
       print("\nAccount_name: " + self.account_name +"\nAccount number: " + str(self.account_num) + "\nAccount Balance: $" + str(self.balance) + "\n")