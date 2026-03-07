'''
try:
  x=int(input("Enter a number: "))
  y=int(input("Enter another number: "))
  c=x+y
  print(c)
except TypeError:
    print("Type error")

except ValueError:
    print("Enter a valid number")
'''
try:
  x=int(input("Enter a number: "))
  y=int(input("Enter another number: "))
  c=x/y
  print(c)
except TypeError:
    print("Type error")

except ZeroDivisionError:
    print("Give a non zero number")

else :
   print("There is no error")

finally :
    print("Finally will always execute")