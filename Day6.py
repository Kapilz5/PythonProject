# 1. Standard Literal (Parentheses)
a = (1, 2, 3)

# 2. Packing Without Parentheses (Implicit Tuple)
b = 10, 20, 30               # Evaluates to (10, 20, 30)

# 3. Single-Element Tuple (CRITICAL EDGE CASE)
# Python requires a trailing comma for 1-element tuples!
not_a_tuple = (5)            # Evaluates to int 5!
single_tuple = (5,)          # <class 'tuple'>
single_tuple2 = 5,           # <class 'tuple'>

# 4. Empty Tuple
e1 = ()
e2 = tuple()

# 5. tuple() Constructor (Converts iterables like list, str, set, range)
t1 = tuple([1, 2, 3])        # (1, 2, 3)
t2 = tuple("abc")            # ('a', 'b', 'c')
t3 = tuple(range(4))         # (0, 1, 2, 3)

# 6. Repetition / Multiplication
r = (0,) * 5                 # (0, 0, 0, 0, 0)

t = (10, 20, 30, 40, 50)

# Positive & Negative Indexing
print(t[0])        # Output: 10
print(t[-1])       # Output: 50

# Slicing (Returns a NEW tuple)
print(t[1:4])      # Output: (20, 30, 40)
print(t[::5])      # Output: (10, 30, 50)
print(t[2:1:-1])     # Output: (50, 40, 30, 20, 10) (Reversed tuple)

#Sequence Unpacking
point = (10, 20, 30)
x, y, z = point              # x=10, y=20, z=30
print(x, y, z)
point1 = [10, 20, 30]
a,b,c = point1
print(a,b,c)
# Extended Unpacking using Asterisk (*)
first1, *middle1, last1 = (1, 2, 3, 4, 5, 6)
print(first1)   # 1
print(middle1)  # [2, 3, 4] (Extracted as a list)
print(last1)    # 5

first, *_, last = (1, 2, 3, 4, 5, 6)
print(first)   # 1
print(last)    # 5

#Swapping Variables without Temp Variable
a, b = 5, 10
a, b = b, a                  # Tuple packing and unpacking under the hood!
print(a, b)                  # Output: 10, 5

#Built-in Methods & Utility Functions
t = (1, 2, 3, 2, 4, 2, -1)

# 1. .count(val): Returns frequency of val
print(t.count(2))            # Output: 3

# 2. .index(val): Returns index of first occurrence of val (raises ValueError if absent)
print(t.index(4))            # Output: 4

# Global functions working on tuples
print(len(t))                # 6
print(min(t))                # 1
print(max(t))                # 4
print(sum(t))                # 14
print(sorted(t))             # Returns a NEW sorted LIST: [1, 2, 2, 2, 3, 4]

#Immutability Edge Cases & Concatenation

#hash()
