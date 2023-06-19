class Calculator:
    @staticmethod
    def addNumbers(x,y):
        return x + y

if __name__ == '__main__':
    result = Calculator.addNumbers(10,20)
    print(result)