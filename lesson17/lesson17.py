# Lesson 17

num = int(input("enter a value of N: "))

totalProduct = 1
multiplier = 1

while multiplier <= num:
  totalProduct = totalProduct* multiplier
  multiplier = multiplier + 1

print(f"factorial of {num} is {totalProduct})
