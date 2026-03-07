#write a python program that takes a user name as a input and prints its 1st,last and the length of the string.
from string import whitespace


name=(input("Enter your name: "))
print(name[0])
print(name[-1])
print(len(name))
#TAKE USER INPUT AND PRINT MIDDLE 3 CHARACTERS AND LAST 2 CHARACTERS

food=input("Enter your favourite food: ")
mid = len(food) //2 
output1 = food[mid-1:mid+2]
output2 = food[-2:]
print("Middle 3 characters: ", output1)
print("Last 2 characters: ", output2)

