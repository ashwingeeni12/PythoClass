def factorial(num):
    output = 1
    for num in range(1, num + 1):
      output = num * output
      num = num - 1
    print(int(output))
    output = 1

#don't change anything below this
factorial(5)
factorial(4)
factorial(9)
factorial(24)
factorial(17)