# Explanation

## 1. The evenly_divides() function starts by entering a while loop that will continue indefinitely until a valid input is received.

## 2. Inside the loop, the function uses try and except statements to handle any invalid input (e.g., non-integer input). If an invalid input is detected, an error message is displayed and the loop starts over again.

## 3. The function then checks whether both input numbers are positive integers. If either of them is not, an error message is displayed and the loop starts over again.

## 4.If both numbers are positive integers, the function checks whether either one evenly divides the other (i.e., whether there is no remainder when one number is divided by the other). If so, the function returns True. Otherwise, it returns False.

## 5.Finally, in the calling function, the boolean result returned by evenly_divides() is used to display an appropriate message.

