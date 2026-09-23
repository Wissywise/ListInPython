
"""
Method                 What it does                             Example                              Result
.append(item)         Adds an item to the end of the list.      nums = [1, 2]; nums.append(3)        [1, 2, 3]
.insert(index, item)  Inserts an item at a specific position.   nums = [1, 3]; nums.insert(1, 2)     [1, 2, 3]
.extend(iterable)     Appends multiple elements to the end.     nums = [1, 2]; nums.extend([3, 4])   [1, 2, 3, 4]
.remove(item)         Removes the first occurrence of a value.  nums = [1, 2, 3, 2]; nums.remove(2)  [1, 3, 2]
.pop(index)          Removes and returns the item at an index   nums = [1, 2, 3];                    Returns 3,
                    (defaults to the last item).                nums.pop()                          list becomes [1, 2]
.sort()             Sorts the list in place.                    nums = [3, 1, 2]; nums.sort()       [1, 2, 3]
"""
fruits = ["Apple", "Banana", "Cherry"]

fruits.append("Mango")

fruits.insert(1, "Orange")

fruits.remove("Banana")

print(fruits)