#pop
amazon_cart = ['apple','notebooks','sunglasses','toys']
# pop_element = amazon_cart.pop(1)#pop fun returns
# print("After pop",amazon_cart)
# print("Pop element: ",pop_element)

#remove doesn't return removing element
# r_e = amazon_cart.remove("toys")
# print(amazon_cart)
# print(r_e)#None

#sort
# amazon_cart.sort()#default --> ascending order
# print(amazon_cart)
#
# amazon_cart.sort(reverse=True)#descending order
# print(amazon_cart)

#sorting list by length of the values
def myFunc(e):
    return len(e)

# amazon_cart.sort(key=myFunc,reverse=True)
# print(amazon_cart)

#sorting function
# sorted(amazon_cart)
# print(amazon_cart)
# new_cart = sorted(amazon_cart,reverse=True)
# print(new_cart)

new_cart2 = sorted(amazon_cart,key=myFunc)
print(new_cart2)

#copy()
new_amazon_cart = amazon_cart.copy()
print(new_amazon_cart)

#reverse()
amazon_cart.reverse()
print(amazon_cart)
print(amazon_cart[-4:])#not flexible
print(amazon_cart[::-1])

