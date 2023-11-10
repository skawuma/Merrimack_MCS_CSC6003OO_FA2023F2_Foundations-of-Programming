def evenly_divides():
    while True:
        try:
            num1 = int(input("Enter the first positive integer: "))
            num2 = int(input("Enter the second positive integer: "))
            # condition to check If both numbers are positive integers,
            if num1 <= 0 or num2 <= 0:
                print("Both numbers must be positive integers. Please try again.")
                continue
            # Condition to check if the function checks whether either one evenly divides the other 
            if num1 % num2 == 0 or num2 % num1 == 0:
                return True
            else:
                return False
            #try and except block to get an invalid input is detected, an error message is displayed
        except ValueError:
            print("Invalid input. Please enter positive integers.")

if evenly_divides():
    print("Either one number evenly divides the other.")
else:
    print("Neither Two of  evenly divides the other.")