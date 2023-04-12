amazon_cart = ['notebooks','sunglasses','toys']
print(amazon_cart[:])#accessing with index

#strings are immutable,list is mutable
string1 = "Khine"
#error ----> 'str' object does not support item assignment
# string1[0] = "U"
# print(string1)

amazon_cart[0] = "earphones"
print(amazon_cart)

new_cart = amazon_cart[0:2]
print(new_cart)

#List methods
#adding
#append()
#extend()--->adding another list into old list
#insert()

#append
amazon_cart.append("Books")#adding elements at the end of the list
print(amazon_cart)

#extend
amazon_cart.extend(["tv","headphone"])
print("After Extending : ",amazon_cart)

basketball = [1,2,3,4,5]
basketball.extend([100,10])#extend doesn't return
print(basketball)

#insert
#amazon_cart --- > ['earphones', 'sunglasses', 'toys', 'Books', 'tv', 'headphone']
amazon_cart.insert(4,"apple")
print("After inserting at index 4",amazon_cart)
#['earphones', 'sunglasses', 'toys', 'Books', 'apple', 'tv', 'headphone']
