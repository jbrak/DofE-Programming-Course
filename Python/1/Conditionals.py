trainName = "freddy"
trainType = "diesel"
trainUse = "passengers"
trainLength = 9
trainAge = 50
trainWorking = True

#Write weather the folowing statements are true or false.
(10 > 9) == True
(12 == 9) == False
(78 > 100) == False
(42 <= 21) == False
(1314 >= 212) == True
(1232 < 123) == False

#Print the trains name
print(trainName)

#Fix this piece of code
if trainWorking == True:
    print("Hurray!\nThe train is in operation!")

#If the train is older than 60 years old then print: "The train is too old!".
#If the train is inbetween 45 and 60 years old then calculate the amount of
#Years until it is 60. Print this.
#If the train is less than 45 years print: "The train is still in operation."
if trainAge > 60:
    print("the train is too old")
elif trainAge > 45 and trainAge < 60:
    print(60-trainAge)
else:
    print("the train is still operation")
#If the amount of carrages is greater than or equal to 10 print: "This train can
#carry lots of people"
#If the amount of carrages is less than or equal to 9 print: "this train can not
#carry many people"
if trainLength >= 10:
    print("the train can carry lots of people")
else:
    print("the train can not carry many people")

#If the train is steam print: "Yay the train is good for the enviroment"
#If it isn't print: "Noo the train is not good for the enviroment"
if trainType == "steam":
    print("yay the train is good for the enviroment")
else:
    print("noooooooooooooo the train is not good for the enviroment")
