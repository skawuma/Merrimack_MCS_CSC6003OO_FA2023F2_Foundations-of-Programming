
##List of bank accounts
import sys
from BankAccount import BankAccount

class Bank:
 bank_accounts_collections=[]
 
#variable to store count of entered accounts

 def __init__(self) :
     
     self.bank_accounts_collections=[]

#function to open a new account 
 def open_new_account(self):
  while True:
    name=str(input ("Please enter the name on the account: "))
    obj=BankAccount (name)
    self.bank_accounts_collections.append (obj)
    global count
    self.count +=1
    print("\033[32m\nYour Account Has Successfully Been Created  \033[0m")
    another_acc = input("Create another Account ? (y/n): ").strip().lower()
    if  another_acc != 'y':
      break


#function to display an account details 
 def display_account_details(self):
  while True:
   try:
    
       account_number = int(input("Please enter the account number for which you'd like to display its details: "))
       if len(self.bank_accounts_collections)==0:
           print("\033[1;31;40mThe list is empty, You need to add a Bank Account first!!\033[0m")
           print ("\n")
           return
       for i in range(len(self.bank_accounts_collections)):
           
           if self.bank_accounts_collections [i].get_account_number() == account_number:
              print("\nThe Account Details for the selected bank account are: ")
              self.bank_accounts_collections[i].display()
              return
      
   except ValueError:
      print("\033[1;31;40mPlease enter a valid account number containing only numbers.\033[0m")
   except IndexError as e:
      print("\033[1;31;40mThat bank account does not exist.\033[0m",e)   
   continue
 #function to deposit an amount by asking the user to input an account number from which to withdraw  
 def deposit_amount (self):   
    try:
# then inside a for loop I traverse my bank account list and compare the bank # entered with the ones stored in the list
# if there is a match, I display that account info and ask for the amount to be deposited into it
     while True:
       account_number = int(input("Please enter the account number for which you'd like to to make a deposit: "))
       for i in range(len(self.bank_accounts_collections)):
           if self.bank_accounts_collections [i].get_account_number() == account_number:
               print("\nThe Account Details for the selected bank account are: ")
               self.bank_accounts_collections[i].display()
               amount = int(input("\nPlease enter the amount that you'd like to deposit: "))
               if(amount>0):
                   self.bank_accounts_collections [i].add_amount(amount)
                   print("\033[32m\nYour Funds were Successfully Deposited\033[0m")
                   print ("\nThe Updated  Account Details for ",self.bank_accounts_collections[i].get_acc_name()," are: ") 
                   self.bank_accounts_collections [i].display()
               else:
                    print("\nThe amount to be deposited must be greater than 0!")
               break
       another_depo = input("Make Another Deposit ? (y/n): ").strip().lower()
       if  another_depo != 'y':
        break
    except ValueError:
         print("Please enter a valid account number containing only numbers.")
    except IndexError :
         print ("That bank account does not exist.")

#function to withdraw an amount by asking the user to input an account number from which to withdraw 
 def withdraw_amount(self):
  
   try:
# then inside a for loop I traverse my bank account list and compare the bank # entered with the ones stored in the list
# if there is a match,I display that account info and ask for the amount to be withdrawn
        account_number = int(input("Please enter the account number for which you'd like to make a withdraw: "))
        for i in range(len(self.bank_accounts_collections)):
            if self.bank_accounts_collections [i].get_account_number() == account_number:
                print ("\nThe Account Details for the selected bank account are: ") 
                self.bank_accounts_collections [i].display()
                amount = int(input("\nPlease enter the amount that you'd like to withdraw: "))
                if (amount>0):
                     self.bank_accounts_collections[i].withdraw_amount (amount)
                else:
                     print("\nThe amount to be withdrawn must be greater than O!")
                break
   except ValueError as ve:
       print("Please enter a valid account number containing only numbers.")
   except IndexError as e:
       print("That bank account does not exist.")  


 def transfer(self):
    while True:
        try:  
        
            self.source_account_num = int(input("Please enter the account number for which you'd like to make a Transfer From: ")) 
            self.target_account_num =int(input("Please enter the account number for which you'd like to make a Transfer To: "))
            self.transfer_amount = int(input("\nPlease enter the amount that you'd like to Transfer: "))
            for i in range(len(self.bank_accounts_collections)):
               if self.bank_accounts_collections [i].get_account_number() == self.source_account_num:
                
                #Condition Checking to see wether you hav sufficient funds
                  if (self.bank_accounts_collections[i].get_balance()-self.transfer_amount>0 and  self.transfer_amount>0 ): 
                     self.bank_accounts_collections[i].withdraw_amount (self.transfer_amount)
                  else:
                     print("\033[1;31;40m\nYou do not have sufficient funds to make this Transfer\033[0m") 
                     break
                

               if self.bank_accounts_collections [i].get_account_number() == self.target_account_num :   
                #Making Deposit to Account you want to transfer funds to
                 self.bank_accounts_collections [i].add_amount(self.transfer_amount)
             
                 print("\033[32m\nYour Funds were Successfully Transfered\033[0m")
                 print ("\nThe Account Details for ",self.bank_accounts_collections[i].get_acc_name()," are: ") 
                 self.bank_accounts_collections [i].display()
                 return
           
            
        except ValueError:
         print("\033[1;31;40mPlease enter a valid account number containing only numbers.\033[0m")
         continue
        except IndexError:
         print("\033[1;31;40mThat bank account does not exist.\033[0m")
         continue

 def check_balance(self):
  global count
  try:
       if len(self.bank_accounts_collections)==0:
           print("\033[1;31;40mThe list is empty, You need to add a Bank Account first\033[0m")
           print ("\n")
          # self.menu()
           return
               
       account_number = int(input("Please enter the account number for which you'd like to display its Balance: "))
       for i in range(self.count):
           
           if self.bank_accounts_collections [i].get_account_number() == account_number:
              print("\nYour Account Balance is: ",self.bank_accounts_collections[i].get_balance())
              
              break
  except ValueError as ve:
      print("\033[1;31;40mPlease enter a valid account number containing only numbers.\033[0m")
  except IndexError as e:
      print("\033[1;31;40mThat bank account does not exist.\033[0m") 
      
          
#main function to be called from main containing the menu displaying the different choices for the user       
 def menu(self):
    print( """\033[34m
                       Welcome to My Banking Application
                    -------------------------------------------------------------
                           1)Open new account "
                           2)Display all account details "
                           3)Deposit an amount "
                           4)Check Balance"
                           5)Withdraw an amount "
                           6)Transfer "
                           7)quit "
                           
                         \033[0m""")
    while True:
        try: 
            option=self.execute_choice()  
                      
            if (option == '1'):
               self.open_new_account()
            elif (option == '2'):
              self.display_account_details()
            elif (option == '3'):
              self.deposit_amount ()
            elif (option == '4'):
              self.check_balance()  
            elif (option == '5'):
              self.withdraw_amount()
            elif (option == '6'):
              self.transfer()
            elif (option == '7'):
              self.exit_program()
            else:
               print("\033[1;31;40m Invalid input. Please enter a number between 1 and 6.\033[0m")
               
        except ValueError:
            print ("\033[1;31;40m Please enter a valid account number containing only numbers.\033[0m")
        except IndexError :
            print("\033[1;31;40m That bank account does not exist.\033[0m")     
        self.continue_operation()


 def exit_program(self):
    print("\033[1;31;40m \nExiting the program...\nGood Bye!!\033[0m")
    sys.exit(0)
    
 def continue_operation(self):
         user_input = input("Do you want to exit the program? (y/n): ")
         if user_input.lower() == "y":
          self.exit_program()
               # Continue  and call  the main function
         elif user_input.lower() == "n":
          self.menu()
 def execute_choice(self):

  return   str(input("Please select one of the following options: "))