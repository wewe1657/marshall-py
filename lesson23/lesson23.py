# Lesson 23

total_sum = 0
counter = 0

while True:

  userInput = input("eneter the mark (Exit) to stop inputing")

if userInput.lower().capitalize() == "Exit":
  break:
else:
  mark = int(userInput)
  if 0 <=mark<=199:
  total_sum += mark
  counter+= 1
  else:
    print("invalid input

average = total_sum / counter

print(f"averege is {average}")



  
