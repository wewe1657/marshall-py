# Lesson 12

month = int(input())
day = int(input())

if month == 2 and day == 18:
  print ("special")
else:
  if month < 2:
    print("before")
  elif month > 2:
    print ("after")
  else:
    if day <  18:
      print("before")
  else:
      print("after")

  
  
