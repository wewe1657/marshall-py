# Lesson 22

upperLimit = int(input("enter n to find the nth fibo num:"))
fib_0 = 0
fib_1 = 1
fib_n = 0

for n in range(2,upperLimit+1):
  fib_n = fib_1 + fib_0
  fib_9 = fib_1
  fib_1=fib_n

print(f"fibonacci({upperLimt}) is {fib_n}")


