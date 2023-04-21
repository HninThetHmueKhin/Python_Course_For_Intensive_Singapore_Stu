#Recursive ---> clean
#5! --->
#recursion logic hard to follow
#hard to debug
#inefficient
def factorial(x):#1
    """This is a recursive function to find the factorial of an integer"""
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))#5*4*3*2*1=120
if __name__ == '__main__':
    num = int(input("Enter num : "))
    result =factorial(num)
    print('The factorial of',num,"is",result)