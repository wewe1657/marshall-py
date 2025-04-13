# Lesson 38

def is_palindrome(text):
  return text == text[::-1]
palindromeic_numbers = []
for num1 in range(999,99,-1):
  for num2 in range(999,99,-1):
    current_product = num*num2
    if is_palindrom(str(current_product)):
      palindromic_numbers.append(current_product)

print(f"the largest palindromic num in the list is: {max(palidromic_numbers)}")
