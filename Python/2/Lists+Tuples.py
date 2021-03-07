#Are the following Lists or Turples
#(1,3) = T
#[1,2,3,4,5] = L
#("Bat","dog","lemur","monkey") = T
#["I" "like", "Lemurs", "and", "monkeys"] = L
#[("lemur",10),("dog", 15), ("cat", 1), ("bat", 23)] = L of T

#Write a tuple containing your first name, date of birth, favorite color and favorite animal. Save it to a variable called profile
profile = ("jake", "19/04/09", "red", "lemur")

#Print the data at index 1 of profile
print(profile[1])

#Print the data at the end of profile without using index 3
print(profile[-1])

#Why can't I add more data to a Profile?
#Because its a turple

#Create a list of animals below. Save it to a variable called zoo.
zoo = ["lemurs", "snakes", "red eye tree frogs", "posion dart frogs", "reed lemurs"]
print(zoo)

#Print the length of this List
print(len(zoo))
print(zoo)

#The zoo got a new animal. Append a new animal to the list.
zoo.append("wolf")
print(zoo)

#One of the animals has been moved to another zoo and was replaced with a polar bear. Replace one of the list values with a polar bear.
zoo[1] = "polar bear"
print(zoo)

#Iterate through lst and add all the values that are 5 or less to new_lst.
lst = [10,2,4,2,6,2,1,2,34,5,6,21,4,5,63,1,7,4,1020]
new_lst = []

for i in lst:
    if i <= 5:
        new_lst.append(i)
print(lst)
print(new_lst)
