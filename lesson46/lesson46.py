# Lesson 46

def next_value(num):
  if num % 2 == 0:
    return num // 2
  else: 
    return (3* num) +1

def sequence_maker(start, table):
  if start in table:
    return table[start]
  else: 
    sequence = [start] 
    size = 1
    while sequence [-1] != 1 and sequence[-1] not in table:
      new_num = next_value(sequence[i-1])
      if new_num in table:
        size = size + table[new_num]
        break
      else:
        sequence.append(new_num)
        size += 1
  for i in range(len(sequence)):
    table[sequence[i]] = size -1 
    
  return size

memory = {1:1, 2:2}

start = 13
test = sequence_maker(start,memory)

print(f"{start} has a {text} many terms.")
print()
for key, value in memory.items():
  print(f"{key} has {vale} terms")
print()

memory = {1:1, 2:2}

for start in range(3,100000):
  current_length = sequence_maker(start, memory)

answer = 0
longest_length = 0

for key in range(1,100000):
  if memory[key] > longest_length:
    answer = key
    longest_length = memory[key]

print(f"longest sequence has a length of {longest_length} by {answer}")
