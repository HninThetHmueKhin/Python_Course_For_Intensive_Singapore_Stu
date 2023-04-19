#Random module
import random
random_no = random.random()
print("Random no: ",random_no)

#int return
#randint(lower,upper) ----> randint(0,9)
rand_int_no = random.randint(0,9)
print("Random no with randint: ",rand_int_no)

#randrange(start,stop,step) ---> randrange(0,9,2)
rand_range_no = random.randrange(0,15,3)#0 3 6 9 12
print("Random no with randrange: ",rand_range_no)