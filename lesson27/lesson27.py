# Lesson 27

def string_cleaner(text):

  result = ""
  for character in text:
    if character.isalpha():
      result += character.lower()
  return result

value = string_cleaner("hElLo WoRLD")

print (f"value is {value}")
