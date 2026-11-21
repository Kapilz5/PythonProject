#Modifying a Mutable Object Inside a Tuple
t = (1, 2, [10, 20])
t[2].append(30)              # VALID! Inner list is modified.
print(t)                     # Output: (1, 2, [10, 20, 30])

# BUT: Reassigning the list raises TypeError
# t[2] = [1, 2]              # TypeError: 'tuple' object does not support item assignment
#Joining & Concatenating Tuples
a = (5,6)
b = (2,8)
a += b
print(a)

d = 5
e = 6
e = d+e
print(e)

#Hashability & Dict Keys
valid_key = (1, 2, "a")      # Hashable -> Valid dict key / set item
invalid_key = (1, 2, [3, 4])  # Unhashable -> Raises TypeError!

