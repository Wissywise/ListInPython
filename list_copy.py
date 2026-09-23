
"""
In Python, a list is a built-in data structure used to store an ordered, mutable (changeable), and heterogeneous
collection of items. Lists are written with square brackets [], with items separated by commas.Here is a quick
breakdown of their core characteristics:Ordered: Items maintain the exact order in which they were inserted.Mutable:
You can change, add, or remove items after the list is created.Heterogeneous: A single list can contain multiple
different data types at once (integers, strings, booleans, or even other lists).Allows Duplicates: The same value
can appear multiple times at different index positions.
"""

# A list of strings
fruits = ["apple", "banana", "cherry"]

# A list with mixed data types
mixed_list = [42, "hello", True, 3.14]

# An empty list
empty_list = []

"""
Accessing Items (Indexing & Slicing)Lists use zero-based indexing, meaning the first item is at position 0. You can 
also use negative numbers to count backward from the end
"""
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])   # Output: 'apple' (First item)
print(fruits[-1])  # Output: 'date'  (Last item)

# Slicing: Getting a sub-list from index 1 up to (but not including) index 3
print(fruits[1:3]) # Output: ['banana', 'cherry']

"""
Modifying a ListBecause lists are mutable, you can reassign items directly using their index position
"""
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"

print(fruits) # Output: ['apple', 'blueberry', 'cherry']

# Copying list
import copy

original_list = [1, 2, 3, 4, 5]

deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[0] = 100

print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)