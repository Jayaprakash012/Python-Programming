try:
    x=int(input("Enter a number: "))
    y=int(input("Enter another number: "))
    z=x/y
    print("Result:", z)
except TypeError:
    print("Type error! Please enter valid numbers.")

except ValueError:
    print("Invalid input! Please enter a valid number.")

except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")

else:
    print("The operation was successful.")

finally:
    print("This block will always execute.")