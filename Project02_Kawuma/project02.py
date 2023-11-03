def evenly_divides():
    while True:
        try:
            num1 = int(input("Enter the first positive integer: "))
            num2 = int(input("Enter the second positive integer: "))
            if num1 <= 0 or num2 <= 0:
                print("Both numbers must be positive integers. Please try again.")
                continue
            if num1 % num2 == 0 or num2 % num1 == 0:
                return True
            else:
                return False
        except ValueError:
            print("Invalid input. Please enter positive integers.")

if evenly_divides():
    print("Either one number evenly divides the other.")
else:
    print("No number evenly divides the other.")