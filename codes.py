# Variables and Data Types:

# 1. Write a program to declare an integer variable and print its value.
"""
num=int(input("enter a number:"))
print(num)
"""
# 2. Create a program that takes user input for their age and prints it.
"""
age=int(input("enter your age"))
print(age)
"""
# 3. Write a program that calculates the area of a rectangle (length * width).
"""
l=int(input("enter length:"))
w=int(input("enter width"))
print("area of rectangle=",l*w)
"""
# 4. Create a program that swaps the values of two variables.
"""
a=int(input("enter a number:"))
b=int(input("enter another number:"))
temp=0
print("a,b before swap:",a,b)
temp=a
a=b
b=temp
print("a,b after swap:",a,b)
"""
# 5. Write a program that concatenates two strings and prints the result.
"""
a=input()
b=input()
print(a+b)
"""

# 6. Develop a program that converts a Fahrenheit temperature to Celsius.
"""
f=int(input("enter a farenheit"))
Celsius=(f-32)*5/9
print(f,"into celsius is",Celsius)
"""

# 7. Create a program that takes a number as input, squares it, and prints the result.
"""
a=int(input("enter a number:"))
square=a*a
print("square of",a,"is",square)

"""

# 8. Write a program that checks if a number is divisible by both 5 and 7.
"""

num=int(input("enter a number:"))
if num%5==0 and num%7==0:
    print(num,"is divisible by both 5 and 7")
else:
    print(num,"is not divisible by both 5 and 7")

"""
# 9. Develop a program that calculates the average of three numbers.

"""
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
avg=((a+b+c)/3)
print("average is",avg)
"""

# 10. Create a program that uses different data types (int, float, string) in one statement.

"""
a=int(input("enter a integer"))
b=float(input("enter a float"))
c=input("enter a string")
print(a,b,c)
"""

# 11. Write a program to check if a given year is a leap year.
"""
num=int(input("enter a year"))
if num%400==0:
    print("it is a leap year")
else:
    print("it is not a leap year")
"""

# 12. Create a program that generates a random number and prints it.
"""
import random
r=random.randint(1,100)
print(r)
"""

# 13. Write a program that calculates the simple interest using user input for principal, rate, and
# time.
"""
principal=int(input("enter a principal"))
rate=float(input("enter a rate"))
time=float(input("enter a time"))
interest=(principal*rate*time)/100
print("interest is",interest)

"""
# 14. Develop a program that converts a string to uppercase.
"""
i=input("enter a string")
print(i.upper())
"""

# 15. Create a program that checks if a given number is positive, negative, or zero.
"""
a=int(input("enter a number:"))
if a>0:
    print("a is positive number")
elif a<0:
    print("a is negative number")
else:
    print("a is Zero")
"""

# 16. Write a program that concatenates three strings and prints the result.
"""
a=input()
b=input()
c=input()
result=a+""+b+""+c
print(result)
"""
# 17. Develop a program that converts a given number to a binary representation.
"""
def DecimalToBinary(num):
        if num >= 1:
            DecimalToBinary(num // 2)
        print(num % 2)
print(DecimalToBinary(25))
"""
# 18. Create a program that uses the `len()` function to find the length of a list.
"""
list=[1,2,3,4]
print(len(list))

"""
# 19. Write a program that uses the `input()` function to get the user's name and prints a
# greeting.
"""
a=input("enter ur name:")
print("Hello",a)

"""

# 20. Develop a program that calculates the sum of digits in a given number.

"""

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

num=int(input("enter a number"))
print("sum of digits is:",sum_of_digits(num))

"""

# Print() method Python:

# 1. **Basic Print:**
# - Write a program that prints "Hello, World!" to the console.
"""
print("Hello Woorld")
"""

# 2. **Multiple Prints:**
# - Create a program that uses multiple `print` statements to output a message with line
# breaks.
"""
print("Hello")
print("This is Print method")
"""


# 3. **Formatted Output:**
# - Write a program that uses formatted strings to print variables with descriptive messages.
"""
name=input("enter ur name:")
print(f"my name is  {name}")
"""


# 4. **String Concatenation:**
# - Develop a program that prints the concatenation of two strings.
"""
a=input()
b=input()
print(a+""+b)
"""

# 5. **Escape Characters:**
# -Create a program that uses escape characters to print a multi-line string.
"""
print("hello \n world")
"""

# 6. **Print without Line Break:**
# - Write a program that prints multiple items on the same line without line breaks.
"""
print("hello","world",sep="")
"""


# 7. **Variable Printing:**
# - Develop a program that takes user input and prints a personalized greeting.
"""
a=input("enter a name:")
print("hello",a)
"""


# 8. **Number Printing:**
# - Create a program that prints the result of a mathematical expression.
"""
a=int(input("enter a number"))
b=int(input("enter another number"))
print("sum is",a+b)
print("difference is",a-b)
print("product is",a*b)
print("division is",a/b)

"""


# 9. **Precision Printing:**
# - Write a program that uses formatted strings to print a floating-point number with two
# decimal places.
"""
num=float(input("enter a decimal number"))
print(f"the number with 2 decimal places: {num:.2f}")

"""



# 10. **Print with Separator:**
# - Develop a program that prints multiple items separated by a specific character.
"""

a=input("enter a name")
b=int(input("enter a number"))
print(a,b,sep=" @ ")

"""

# 11. **Printing Variables and Constants:**
# - Create a program that prints the value of a variable and a constant.
"""
a=int(input("enter a number:"))
print(a)

"""


# 12. **Print with End Parameter:**
# - Write a program that prints multiple items with a custom `end` parameter.
"""

a=int(input("enter a number:"))
b=input("enter a name:")
print(a,b,end="..")

"""

# 13. **Printing Raw Strings:**
# - Develop a program that uses a raw string to print a path without interpreting escape
# characters.
"""

path=r"D:\python\empty.pdf"
print(path)

"""



# 14. **Print with Triple Quotes:**
# - Create a program that uses triple-quoted strings to print a multi-line message.








# 15. **Printing Special Characters:**
# - Write a program that prints special characters (e.g., copyright symbol, newline) using
# Unicode escape sequences.





# 16. **Print with Separator and End:**
# - Develop a program that uses both the `sep` and `end` parameters in the `print` function.






# 17. **Formatted Output with Arithmetic:**
# - Create a program that uses formatted strings to print the result of an arithmetic
# expression.






# 18. **Print with File Parameter:**
# - Write a program that prints to a file using the `file` parameter in the `print` function.








# 19. **Conditional Printing:**
# - Develop a program that uses the `print` function inside a conditional statement.









# 20. **Print with f-strings:**
# - Write a program that uses f-strings to print variables and expressions.