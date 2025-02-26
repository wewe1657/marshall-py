# Lesson 8

game1 = input("enter game 1 result: ")
game2 = input("enter game 2 result: ")
game3 = input("enter game 3 result: ")
game4 = input("enter game 4 result: ")
game5 = input("enter game 5 result: ")
game6 = input("enter game 6 result: ")

win_counter = 0
for i in range(6):
    current_result = input(f"enter the game {i+1} resuilt:")

  if current_result == "W":
      win_counter += 1


group = 0
if win_counter > 4:
  group = 1
elif win_counter > 2:
  group = 2
elif win_counter > 0:
  group = 3

if group == 0:
    print("the player elimanated")
else 
    print("the player has been placed in group {group}.")
