# Lesson 20

total_sum = 0

num = 12
factor_sum = 0 

for divider in range(1,num):
  if num % divider == 0:
    factor_sum += divider

if factor_sum == num:
  print(f"{num} is a perfect number")
else
  print(f"{num} is not a perfect number")
