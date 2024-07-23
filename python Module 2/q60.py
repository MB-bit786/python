#Pick a Random Item from a List or Tuple
import random

my_list = [1, 2, 3, 4, 5]
print(random.choice(my_list))
print(random.choice(range(1, 100)))  #Pick a Random Item from a Range
print(random.randint(1, 100))  #print(random.randint(1, 100))

random.seed(10)    #Set the Starting Value in Generating Random Numbers
print(random.random())  

random.shuffle(my_list)  #Randomize the Items of a List in Place
print(my_list)
