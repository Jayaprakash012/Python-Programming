diameter=float(input("enter diameter"))
radious= diameter/2
area = 3.14159*radious*radious
print("radious of a circle is:", radious)
print("Area of the circle is:", area)
#program to take age as input and print value entered and its data type
age = int(input("Enter your age: "))
print("The age entered is:", age)
print("The data type of age is:", type(age))
#input 2 numbers and print the sum of the two number
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
sum=n1+n2
print("Sum of the two numbers is:", sum)
#take a number as a input,convert it to float and print both original and converted values with their data types
n1=input("Enter a number: ")
converted_value=float(n1)
print("Original value is:", n1,"datatype:",type(n1))

print("Data type of converted value is:",converted_value, type(converted_value))