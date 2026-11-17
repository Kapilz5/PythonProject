import copy

students = [("Height",6),("Weight",88)]
students.sort(key=lambda x: x[1])
print(students)

original = [3, 1, 2]
n = sorted(original)
print(n)
print(original)

original1 = [3, 1, 2,6]
original1.sort()
print(original1)

arr = [10, 20, 30, 20]

print(arr.index(20))     # Output: 1 (first occurrence index)
print(arr.count(20))     # Output: 2 (total count)
print(20 in arr)         # Output: True (membership check)


# Standard Assignment (=): Shares SAME memory address (NOT a copy!)
orig = [1, 2, 3]
ref = orig
ref.append(4)            # orig becomes [1, 2, 3, 4]!

# Shallow Copy (.copy() or list[:]): Copies top-level list, but nested lists share references
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0][0] = 99       # nested ALSO becomes [[99, 2], [3, 4]]!
shallow.append([5,6,7])
print(shallow)
print(nested)
# Deep Copy (copy.deepcopy()): Recursively duplicates all nested levels completely
deep = copy.deepcopy(nested)
deep[0][0] = 777         # nested remains [[99, 2], [3, 4]] (completely isolated)

#list.sort() vs sorted(), index(), count()