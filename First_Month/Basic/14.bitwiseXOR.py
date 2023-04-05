#Bitwise (^) XOR
# တူရင် 0 မတူရင် 1
#truth table
#x y | output
#0 0 | 0
#0 1 | 1
#1 0 | 1
#1 1 | 0

a = 5 # 101
b = 3# 11

# 1 0 1
#   1 1
#  1  1 0 ---> 6
c = a ^ b
print("XOR result: ",c)