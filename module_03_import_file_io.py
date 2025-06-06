"""
Description: Introduction to Import Statements and File I/O
Author: Amanda Dadalt Makino
Date: June 02, 2025
Usage: To execute, press the play button in the VSC IDE.
"""

# IMPORT STATEMENTS
from math import sqrt
import math
import random
from pprint import pprint

# Variables used in this demonstration
radius = 12.5
square = 144
fruits = ["apple", "banana", "cherry"]

# USING IMPORTED MODULES
area = math.pi * radius ** 2
root = sqrt(square)
"""
print(root)
print (area)
"""
"""
# RANDOM

print(random.random())
print(random.randint(1,6))


# FILE I/O

with open("example.txt", "r") as file:
    content= file.read()
    print(content)

"""
# WITH CLAUSE

data = {}
with open("dict_example.txt", "r") as bob:
    for pawan in bob:
        key, value = pawan.strip().split('*')
        data[key] = int(value)
print(data)
pprint(data)


# READ INTO DICTIONARY


