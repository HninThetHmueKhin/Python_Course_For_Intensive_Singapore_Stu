#random.choice
import random
#for random.choice()---> list tuple dictionary ----> return random value
name = ["rose","sunflower","lily"]
print("Selecting elements: ",random.choice(name))

#random.sample(population,k)-----> population ဆိုတာ list,set or tuple ----> return list
subject = ["python","java","c","c++","c#","js"]
print("Selecting elements: ",random.sample(subject,2))

#random.shuffle
username = ["rose","jisoo","lisa"]
print("Before shuffle",username)
random.shuffle(username)
print("After shuffle",username)

#random.seed
random.seed(10)
print("Random no from seed(): ",random.random())

#random.uniform(start,end) #floating return
print("Random no from uniform: ",random.uniform(10.5,20.5))

#random.triangular(low,high,mode) ---> for floating number
print("Triangular result: ",random.triangular(10.5,20.5,2.5))
