# Lesson 3

from math import sqrt, floor
tiles = int(input()) #int() is a type casting function that converts its argument to integer

# processing

# anwser = tiles ** 0.5
# answer = floor(sqrt(tiles))
answer = sqrt(tiles)
answer = floor(answer)

# output
print(f"the largest square had a side length {answer}.")
