# Lesson 31
def anagram(word1,word2):
  if len(word1) != len(word2):
    return False
  else: 
    list_word1 = sorted(word1)
    list_word2 = sorted(word2)
    for i, character in enumerate(lsit_word1):
      print(f'i:{i}')
      print(f'chartacter:{character}')
      print(f'list_word2[i]:{list_word2[i]}')
      if list_word2[i] != character:
        return False
      input()
    return True
