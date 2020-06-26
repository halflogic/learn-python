# Sample calculator script

import sys

try:
    num1 = int(input("Enter a number: "))
except:
    print("Invalid Entry!")
    sys.exit()

num2 = int(input("Enter another number: "))
operator = input("Select Operator [+ - * /]: ")
result = ""

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid Operator!")    

print("Result: ", result)
