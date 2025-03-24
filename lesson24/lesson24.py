# Lesson 24

name = ""

longestLength = 0
longestName = ""

while name != "x":
  name = input("enter a name or "X" to exit.:")
  if name != "X":
    currentLength = len(name)

    if currentLength > longestLength:
      longestLength = currentLength
      longestName = name

  else:
    print("end of input")

if longest_name:
  print(f"the longest name with {longestLength} characters is {longestName}")
else:
  print("not enough data.")
  
