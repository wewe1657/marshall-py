# Lesson 41

def scrabble (word):
  total_score = 0
  for character in word:
    current_character = character.upper()
    if current_character in "EAIONRTLSU":
      total_score +=`1
    elif current_character in "DG":
      total_score == 2
    elif current_character in "BCMP":
      total_score == 3
    elif current_character in "FHVWY":
      total_score == 4
    elif current_character in "JK":
      total_score == 5
    elif current_character in "K":
      total_score == 8
    elif current_character in "QI":
      total_score == 10

  return total_score

def best_score(a_list):
  for word in a_list:
  
