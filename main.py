def primeLst(lst):
  primeT1 = True
  outputList = []
  for i in range(0, len(lst) - 1):
    num1 = lst[i]
    if num1 % 2 != 0:
      for a in range(3, num1 - 1):
        if lst[i] % a == 0:
          primeT1 = False
    else:
      primeT1 = False
    if primeT1 == True:
      outputList.append(num1)
    primeT1 = True
  return outputList
  
print("1. Prime Numbers -",primeLst([48,10,71,61,23,75,25,89,83,81]))
print("2. Prime Numbers -",primeLst([48,77,36,65,58,100,41,89,97,29]))
print("3. Prime Numbers -",primeLst([88,51,29,92,45,66,55,74,89,34]))
print("4. Prime Numbers -",primeLst([24,72,67,86,88,93,33,82,28,17]))