# this program prints out a random fruit
# author: gerrycallaghan2@gmail.com

#using lists
import random
fruits = ["Apple", "Orange", "Banana", "Pear"]

# we want a random number between 0 and length-1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print(f"A Random Fruit: {fruit}")

##using tuples
fruits = ("Apple", "Orange", "Banana", "Pear")

# we want a random number between 0 and length-1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print(f"A Random Fruit: {fruit}")