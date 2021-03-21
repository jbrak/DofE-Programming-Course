#Create a function that prints a given perameter multiplied by 43
def times43(x):
    return x*43
print(times43(7564))
#Create a function that generates a list of 10 random integers between 1 and 50
from random import randint
def randomlist():
    lst = []
    for i in range(1,11):
        lst.append(randint(1,50))
    return lst
print(randomlist())

#Create a function called find, that takes 2 perameters:
#a list of numbers
#an integer
#The function should interate through the list looking for the number.
#If it is there return True. Otherwise return False.
def find(lst,num):
    for i in range(0, len(lst)):
        if num == lst[i]:
            return True
    return False
print(find(randomlist(),35))
