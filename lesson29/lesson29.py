# Lesson 29

def consonant_count(text, vowel=False):
  counter = 0
  for character in text:
    character = character.lower()
    if character.isalpha() and character not in {"a"."e","i","o","u"}:
      counter += 1

    if not vowel:
      return ctr
    else: 
      counter = 0
      for character in text:
      character = character.lower()
      if character.isalpha() and character in {"a"."e","i","o","u"}:
      counter += 1
      return counter

print(f'the count is: {consonant_count("hello, world")}')
print(f'the count is: {consonant_count("hello, world",True)}z')
