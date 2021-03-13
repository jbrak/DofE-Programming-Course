#Create a dictionary called Doggies. The keys should be names and the value breeds.
doggies = {"sampson":"golden retrever", "moses":"poodel", "aaron":"husky", "jake":"labroaoodal"}

#Print the breed for any of their names
print(doggies["sampson"])

#Print all of the keys for your doggies dictionary
print(list(doggies.keys()))

#Print all of the Values for your doggies dictionary
print(list(doggies.values()))

#Have the reader enter the name of a famous person and then return there birthday.
#Use this dictionary:
birthdays = {
    'albert einstein': '03/14/1879',
    'benjamin franklin': '01/17/1706',
    'ada lovelace': '12/10/1815',
    'donald trump': '06/14/1946',
    'rowan atkinson': '01/6/1955'}
name = input("enter the name of a famous of person:\n").lower()

print(birthdays[name])
