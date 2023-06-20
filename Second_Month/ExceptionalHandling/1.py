#exceptional handling --> try except finally
#ZeroDivisionError
#ValueError
#NameError
#FileNotFoundError
"""
try:
  #code
except:
  #:exception code
else:
  #no exception code
finally:
 #whenever
#try code --> else code
"""
try:
    a = 10/0
except:
    print("Some exception occured.")
finally:
    print("This is from finally")