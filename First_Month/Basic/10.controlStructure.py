"""
Control Structure in python
python မှာ switch case statement မရှိဘူး။ အဲ့ဒီ အစား if else ပဲသုံးတယ်။ match statement
"""
# 1.if
# 2.elif
# 3.else
#
# and
# or ||
# """
#largest number
a = 10
b = 20
c = 30
d = 140
largestNumber = None
if a>b and a>c and a>d:
    largestNumber = a
elif b>a and b>c and b>d:
    largestNumber = b
elif c>a and c>b and c>d:
    largestNumber = c
else:
    largestNumber=d
print(largestNumber)

