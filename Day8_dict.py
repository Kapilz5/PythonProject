# 1. Standard Literal (Curly Braces with key: value)
user = {"name": "Kapil", "age": 28, "role": "Dev"}

# 2. Empty Dictionary
e1 = {}
e2 = dict()

# 3. dict() Constructor using keyword arguments
user2 = dict(name="Alice", age=25)

# 4. dict() with list/tuple of key-value pairs
pairs = [("a", 1), ("b", 2)]
d1 = dict(pairs)                # {'a': 1, 'b': 2}

# 5. Dictionary Comprehension
d2 = {x: x**2 for x in range(5)} # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 6. dict.fromkeys(keys_seq, default_val)
keys = ["id", "score", "rank"]
d3 = dict.fromkeys(keys,0)
print(d3) # {'id': 0, 'score': 0, 'rank': 0}

profile = {"name": "Kapil", "city": "Delhi"}

# Direct Bracket Access (Throws KeyError if key is missing)
print(profile["name"])          # Output: Kapil
# print(profile["age"])         # 💥 KeyError: 'age'

# Safe Access using .get(key, default)
#print(profile.get("name"))      # Output: Kapil
#print(profile.get("age"))       # Output: None (No error!)
print(profile.get("age", 0))    # Output: 0 (Returns custom default if absent)

# Key Existence Check
print("city" in profile)        # Output: True

data = {"a": 1, "b": 2}

# 1. Adding / Updating via Bracket Assignment
data["c"] = 3                   # Adds key 'c' -> {'a': 1, 'b': 2, 'c': 3}
data["a"] = 100                 # Updates existing key 'a'

# 2. .setdefault(key, default): Gets value if exists; inserts key with default if missing
data.setdefault("d", 400)       # Adds 'd': 400

print(data)
# 3. .update(other_dict): Merges another dictionary in-place
data.update({"b": 200, "e": 5}) # Updates 'b' and adds 'e'
print(data)
# 4. Deleting Items
del data["a"]                   # Removes key 'a'
print(data)
val = data.pop("b")             # Removes key 'b' and RETURNS its value (200)
print(data)
print(val)
last_pair = data.popitem()      # Removes and returns LAST inserted (key, value) tuple
data.clear()                    # Empties dictionary {}
print(data)

car = {"brand": "Tesla", "model": "Model 3", "year": 2024}

# 1. Keys Iteration (.keys())
for key in car.keys():          # or simply `for key in car:`
    print(key)

print("line change")
# 2. Values Iteration (.values())
for val in car.values():
    print(val)

print("line change")


# 3. Key-Value Tuple Iteration (.items())
for key, val in car.items():
    print(f"{key} -> {val}")

# forkeys(), items(), values(), keys(), popitems(), update(), setdefault(),