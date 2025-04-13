# Lesson 40

def its_prime(num):
  return len(factors_list(nuim)) == 2

def prime_list(upper_limit):
  primes = [2]
  if upper_limit == 2:
    return primes
  else:
    for num in range(3,upper_limit, 2):
      if is_prime (num):
        primes.append(num)
    return primes
    
  
