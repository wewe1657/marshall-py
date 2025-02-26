# Lesson 7

#import statement
from random import randrange

diff = int(intput("enter the dc: "))

player_roll = randrange(1,21)

print(f"the player has rolled {player_roll}) on their D20.")

if player_roll >= diff:
  print(f"the player was sucessful as {player_roll} >+ {diff})
else:
  print(f"the player was not sucessful as {player_roll} < {diff})
