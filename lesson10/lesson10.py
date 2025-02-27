# Lesson 10

from random import choice

invalid = true
player = ""

while invalid:

  player = input("enter a choice of rock, paper or scissors")

if player in ('rock', 'paper', scissors'):
  invalid = false




cpu = choice (['rock', 'paper', scissors'])

if player == cpu:
  print("tie game")
 else:

if player == 'rock':
  if cpu == 'paper':
    print("the cpu has won")
else:
  print("the player has won")

 elif player == 'paper':
  if cpu == 'scissors':
    print("the CPU has won the game")
  else:
    print("The player has won")

else:
  if cpu == 'rock':
    print("the cpu has won tha game")
  else: 
    print("player has won the game")
               
