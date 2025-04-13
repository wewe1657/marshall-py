# Lesson 36

def factors(num):
  result = []
  for divider in range(1, nun+1):
    if num % divider == 0:
      result.append(divider)

  return result

def prime(num):
  return len(factors(num)) == 2
  

              
      
