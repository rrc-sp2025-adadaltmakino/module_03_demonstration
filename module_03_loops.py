"""
Description: Introduction to Loops
Author: Amanda Dadalt Makino
Date: June 02, 2025
Usage: To execute, press the play button in the VSC IDE.
"""

# Variables used in this demonstration:
fruits = ["apple", "orange", "banana", "cherry"]
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


# FOR LOOP
for fruit in fruits: 
    print(fruit)

for i in range(-10, 0):
    print(i)

"""
# INPUT FUNCTION

# print(f"Name: {name} \nSalary: ${salary:,.2f}")


# WHILE LOOP

favorite_number = 0
while favorite_number < 100:
    favorite_number = int(input("Enter your favorite number (but not 7), 100 & up to quit: "))
    if favorite_number == 7:
        print("You broke this game.")
        #break
else: 
    print("Your favorite number is too big.")

# LOOP CONTROL STATEMENTS

# CONTINUE:

for number in range(1, 10):
    # Use continue statement to skip over multiples of 3.
    if number % 3 == 0:
        continue
    # Print all other integers
    print(number)


#BREAK:

# Use a for loop to iterate over the range of integers 
for number in range(1, 10):
    # Use the break statement to exit the loop if the integer is greater than 5
    if number > 5:
        break
    # Print all other integers.
    print(number)
"""

# INFINITE LOOP
# <ctrl> + c (in the terminal window) to stop an infinite loop in VS Code.
number = 10 
while number > 0 :
    if number > 100:
        break
    number += 1 
    print(number)

# NESTED LOOP
# matrix variable defined at top of editor.

for row in matrix:
    for element in row:
        print(element, end = '')
        print()