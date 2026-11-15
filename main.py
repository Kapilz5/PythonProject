from decimal import Decimal
a=1
b="like"

c=1.1
d=0.8
print(f"number is :",a,b)
print(round(c+d,1))
print(Decimal(str(c)) + Decimal(str(d)))