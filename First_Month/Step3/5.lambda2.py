number = int(input("Enter number: "))
calc = lambda number:"Even Number" if number%2==0 else "Odd Number"
print(calc(number))