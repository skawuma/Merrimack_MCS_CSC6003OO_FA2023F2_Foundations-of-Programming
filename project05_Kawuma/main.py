import sys

from Nurse import Nurse

from Surgeon import Surgeon
from Doctor import Doctor
from Personnel import Personnel


def main():
        while True:
            try:
               print( """
                        Hospital Personnel records
        -              -------------------------------------------------------------
                        1.Doctors.
                        2.Surgeon.
                        3.Nurses.
                         """)
               ans=True
               while ans:
                 ans = str(input("Please Select Your Department Listed Above "))
                 if ans =="1":
                   option1()
                 elif ans =="2":
                    option2()
                 elif ans =="3":
                    option3()  
                 user_input = input("Do you want to exit the program? (y/n): ")
                 if user_input.lower() == "y":
                  exit_program()
               # Continue  and call  the main function
                 else:
                   main() 
            #try and except block to get an invalid input is detected, an error message is displayed
            except ValueError:
               print("Invalid input. Please enter positive Value.")
               main()
               
def option1(): 
     name= str(input("Enter your Name "))
     age=  int(input("Enter a your Age: "))    
     hr_rate= float(input("Enter a your Hourly Rate: "))
     spe = str(input("what is your Speciality"))
     #creating an obj rect of class Rectangle
     person= Doctor(name,age,hr_rate,spe)
     # Newline
     print("\n")
     person.displayDoctor()   
     
def option2():
     name= str(input("Enter your Name "))
     age=  int(input("Enter a your Age: "))    
     hr_rate= float(input("Enter a your Hourly Rate: "))
     b_cert = str(input("Are You Boad Certified, Answer 'Yes' or 'No' "))
     
     
    #creating an obj rect of class Rectangle
     person= Surgeon(name,age,hr_rate,b_cert)
     # Newline
     person.displaySurgeon() 
     if b_cert == "Yes":
          print( "And Board Certified")
     elif b_cert == "No":
            print( "And is Not Board Certified")
   
  
     
def option3():
    name= str(input("Enter your Name "))
    age=  int(input("Enter a your Age: "))    
    hr_rate= float(input("Enter a your Hourly Rate: "))
    print( """
     ********************** NURSING RANKS*******************8
    -------------------------------------------------------------
                        1.CNA
                        2.LPN.
                        3.RN.
                        4.NP.
            """)
    b_cert = str(input("Please Enter Your Rank As a Nurse"))
    #creating an obj rect of class Rectangle
    person= Nurse(name,age,hr_rate,b_cert)
     # Newline
    print("\n")
    person.displayNurse()
              
def exit_program():
    print("Exiting the program...\nGood Bye!!")
    sys.exit(0)       
if __name__ == "__main__":
    main()