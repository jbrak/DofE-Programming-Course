#The user enters a yes or no question
#The computers returns a random Magic 8 Ball Statement to the awnser.
#Here are the statments it should select randomly from to awnser the question.
'''
Yes, Definatly
It is very likely
Maybe
That's pretty unlikely
Thats impossible
Why do you ask me a question you already know the awnser to?
50/50
'''

from random import choice
awn = ["yes, Definatly", "It is very likey", "Maybe", "that's pretty unlikely", "thats impossible", "Why do you ask me a question you already know the awnser to?", "50/50"]
input("enter a yes or no question:\n")
print(choice(awn))
