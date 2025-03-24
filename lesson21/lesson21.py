# Lesson 21

upperLimit = int(input("enter N:"))

maxCount = 0 
resultNum=0

for num in range(1,upper_limit+1):
  totalFactors = 0

for divider in range(1,num+1):
  if num%divider == 0:
    totalFactors+=1
    
if totalFactors > maxCount:
  maxCount = totalFactors
  resultNum=num

print(f"{resultNum} had the most factors with {maxCount} factors.")
