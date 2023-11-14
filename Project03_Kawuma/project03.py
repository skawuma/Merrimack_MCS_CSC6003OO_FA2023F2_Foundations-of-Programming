import random
from statistics import mean

def main():
   # Menu  do displya different operations required to be performed
    print( """
          WELCOME TO MY SIMPLE PROGRAM TO CARRY OUR ARRAY OPERATIONS
        --------------------------------------------------------------
    1.Write a Python program that takes an array of integers as input and calculates the sum of all the elements in the array.
    2.Write a Python program that takes an array of integers as input and finds the maximum and minimum values in the array.
    3.Write a Python program that takes two arrays of integers as input and calculates their element-wise sum. The two arrays should have the same length.
    4.Write a Python program that takes an array of integers as input and removes all duplicate elements, keeping only the unique elements in the array.
    5.Write a Python program that takes an array of integers as input and sorts the elements in ascending order.
    6.Write a Python program that takes an array of integers as input and checks if the array is sorted in non-decreasing order.
    7.Write a Python program that takes an array of integers as input and calculates the average (mean) of all the elements in the array.
              
    8.Exit/Quit
    """)
    #Enter a while loop to define condtions which a user can choose from to peform an operation
    ans=True
    while ans:

     ans = input("What would you like to do? ")
     if ans=="1":
        option1()
     elif ans=="2":
        option2()
     elif ans=="3":
        option3()
     elif ans=="4":
        option4()
     elif ans=="5":
        option5()  
     elif ans=="6":
        option6() 
     elif ans=="7":
        option7()  
     elif ans=="8":
      print("\n Thanks for Trying out my Program, Goodbye") 
      ans = None
     else:
       print("\n Not Valid Choice Try again")
# Declare  a global String to be accessed by each function to Get the number of numbers from the user 
array = "How many numbers do you want to enter into the Array?"
def option1():
# Get the number of numbers from the user
  num_numbers = input(array)

# Create an empty array to hold the numbers
  numbers = []
# Initialize sum to zero
  sum = 0; 
# Loop over the number of numbers and get the user's input
  for i in range(int(num_numbers)):
    numbers.append(random.randint(0, 10))
# Print the array of numbers
  print(numbers)  
     
#Loop through the array to calculate sum of elements 
  for i in range(0, len(numbers)):          
   sum = sum + numbers[i];    
     
  print("Sum of all the elements of an array: " + str(sum)); 

def option2():
# Get the number of numbers from the user
  num_numbers = input(array)

# Create an empty array to hold the numbers
  numbers = []
# Initialize sum to zero
# Loop over the number of numbers and get the user's input
  for i in range(int(num_numbers)):
    numbers.append(random.randint(0, 10))
# Print the array of numbers
  print(numbers)  
# Print the max and min Value
  print("The Maximum and Minimum Number of ", numbers )
  print (max(numbers),"and ", min(numbers), "respectively")  

def option3():
# Get the number of numbers from the user
 num_numbers = input(array)

# Create an two Empty random arrays to hold the numbers
 numbers = []
 numbers1= []
# Initialize sum to zero
# Loop over the number of numbers and get the user's input
 for i in range(int(num_numbers)):
   numbers.append(random.randint(0, 10))
 for i in range(int(num_numbers)):
   numbers1.append(random.randint(0, 10))
# Print the array of numbers
 print(numbers) 
 print(numbers1) 
 print("The element-wise sum is : ",end="")
 print([sum(x) for x in zip(numbers, numbers1)])

def option4():
# Get the number of numbers from the user
  num_numbers = input(array)

# Create an empty array to hold the numbers
  numbers = []
# Initialize sum to zero
# Loop over the number of numbers and get the user's input
  for i in range(int(num_numbers)):
    numbers.append(random.randint(0, 10))
# Print the array of numbers
  print(numbers)  
# Print The new array without duplicates
  print("The array after Duplicates are removed is : ",end="")
  print(list(set(numbers)))

def option5():
# Get the number of numbers from the user
  num_numbers = input(array)

# Create an empty array to hold the numbers
  numbers = []
# Initialize sum to zero
# Loop over the number of numbers and get the user's input
  for i in range(int(num_numbers)):
    numbers.append(random.randint(0, 10))
# Print the array of numbers
  print(numbers)  
# Sorting the Array
  numbers.sort()
  print("The array sorted in Ascending order is ",end="")
# Printing  The new array in ascending order
  print(numbers)


def option6():
# Get the number of numbers from the user
  num_numbers = input(array)

# Create an empty array to hold the numbers
  numbers = []
# Initialize sum to zero
# Loop over the number of numbers and get the user's input
  for i in range(int(num_numbers)):
    numbers.append(random.randint(0, 10))
# Print the array of numbers
  print(numbers)  
 # Checking if Array is sorted
# Apply all and range
  if (all(numbers[i] <= numbers[i + 1] for i in range(len(numbers)-1))):
   print("Yes, List is sorted.")
  else:
   print("No, List is not sorted.")

def option7():
# Get the number of numbers from the user
  num_numbers = input(array)

# Create an empty array to hold the numbers
  numbers = []
# Initialize sum to zero
# Loop over the number of numbers and get the user's input
  for i in range(int(num_numbers)):
    numbers.append(random.randint(0, 10))
# Print the array of numbers
  print(numbers)  
# Print THe average of the the array
  print("The mean of of the Array is ",end="")
  print (mean(numbers))
      
if __name__ == "__main__":
    main() 