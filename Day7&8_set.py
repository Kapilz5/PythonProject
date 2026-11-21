# 1. Standard Literal (Curly Braces with items)
a = {1, 2, 3, 4}

# 2. Empty Set Initialization (CRITICAL RULE)
# Note: {} creates an empty dict, NOT a set!
empty_set = set()              # Correct <class 'set'>
trick_set = {*()}              # Unpacking trick <class 'set'>

# 3. set() Constructor (Converts iterables & deduplicates)
s1 = set([1, 2, 2, 3, 3, 4])   # {1, 2, 3, 4}
s2 = set("banana")             # {'b', 'a', 'n'}
s3 = set(range(5))             # {0, 1, 2, 3, 4}

# 4. Set Comprehension
s4 = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}

print(s4)
# 5. Immutable Set (frozenset)
frozen = frozenset([1, 2, 3])  # Cannot be modified; CAN be a set element or dict ke
print(frozen)

fruits = {"apple", "banana"}
fruits.add("cherry")               # {"apple", "banana", "cherry"}
fruits.update(["mango", "grape"])  # Adds all items to the set
print(fruits)

tags = {"python", "coding", "data"}
tags.remove("coding")      # Removes 'coding'
tags.discard("java")       # Safe remove: does nothing, no KeyError

removed_item = tags.pop()  # Removes and returns a random element
tags.clear()               # Set is now set()

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 1. Union (|): All elements from both sets
print(A | B)                    # {1, 2, 3, 4, 5, 6}
print(A.union(B))

# 2. Intersection (&): Shared elements only
print(A & B)                    # {3, 4}
print(A.intersection(B))

# 3. Difference (-): Elements in A but NOT in B
print(A - B)                    # {1, 2}
print(A.difference(B))

# 4. Symmetric Difference (^): Elements in A or B, but NOT both
print(A ^ B)                    # {1, 2, 5, 6}
print(A.symmetric_difference(B))

#In-Place Set Updates - Adding _update to methods updates the original set instead of returning a new one:
A.intersection_update(B)  # A becomes {3, 4}
print(A)

#Set Comparison & Subset Methods
x = {1, 2}
y = {1, 2, 3, 4}
z = {5, 6}

# Subset & Superset Checks
print(x.issubset(y))           # True (x <= y)
print(y.issuperset(x))         # True (y >= x)

# Disjoint Check (returns True if sets share ZERO elements)
print(x.isdisjoint(z))         # True
print(x.isdisjoint(y))         # False (share 1 and 2)

#union(), intersection(), difference(), symmetric_difference(), intersection_update()
# issubset(), issuperset(), isdisjoint(), discardS