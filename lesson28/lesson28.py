# Lesson 28

def is_palindrome1(text):

  return text == text[::-1]

def is_palindrome2(text):

  if not text:
    return True
  elif len(text)<4:
    return text[0] == text[-1]
  else:
    midpoint=len(text)//2
    for i in range(0,midpoint):
      left = text[i]
      right = text[-1*1 -1]
      if left != right:
        return False
    return True

print(is_palindrome1("tacocat"), is_palindrome2("tacocat"))
print(is_palindrome1("tacodog"), is_palindrome2("tacodog"))
