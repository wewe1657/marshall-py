# Lesson 43

def r_dupe(a_list):
  result = []
  for value in a_list:
    if value not in result:
      result.append(value)
  return result

def unique_letters(a_list):
  result_set = set()
  for word in a_list:
    tmp_set = set(word)
    result_set = result_set | (tmp_set)
  return result_set

def i_count(a_list):
  if a_list:
    result_set = a_list[0]
    for example_set in a_list [1:]:
      result_set = result_set & example_set
    return len(result_set)
    
  
