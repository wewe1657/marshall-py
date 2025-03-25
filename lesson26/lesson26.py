# Lesson 26

def is_divisible(num1, num2):
  return num1 % num2 ==0

def factor_count(number):
  counter = 0
  for divider in range 1, number+1):
  if number % divider ==0:
    counter += 1
  return counter



upper_limit = int(input("Enter N:"))

for num in range (1, upperlimit+1):
  factor_size = factor_count(num)
  print(f"{num} has {factor_size} factors.")
