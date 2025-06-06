"""
Description: Introduction to Logic
Author:  Amanda Dadalt Makino
Date: June 02, 2025
Usage: To execute, press the play button in the VSC IDE.
"""

# Variables used in this demonstration:
age = 18
sibling_age = 9
horizontal_position = -1
vertical_position = 5
number = 5
fruits = ["apple", "banana", "cherry"]


# CONDITIONALS
# If Statement
if age < 13:
    print("Child")
elif age < 18:
    print("Teen or Adult")
elif age < 20:
    print("Young Adult")
else:
    print("Adult")

# NESTED CONDITIONALS
if horizontal_position > 0: 
    if vertical_position > 0:
        print("Horizontal and Vertical are positive.")
    else:
        print("Horizontal is positive, but Vertical is not.")
else:
    if vertical_position > 0:
        print("Vertical is positive, but Horizontal is not.")
    else:
        print("Both Horizontal and Vertical are negative.")

# COMPARISON OPERATORS:

# == equality.  Returns True if both operands are equal, false otherwise.
# != inequality. Returns True if operands are not equal, false otherwise.
# < less than. Returns True if first operand is less than second, false otherwise.
# > greater than. Returns True if first operand is greater than second, false otherwise.
# <= less than or equal.Returns True if first operand is less than or equal to second, false otherwise.
# >= greater than or equal. Returns True if first operand is greater than or equal to second, false otherwise.

# Examples:

first_operand = 5
second_operand = 10
print(first_operand == second_operand) # False
print(first_operand != second_operand) # True
print(first_operand < second_operand) # True
print(first_operand > second_operand) # False
print(first_operand <= second_operand) # True
print(first_operand >= second_operand) # False


# LOGICAL OPERATORS

if age > 0 and sibling_age > 0:
    print("Both values are positive.")
if age > 9 or sibling_age > 9:
    print("At least one value is greater than 9.")
if not age > 10:
    print("Age is not greater than 10.")
if not sibling_age > 10:
    print("Sibling age is not greater than 10.")

# TERNARY EXPRESSION
# given expression:

"""
if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"

print("result")
"""

result = "Even" if number % 2 == 0 else "Odd"
print(result)

print("Even" if number % 2 == 0 else "Odd")


# MEMBERSHIP CHECKING

print("banana" in fruits)
print("orange" not in fruits)
text = "Hello world!"
print("world" in text)

searched_fruit = "banana"

if searched_fruit in fruits:
    print("Found", searched_fruit)
else:
    print(searched_fruit, "not found")