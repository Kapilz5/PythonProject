fruits = ["apple", "banana"]

# append(x): Adds 1 single item to the end
fruits.append("cherry")         # ["apple", "banana", "cherry"]

# extend(iterable): Unpacks and appends multiple items to the end
fruits.extend(["mango", "fig"]) # ["apple", "banana", "cherry", "mango", "fig"]

# insert(index, x): Inserts item at index, shifting existing items right
fruits.insert(1, "orange")

data = [10, 20, 30, 40]

# Update single element
data[1] = 25                    # [10, 25, 30, 40]
data[-1] = 99                   # [10, 25, 30, 99]

# Update slice (replace multiple items)
data[1:3] = [200, 300]          # [10, 200, 300, 99]
data[1:3] = [250]
print(data)

items = ["a", "b", "c", "d", "e"]
print(items)
del items[0]
print(items)# ['b', 'c', 'd', 'e']
val = items.pop(2)
print(val)
print(items)# Removes index 2 ('d') -> returns 'd' -> items: ['b', 'c', 'e']
items.remove("b")
print(items)# Removes value 'b' -> items: ['c', 'e']
items.clear()             # []
print(items)

# 1. Element by Element (Loop)
'''nums = []
for i in range(int(input("List Size: "))): #range(n)
   nums.append(int(input(f"val {i}th index: ")))

# 2. Space-Separated Single-Line Input (Standard)
# Input: "10 20 30" -> split() gives ['10', '20', '30'] -> int converts each
numbers = [int(x) for x in input("Enter space-separated numbers: ").split()]

print(numbers)'''

colors = ["red", "green", "blue"]

# Standard format
print(colors)             # ['red', 'green', 'blue']

# Clean space-separated output using unpacking operator (*)
print(*colors)            # red green blue

# Custom separator
print(*colors, sep=", ")   # red, green, blue

# Iterating with index (enumerate)
for idx, item in enumerate(colors, start=1):
    print(f"Item {idx}: {item}")

'''Bonus Tip: Starting the Count at 1
If you want human-friendly numbering (1, 2, 3 instead of 0, 1, 2), pass start=1:

Python

for idx, item in enumerate(colors, start=1):
    print(f"Item #{idx}: {item}")
# Output:
# Item #1: red
# Item #2: green
# Item #3: blue'''

#pop(), append(), extend(), remove(), join(), insert(),id(), input(), int(), format(), split(), enumerate()