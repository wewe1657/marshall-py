# Lesson 4
from math import ceil
#input
section1 = input("Enter section 1:")
section2 = input("Enter section 2:")
section3 = input("Enter section 3:")

#processing
cans = len(section1)+len(section2)+len(section3)

boxes = ceil(cans / 12)

leftover = 12*boxes - cans

totalcost = 14.95 * boxes

#output
print(f"we have {leftover} cans")
print (f"the cost is {totalcost}")
print(f"we need {cans} to paint the fences")
