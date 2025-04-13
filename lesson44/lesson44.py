# Lesson 44
def frequency(word):
  clean_word = sorted(word.lower())
  answer = {}
  for character in clean_word:
    if character not in answer:
      answer[character] = 1
    else:
      answer[character] += 1
  return answer
  
