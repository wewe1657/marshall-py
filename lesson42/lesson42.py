# Lesson 42
def possible_sum(a_liust,target):
  for i, value in enumerate(a_list):
    new_target = target - value
    if new_target in a_list[i+1:]:
      return True

  return False

test = [1,2,3,4,5,6,7]
target = 4

print(f"can {target} be made from two unique values in: {test}")
print(possible_sum(test,target))
