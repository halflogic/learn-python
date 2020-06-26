
# FizzBuzz code exercise
"""
Print 1 to 100, 
for numbers divisible by 3 print Fizz,
for numbers divisible by 5 print Buzz,
for numbers divisible by 3 and 5 print FizzBuzz
"""
maxnum = 100

for num in range (1, maxnum+1):  # you add 1 to maxnum for range to include it
    if num % 15 ==0:
        print(num, "FizzBuzz")
    elif num % 3 == 0:
        print(num, "Fizz")
    elif num % 5 ==0:
        print(num, "Buzz")
    else:
        print(num)
