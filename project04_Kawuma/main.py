import sys

from Parallelepiped import Parallelepiped
from Rectangle import Rectangle


def main():
        while True:
            try:
               length= float(input("Enter a positive integer for Length: "))
               width= float(input("Enter a positive integer for width: "))
    
               #creating an obj rect of class Rectangle
               rect= Rectangle(length,width)
               # Newline
               print("\n")
               rect.display()
               height = float(input("Enter a positive integer for Height: "))
               #creating an obj rect of class Rectangle
               para = Parallelepiped(length,width,height)
               para.display()
               
               user_input = input("Do you want to exit the program? (y/n): ")
               if user_input.lower() == "y":
                exit_program()
               # Continue  and call  the main function
               else:
                   main() 
            #try and except block to get an invalid input is detected, an error message is displayed
            except ValueError:
               print("Invalid input. Please enter positive integers.")
               main() 
               
def exit_program():
    print("Exiting the program...")
    sys.exit(0)       
if __name__ == "__main__":
    main()