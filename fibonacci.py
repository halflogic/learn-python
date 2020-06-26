# Generate Fibonacci sequence using list
# 1 1 2 3 5 8 13 21
# fib = [1, 1 ,2, 3, 5]

fib = [1, 1]
maxlen = 100    # set max length of sequence
maxnum = 1000   # set the highest number in the sequence

# Break sequence if any of the max limit is reached
for i in range(2, maxlen):
    fib.append(fib[i-2] + fib[i-1])
    if fib[i] > maxnum:
        fib.pop()   # remove the last number in the sequence if exceeds maxnum
        break

print(fib) 
print("Sequence length: " + str(len(fib)))

for x in fib:
    print(x)