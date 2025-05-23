# Task 1: Understanding Python Exceptions
num1 = int(input("Enter a number: "))
# testing the number with try/except...
try:
    100 / num1
except ZeroDivisionError:
    print("Oops! You cannot divide by zero")
except ValueError:
    print("Invalid Input! Please enter a valid number")
# the result if applicable:
else:
    print("100 divided by", num1, "is", 100/num1)

# Task 2: Types of Exceptions
list1 = [0, 1, 2]
str1 = "dog"
int1 = 20
# testing the structures again...
try: # index error
    list1[4]
except IndexError:
    print("This index is out of range!")
try: # type error
    str1 + int1
except TypeError:
    print("You can't add a string and an integer!")

# Task 3: Using try... except... else... finally
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
# the exception logic...
try:
    num2 / num3
except TypeError:
    print("You can't add two different datatypes!")
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print("Your division resut is:", num2/num3)
finally:
    print("This block always executes!")