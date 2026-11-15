from decimal import Decimal
num:int = 1
execution = 10.9
str1 = "Are multiple 'words' to btao km se km"
study = True
list1 = ["kapil",29,87.5]
list2 = []
list3 = list()
tuple1 = (1,4,4,2,6,5)
limit = range(5,100)
result = None
library = {"name":"kapil", "age":29, "height":"6feet", 88:"Weight"}
set1 = {1,4,"kapil"}
set2 = {1,3,3,6,5,100, 500, 250, 4, "Kapil", "Apple"}
print(library["name"],library[88])
empty_set = {*()}
print(type(empty_set))
print(set2)
print(tuple1)
m = 1.1
n = 0.8
t = 3.1449595
print(round(m+n,1))
print(Decimal(str(m))+Decimal(str(n)))
print(list(limit))
#DataTypes , type(), round(), Decimal(), str(), hint "m:int=1",list()