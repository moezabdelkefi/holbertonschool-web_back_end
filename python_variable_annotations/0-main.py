#!/usr/bin/env python3

"""
 a type-annotated function add that takes a float
 a and a float b as arguments and returns their sum as a float
"""
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
