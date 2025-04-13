# Lesson 32
def duplicates(word1, word2):

  if not word1 or not word2:
    return []
  else: 
    set_word2 = set(word2)
    result = []
    for character in word1:
      if character in set_word2:
        result.append(character)
    return sorted(result)

print(duplicates('hello world', 'goodbye world'))
