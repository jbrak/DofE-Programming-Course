#Write a For loop that prints "monkey" and i 20 times
for i in range(1,21):
    print("monkey",i)
#Write a while loop that does the same thing
v = 0
while v < 21:
    print("monkey",v)
    v += 1

#Write a For loop that multiplys i by 2 if below 5 and 3 if above 5. THe loop should run 10 times
for i in range(1,11):
    if i < 5:
        print(i * 2)
    else:
        print(i * 3)

#Write an infinate loop that breaks when x == 100. Print x.
x = 0
while True:
        print(x)
        if x == 100:
            break
        x = x + 1
#Write a program that prints 10 random floats in between i & i-1
#So if i = 2 the program will print 10 random numbers between 1 and 2
import random
for i in range(1, 11):
    for j in range(1, 11):
        print(random.uniform(i-1, i))
